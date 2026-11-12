import pandas as pd 
import numpy as np
from sentence_transformers import SentenceTransformer
from sentence_transformers import util
from rank_bm25 import BM25Okapi

#embedding model & bm25
model = SentenceTransformer('\\Users\\CAAH148734\\Downloads\\sentence-transformers_all-MiniLM-L6-v2\\sentence-transformers_all-MiniLM-L6-v2')

hazardlog = pd.read_excel("hazardlog.xlsx")
requirements = pd.read_excel("requirements.xlsx")

#Specific data into lists
def text_data(hazardlog, requirements):
    """Extracts the primary text and hazard text from the provided DataFrames.
    
    arguments: 
        hazardlog: DataFrame containing hazard log data.
        requirements: DataFrame containing requirement data.
    
    returns: 
        primary_text_list: List of primary text from requirements DataFrame.
        hazard_text_list: List of concatenated hazard text from hazardlog DataFrame.
    
    """
    primary_text_list = requirements["Primary Text"].dropna().tolist()
    hazard_text_list = (
        hazardlog
        .fillna("")
        .astype(str)
        .apply(" ".join, axis=1)
        .tolist()
    )
    return primary_text_list, hazard_text_list

#cosine comparison storing in a similarity matrix 
def cosine_comparison(hazard_text_list,primary_text_list):
    """Computes the cosine similarity between primary text embeddings and hazard text embeddings.
    
    arguments:
        primary_text_list: List of primary text from requirements DataFrame. 
        hazard_text_list: List of concatenated hazard text from hazardlog DataFrame.

    returns:
        semantic_scores: 2D array of cosine similarity scores between primary text and hazard text.
    """
    #Embedding the texts using the SentenceTransformer model
    primary_text_embeddings = model.encode(primary_text_list, convert_to_tensor=True)
    hazard_text_embeddings = model.encode(hazard_text_list, convert_to_tensor=True)

    #Calculating cosine simularity and returning a 2D array of similarity scores
    semantic_scores = util.cos_sim(primary_text_embeddings, hazard_text_embeddings).numpy()
    return semantic_scores

#BM25 comparison
def bm25_comparison(hazard_text_list, primary_text_list):
    """Computes the BM25 similarity between primary text and hazard text.
    
    arguments:
        hazard_text_list: List of concatenated hazard text from hazardlog DataFrame.
        primary_text_list: List of primary text from requirements DataFrame.
    
    returns:
        bm25_scores: 2D array of BM25 similarity scores between primary text and hazard text.
    """

    #Seperates the hazard text into individual words for comparison
    tokenized_hazard = [text.split() for text in hazard_text_list]
    bm25 = BM25Okapi(tokenized_hazard)

    #Calculates the BM25 scores for each primary text against the hazard text returning a 2D array of scores
    bm25_scores = []
    for text in primary_text_list:
        score = bm25.get_scores(text.split())
        bm25_scores.append(score)
    return np.array(bm25_scores)


#RRF comparison
def rrf_comparison(semantic_scores, bm25_scores, k=60):
    """Combines cosine similarity and BM25 scores using Reciprocal Rank Fusion (RRF).

    arguements: 
        semantic_scores: 2D array of cosine similarity scores.
        bm25_scores: 2D array of BM25 similarity scores.
        k: Constant for RRF calculation.
    
    returns:
        ranked_results:
    """
    ranked_results =  []

    #Note: semantic scores and bm25_scores have the same shape
    for i in range(len(semantic_scores)):

        #Get the ranks for each score
        semantic_ranks = np.argsort(-semantic_scores[i]) + 1  # Adding 1 to avoid division by zero
        bm25_ranks = np.argsort(-bm25_scores[i]) + 1

        #Calculate RRF scores
        rrf_scores = (1 / (k + semantic_ranks)) + (1 / (k + bm25_ranks))
        ranked_results.append(rrf_scores)

    return np.array(ranked_results)


    




