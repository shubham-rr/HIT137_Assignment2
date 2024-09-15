import pandas as pd
import os
import re

file_path = 'files/'

def cleaner(column_name, df):
    if column_name in df.columns:
        for line in df[column_name]:
            cleaned_line = re.sub(r'[^a-z\s]', '', line.lower())
            texts.append(cleaned_line)

# Read CSVs and extract 'text' column
texts = []
for file in os.listdir(file_path):
    if file.endswith(".csv"):
        df = pd.read_csv(os.path.join(file_path, file))
        cleaner('TEXT', df)
        cleaner('SHORT-TEXT', df)

# Write all texts to a single text file
with open('Question 1/extracted.txt', 'w') as f:
    for line in texts:
        f.write(line + '\n')
