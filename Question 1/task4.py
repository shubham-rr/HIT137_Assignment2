import spacy
import csv
import os
import nltk
from nltk.corpus import stopwords
from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForTokenClassification
from collections import defaultdict
from collections import Counter
 
# --------------------------------------------------
# File paths
# --------------------------------------------------
 
file_path = "Question 1/extracted.txt"
output_dir = "Question 1/"
output_file = os.path.join(output_dir, "entities_comparison.csv")
 
# --------------------------------------------------
# Download NLTK stopwords dataset
# --------------------------------------------------
 
nltk.download("stopwords", quiet=True)
stop_words = set(stopwords.words("english"))
 
# --------------------------------------------------
# Load Models
# --------------------------------------------------
 
print("Loading all models...")
# BioBERT
tokenizer = AutoTokenizer.from_pretrained("dmis-lab/biobert-base-cased-v1.1")
model = AutoModelForTokenClassification.from_pretrained("dmis-lab/biobert-base-cased-v1.1")
nlp_biobert = pipeline("ner", model=model, tokenizer=tokenizer)
 
# SciSpacy models
nlp_sci_spacy = spacy.load("en_core_sci_sm")
nlp_sci_spacy_bc5cdr = spacy.load("en_ner_bc5cdr_md")
 
print("Successfully loaded all models...")
 
# --------------------------------------------------
# Define Functions
# --------------------------------------------------
 
# Function to clean text
def clean_text(text):
    words = text.split()  # Split by whitespaces
 
    # Filter words based on stopwords list and len > 2 to avoid unmeaningful words
    filtered_words = [
        word for word in words if word not in stop_words and len(word) > 2
    ]
 
    # Join the filtered words back into a single string
    cleaned_text = " ".join(filtered_words)
    return cleaned_text
 
# Function to chunk text into smaller pieces
def chunk_text(text, tokenizer, max_length=512):
    tokens = tokenizer.encode(text, add_special_tokens=True, truncation=True, padding='longest', max_length=max_length)
    chunks = [tokens[i:i + max_length] for i in range(0, len(tokens), max_length)]
    chunk_texts = [tokenizer.decode(chunk, skip_special_tokens=True) for chunk in chunks]
    return chunk_texts
 
# Function to extract entities using SciSpacy
def extract_entities_spacy(text, model, entity_labels):
    doc = model(text) # en_core_sci_sm(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents if ent.label_ in entity_labels]
    return entities