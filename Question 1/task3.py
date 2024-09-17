# import statements
import csv
import nltk
from collections import Counter
from nltk.corpus import stopwords
from transformers import AutoTokenizer

file_path = 'Question 1/extracted.txt'

# Download NLTK stopwords dataset (only needed once)
nltk.download('stopwords', quiet=True)
stop_words = set(stopwords.words('english'))

# Function to clean text only (not to be used in Task 3.2 where we deal with tokens and chunks)
def clean_text(text):
    words = text.split() # split by whitespaces
    # filter words based on stopwords list and len > 2 to avoid unmeaningful words
    filtered_words = [word for word in words if word not in stop_words and len(word) > 2]
    return filtered_words

# Function to save the results into a CSV
def save_to_csv(data, file_name, headers):
    with open(file_name, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        writer.writerows(data)

## TASK 3.1
# Read and clean the text file
with open(file_path, 'r') as f:
    text = f.read()
filtered_words = clean_text(text)

# Count occurrences of filtered words
word_counts = Counter(filtered_words)

# Get the top 30 most common words
top_30_words = word_counts.most_common(30)

# Save results to CSV
save_to_csv(top_30_words, 'Question 1/top_30_words.csv', ['Word', 'Count'])
print('Task 3.1 finished! Please check the file top_30_words.csv')

#--------------------------------------------------------------------

## TASK 3.2
def count_unique_tokens(file_path, chunk_size=10000):
    tokenizer = AutoTokenizer.from_pretrained("dmis-lab/biobert-base-cased-v1.1") # Load BioBERT tokenizer
    token_counts = Counter() # initialize token counter

    # Open and process text file in chunks to avoid memory issues since the file is quite big
    with open(file_path, 'r') as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            tokens = tokenizer.tokenize(chunk) # tokenize text chunks
            # Clean and filter text with subword removal (that start with '##')
            filtered_tokens = [token for token in tokens if token not in stop_words and len(token) > 2 and not token.startswith('##')]
            token_counts.update(filtered_tokens) # Update token counts
            
    # Get the top 30 most common tokens
    top_30_tokens = token_counts.most_common(30)
    return top_30_tokens   

# Call the function for TASK 3.2
top_30_tokens = count_unique_tokens('Question 1/extracted.txt')
# Save results to CSV
save_to_csv(top_30_tokens, 'Question 1/top_30_tokens.csv', ['Token', 'Count'])
print('Task 3.2 finished! Please check the file top_30_tokens.csv')
