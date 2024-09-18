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

# using test.txt as a sample of extracted.txt due to processing time constraints
file_path = "Question 1/test.txt" # Adjust to extracted.txt for actual results
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

# Function to extract entities using BioBERT
def extract_entities_biobert(text, valid_medical_labels):
    entities = []
    results = nlp_biobert(text)
    # print("Raw BioBERT results:", results)
    for entity in results:
        if not entity['word'].startswith('##') and len(entity['word']) > 2 and entity['word'].lower() not in stop_words:
            # print(f"Entity before mapping: {entity['word']} with raw label {entity['entity']}")
            # Map label
            label = label_mapping.get(entity['entity'], 'Unknown')
            # print(f"Mapped label: {label}")
            if label.upper() in valid_medical_labels:
                entities.append((entity['word'], label))
    return entities

# Function to filter medical terms
def filter_medical_terms(entities, valid_labels):
    return [(entity, label) for entity, label in entities if label in valid_labels]

# Function to count entities
def count_entities(entities):
    return Counter([ent[0] for ent in entities])

# Function to aggregate entity counts
def aggregate_entity_counts(entities_list):
    aggregated_counts = defaultdict(int)
    for entity, label in entities_list:
        aggregated_counts[(entity, label)] += 1
    return aggregated_counts

# Function to calculate total entities
def calculate_total_entities(entity_counts):
    return sum(entity_counts.values())

# Function to map entity names to their details
def create_entity_map(entities_set):
    return {entity[0]: {'entity': entity[0], 'label': entity[1]} for entity in entities_set}

# Function to get the most common entities
def get_most_common_entities(entities_count, top_n=30):
    return entities_count.most_common(top_n)


# --------------------------------------------------
# Main Processing
# --------------------------------------------------

# Read and process the text file
try:
    with open(file_path, "r") as file:
        text = file.read()
except FileNotFoundError:
    print(f"File not found: {file_path}")
    # Handle the error

# Clean and chunk the text
cleaned_text = clean_text(text)
chunked_texts = chunk_text(cleaned_text, tokenizer)


# Define entity labels
entity_labels_sci_spacy = ['ENTITY']
entity_labels_sci_spacy_bc5cdr = ['DISEASE', 'DRUG']
entity_labels_biobert = ['LABEL_0', 'LABEL_1']
valid_medical_labels = entity_labels_sci_spacy_bc5cdr

label_mapping = {
    'LABEL_0': 'Disease',
    'LABEL_1': 'Drug' 
}

# Extract entities
print("Extracting entities...")
entities_sci_spacy = []
entities_sci_spacy_bc5cdr = []
entities_biobert = []

for chunk in chunked_texts:
    entities_sci_spacy.extend(extract_entities_spacy(chunk, nlp_sci_spacy, entity_labels_sci_spacy))
    entities_sci_spacy_bc5cdr.extend(extract_entities_spacy(chunk, nlp_sci_spacy_bc5cdr, entity_labels_sci_spacy_bc5cdr))
    entities_biobert.extend(extract_entities_biobert(chunk, valid_medical_labels))

# --------------------------------------------------
# Analyze Entities
# --------------------------------------------------
# aggregate entity counts
agg_sci_spacy = aggregate_entity_counts(entities_sci_spacy)
agg_sci_spacy_bc5cdr = aggregate_entity_counts(entities_sci_spacy_bc5cdr)
agg_biobert = aggregate_entity_counts(entities_biobert)

# Calculate totals
total_sci_spacy = calculate_total_entities(agg_sci_spacy)
total_sci_spacy_bc5cdr = calculate_total_entities(agg_sci_spacy_bc5cdr)
total_biobert = calculate_total_entities(agg_biobert)

# Preparing to save summary of data

results_lines = []

# Total counts
results_lines.append(f"Total entities detected by SciSpacy: {total_sci_spacy}")
print(f"Total entities detected by SciSpacy: {total_sci_spacy}")
results_lines.append(f"Total entities detected by SciSpacy BC5CDR: {total_sci_spacy_bc5cdr}")
print(f"Total entities detected by SciSpacy BC5CDR: {total_sci_spacy_bc5cdr}")
results_lines.append(f"Total entities detected by BioBERT: {total_biobert}")
print(f"Total entities detected by BioBERT: {total_biobert}")

# --------------------
# Finding Common Entities between all models
# --------------------

# Convert aggregated counts to sets of entities
entities_sci_spacy_set = set(agg_sci_spacy.keys())
entities_sci_spacy_bc5cdr_set = set(agg_sci_spacy_bc5cdr.keys())
entities_biobert_set = set(agg_biobert.keys())

# Create maps for each set
sci_spacy_map = create_entity_map(entities_sci_spacy_set)
sci_spacy_bc5cdr_map = create_entity_map(entities_sci_spacy_bc5cdr_set)
biobert_map = create_entity_map(entities_biobert_set)

# Find common entities between sci_spacy and biobert
common_sci_spacy_biobert = set(sci_spacy_map.keys()) & set(biobert_map.keys())

# Find common entities between sci_spacy_bc5cdr and biobert
common_sci_spacy_bc5cdr_biobert = set(sci_spacy_bc5cdr_map.keys()) & set(biobert_map.keys())

# Find common entities between common_sci_spacy_biobert and common_sci_spacy_bc5cdr_biobert
common_entities_all_models = common_sci_spacy_biobert & common_sci_spacy_biobert

common_entities_all_models_txt = os.path.join(output_dir, "common_entities_all_models.txt")
with open(common_entities_all_models_txt, 'w', newline='') as file:
    for line in common_entities_all_models:
        file.write(line + "\n")
print(f"Common entities in all models saved at {common_entities_all_models_txt}")

# --------------------
# Finding most common entities in each model
# --------------------

counter_sci_spacy = Counter(agg_sci_spacy)
counter_sci_spacy_bc5cdr = Counter(agg_sci_spacy_bc5cdr)
counter_biobert = Counter(agg_biobert)

# Get the top 30 most common entities for each model
top_sci_spacy = get_most_common_entities(counter_sci_spacy)
top_sci_spacy_bc5cdr = get_most_common_entities(counter_sci_spacy_bc5cdr)
top_biobert = get_most_common_entities(counter_biobert)

# Preparing to save summary of most common entities
results_lines.append("\nMost common entities detected by SciSpacy:")
for entity, count in top_sci_spacy:
    results_lines.append(f"Entity: {entity}, Count: {count}")

results_lines.append("\nMost common entities detected by SciSpacy BC5CDR:")
for entity, count in top_sci_spacy_bc5cdr:
    results_lines.append(f"Entity: {entity}, Count: {count}")

results_lines.append("\nMost common entities detected by BioBERT:")
for entity, count in top_biobert:
    results_lines.append(f"Entity: {entity}, Count: {count}")

# Save the most common entities results to a text file
common_entities_output_file = os.path.join(output_dir, "most_common_entities.txt")
with open(common_entities_output_file, 'w') as file:
    file.write("\n".join(results_lines))

print(f"Most common entities have been saved to {common_entities_output_file}")

# --------------------------------------------------
# Prepare Data for CSV
# --------------------------------------------------

data_to_write = []

# Aggregate entities for SciSpacy
for (entity, label), count in agg_sci_spacy.items():
    data_to_write.append({'Model': 'SciSpacy', 'Entity': entity, 'Count': count, 'Label': label})

# Aggregate entities for SciSpacy BC5CDR
for (entity, label), count in agg_sci_spacy_bc5cdr.items():
    data_to_write.append({'Model': 'SciSpacy BC5CDR', 'Entity': entity, 'Count': count, 'Label': label})

# Aggregate entities for BioBERT
for (entity, label), count in agg_biobert.items():
    data_to_write.append({'Model': 'BioBERT', 'Entity': entity, 'Count': count, 'Label': label})

# --------------------------------------------------
# Write to CSV
# --------------------------------------------------

with open(output_file, 'w', newline='') as csvfile:
    fieldnames = ['Model', 'Entity', 'Count', 'Label']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for row in data_to_write:
        writer.writerow(row)

print(f"Results have been saved to {output_file}")
