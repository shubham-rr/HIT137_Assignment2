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