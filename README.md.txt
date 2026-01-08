# Financial Insight Project – Financial NER

This project focuses on extracting key financial information from text and PDF
documents using a Financial Named Entity Recognition (NER) system based on FinBERT.

## Datasets
Due to size constraints, raw datasets are not included in this repository.
Datasets were loaded from Google Drive during development.
All generated outputs are provided in this repository.


## Milestones

### Milestone 1: Data Collection & Preprocessing
- Collected multiple financial text datasets
- Cleaned and normalized text data
- Performed tokenization, stopword removal, and lemmatization
- Conducted Exploratory Data Analysis (EDA)

### Milestone 2: Financial NER Model Training
- Defined financial entity labels using BIO format
- Prepared BIO-tagged training data
- Fine-tuned FinBERT for financial NER
- Evaluated the model using precision, recall, and F1-score

### Milestone 3: Model Inference
- Applied the trained model to unseen financial sentences
- Extracted financial entities
- Generated structured JSON outputs

### Milestone 4: PDF-Based Financial Information Extraction
- Extracted text from financial PDF documents## Project Files

- `FinancialInsights.ipynb` – Complete implementation of all milestones
- `input.pdf` – Sample PDF input used in Milestone 4
- ner_text_for_biotagging_3000 (1)– Output generated from model inference
- `milestone4_output.json` – Financial data extracted from PDF
- `financial_ner_bio.txt` – BIO-tagged sample data

- Identified sections such as MD&A, Risk Factors, and Balance Sheet
- Extracted financial metrics, values, and periods
- Generated structured JSON output from PDFs





## Technologies Used
- Python
- HuggingFace Transformers
- FinBERT
- PyTorch
- PDFPlumber
- Pandas
- NumPy
- NLTK



