#-------------------------------------------------------------------------
# AUTHOR: Wesley Dam
# FILENAME: indexing.py
# SPECIFICATION: This program reads a csv file and removes stopwords, stems words, and creates a document-term matrix using tf-idf weights.
# FOR: CS 4250- Assignment #1
# TIME SPENT: 7 hours
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard arrays

#Importing some Python libraries
import csv
import math

documents = []

#Reading the data in a csv file
with open('C:\\Users\\wesle\\OneDrive\\Desktop\\collection.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
         if i > 0:  # skipping the header
            documents.append (row[0])

#Conducting stopword removal for pronouns/conjunctions. Hint: use a set to define your stopwords.
#--> add your Python code here
stopWords = {"I", "She", "her", "They", "their", "and"}
for i in range(len(documents)):
    documents[i] = ' '.join([word for word in documents[i].split() if word not in stopWords])
print("After stopword removal: ", documents)

#Conducting stemming. Hint: use a dictionary to map word variations to their stem.
#--> add your Python code here
steeming = {
    "cats": "cat",
    "dogs": "dog",
    "loves": "love",
}
for i in range(len(documents)):
    documents[i] = ' '.join([steeming.get(word, word) for word in documents[i].split()])
print("After stemming: ", documents)

#Identifying the index terms.
#--> add your Python code here
terms = []
[terms.append(word) for doc in documents for word in doc.split() if word not in terms]
print("Index terms: ", terms)

#Building the document-term matrix by using the tf-idf weights.
#--> add your Python code here
docTermMatrix = []

def tf(term, doc):
    return doc.count(term) / len(doc.split())

def idf(term, documents):
    return math.log10(len(documents) / sum([1 for doc in documents if term in doc]))

def tf_idf(term, doc, documents):
    return (tf(term, doc) * idf(term, documents))

docTermMatrix = [[tf_idf(term, doc, documents) for term in terms] for doc in documents]
print("Values: ", docTermMatrix)

#Printing the document-term matrix.
#--> add your Python code here
print("Document-term matrix:")
print("\tlove\tcat\tdog")
for d, values in enumerate(docTermMatrix):
    print(f"Doc {d + 1}:", end = "\t")
    for t, val in enumerate(values):
        print(f"{val:.3f}", end = "\t")
    print()