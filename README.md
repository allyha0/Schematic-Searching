# Hazard Similarity Tool
A python-based tool that compare the hazard descriptions and requirements from Excel spreadsheets using AI embeddings and cosine similarities to identify similar records.

## Table of Contents
- [Problem](#problem)
- [Solution](#solution)
- [Features](#features)
- [Technology Stack](#technology-stack)


## Problem
Currently, WSP Global's Safety team maintains extensive hazard logs and project requirements that are manually reviewed and cross-referenced to identify the standards and design requirements. This process is time consuming and difficult to maintain due to the time-consuming manual work to cross-check between the project requirements. These requirements have broad descriptions that are difficult to compare through the numerous rows of the hazard logs. 

As a result, the team is seeking an AI-assisted solution that automatically compares project requirements and hazard records using sematic similarity. By leveraging an embedding model and cosine similarity, the tool will identify related requirements to hazards reducing manual effort and improving consistency across projects.

## Solution
This Hazard similarity tool aims to identify relationships between project requirements and hazard log entries. Rather than relying fully on manual keyword searches, this tool converts the requirements and hazards into vector embeddings, allowing comparisons based on semantic meaning. Since this tool can't have embedding models, the embedding values will be outputted in the provided .xlsx files. The tool then uses cosine similarity to perform an exhaustive search to cross-check between the data.  

This approach helps identify related requirements, risks, mitigations, and safety controls even when they are written using different terminology.

## Features 
1. Importing hazard logs and project requirements
2. Generating embedding values
3. Comparing through co-sine similarity
4. Ranking and Scoring the matches
5. Export results for stakeholder review 

## Technology Stack
- Python
- Pandas
- Numpy
- Scikit-Learn
- Sentence Transformers
- OpenPyXL

## Useage of AI 
Throughout this project I kept in mind that it was for me to learn the foundation of schematic searching, thus throughout I've utlized AI for support on basic Python scripts and support in learning by asking questions and support for bug fixing. For example, unknowingly using newest version of Python which does not support sentence-transformers needed for a program that is embedding sentences without a downloaded model. 

NOTE: Throughout this process I will keep track on what I used AI for and also what AI was not helpful with.

## Resources
In this list I added some resources that supported my learning and understanding the different concepts. 
1. BM25 Methods: https://4d9506f4.isolation.zscaler.com/profile/66efb910-9c57-401a-bef6-d39c8ae10b8d/zia-session/?controls_id=f4fc2f0c-82bc-4a39-a7a7-b01e9efb1b8b&tenant=9240298949af&region=was&user=656f920f9d17163e882b294f62c8a3f7bb1f5e42060153a72fbc8eed626cf3f5&original_url=https%3A%2F%2Flink.springer.com%2Fchapter%2F10.1007%2F978-3-030-45442-5_4&key=sh-1&hmac=6c797191676e2658f5f0b30a2be0324216c80a2bf84d14d81c72493c6a47a355
2. RRF (Reciporcal Rank Fusions): https://learn.microsoft.com/en-us/azure/search/hybrid-search-ranking
3. 

