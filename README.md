# FinanceInsight-NER

## Project Title
Developing Named Entity Recognition (NER) Models for Financial Data Extraction

## Description
FinanceInsight-NER is a Python-based backend project that demonstrates how Named Entity Recognition (NER) can be used to extract important entities from financial text data.  
The project focuses on identifying entities such as Person Name, Organization, Date, and Monetary Values from financial statements or transaction-like sentences.

## Objective
- To understand the concept of Named Entity Recognition (NER)
- To extract meaningful financial entities from unstructured text
- To apply NLP concepts in a real-world financial use case

## Technologies Used
- Python
- Regular Expressions (Regex)
- Basic NLP concepts

## Project Structure
- ner_demo.py : Main Python file for demonstrating NER
- README.md : Project documentation

## How It Works
The system takes a sample financial sentence as input and identifies:
- PERSON
- ORGANIZATION
- MONEY
- DATE  

Entity extraction is done using pattern matching techniques to simulate NER behavior.

## Sample Input
Rutuja invested ₹50,000 in Infosys on 12 Jan 2026.

## Sample Output
PERSON: Rutuja  
ORG: Infosys  
MONEY: ₹50,000  
DATE: 12 Jan 2026

## Real-Life Applications
- Banking transaction analysis
- Invoice processing
- Financial document automation
- Fraud detection systems
- Expense tracking tools

## Limitations
- This is a demo-level implementation
- Advanced ML-based NER models require additional libraries and stable environments

## Conclusion
This project demonstrates the practical understanding of Named Entity Recognition and its importance in financial data extraction. It serves as a strong foundation for advanced NLP-based financial analytics systems.
