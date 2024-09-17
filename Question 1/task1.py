import pandas as pd
import os
import re

file_path = "files/"
output_dir = "Question 1/"
output_file = os.path.join(output_dir, "extracted.txt")


def cleaner(column_name, df):
    cleaned_lines = []
    if column_name in df.columns:  # check if column exists
        lines = df[column_name].dropna()  # Drop null values
        for line in lines:  # For each line/row in df[column]
            cleaned_line = re.sub(
                r"[^a-z\s]", "", line.lower()
            )  # Clean text and convert to lowercase
            cleaned_lines.append(cleaned_line)
    return cleaned_lines


# Create output directory if it doesn't exist

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Read CSVs and extract 'TEXT' and 'SHORT-TEXT' columns

texts = []
for file in os.listdir(file_path):
    if file.endswith(".csv"):  # For each CSV file
        df = pd.read_csv(os.path.join(file_path, file))
        texts.extend(cleaner("TEXT", df))  # Extend list with cleaned lines from 'TEXT'
        texts.extend(cleaner("SHORT-TEXT", df))  # Extend list with cleaned lines from 'SHORT-TEXT'

# Write all texts to a single text file

with open(output_file, "w") as f:
    for line in texts:
        f.write(line + "\n")
