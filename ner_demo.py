# Developing Named Entity Recognition (NER) Models for Financial Data Extraction

text = "RBI approved a loan of 5 crore rupees to Infosys in 2024."

entities = {
    "ORGANIZATION": ["RBI", "Infosys"],
    "MONEY": ["5 crore rupees"],
    "DATE": ["2024"]
}

print("Input Text:", text)
print("Extracted Entities:")
for key, value in entities.items():
    print(key, ":", value)
