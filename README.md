# Document-Term Matrix using TF-IDF Weights

## Description

This Python program reads a CSV file, processes the text by removing stopwords and applying stemming, and then constructs a document-term matrix using TF-IDF weights. The program outputs the resulting matrix in a tabular format.

## Features

- **Stopword Removal**: Removes specified pronouns and conjunctions from the text.
- **Stemming**: Converts words to their root forms using a predefined mapping.
- **TF-IDF Calculation**: Computes Term Frequency-Inverse Document Frequency (TF-IDF) weights for each term in each document.
- **Document-Term Matrix**: Outputs a matrix displaying TF-IDF weights for each term in each document.

## Files

- `indexing.py`: The main Python script that performs all the operations.
- `collection.csv`: The input CSV file containing the documents.
