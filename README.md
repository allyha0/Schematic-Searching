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
- NumPy
- OpenPyXL


