import pandas as pd 
import numpy as np
from sentence_transformers import SentenceTransformer
model = SentenceTransformer('\\Users\\CAAH148734\\Downloads\\sentence-transformers_all-MiniLM-L6-v2\\sentence-transformers_all-MiniLM-L6-v2')

hazardlog = pd.read_excel("hazardlog.xlsx")
requirements = pd.read_excel("requirements.xlsx")

#Specific data into lists
primary_text_list = requirements["Primary Text"].dropna().tolist()
hazard_list = hazardlog.values.tolist()

#embedding the primary text list into numbers for comparison 
primary_text_embeddings = model.encode(primary_text_list, convert_to_tensor=True)
print("Primary text embeddings shape:", primary_text_embeddings.shape)
