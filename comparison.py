import pandas as pd 
import numpy as np
from sentence_transformers import SentenceTransformer
from sentence_transformers import util

#embedding model 
model = SentenceTransformer('\\Users\\CAAH148734\\Downloads\\sentence-transformers_all-MiniLM-L6-v2\\sentence-transformers_all-MiniLM-L6-v2')

hazardlog = pd.read_excel("hazardlog.xlsx")
requirements = pd.read_excel("requirements.xlsx")

#Specific data into lists
primary_text_list = requirements["Primary Text"].dropna().tolist()

#combine all the columns of the hazardlog into a single list of strings for comparison
hazard_text_list = (
    hazardlog
    .fillna("")
    .astype(str)
    .apply(" ".join, axis=1)
    .tolist()
)
#embedding the primary text list into numbers for comparison 
primary_text_embeddings = model.encode(primary_text_list, convert_to_tensor=True)
hazard_text_embeddings = model.encode(hazard_text_list, convert_to_tensor=True)

#cosine comparison
scores = util.cos_sim(
primary_text_embeddings[0],
hazard_text_embeddings
)

