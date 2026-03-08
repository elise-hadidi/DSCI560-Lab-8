import sys
import pandas as pd
from nltk.tokenize import sent_tokenize, word_tokenize
from gensim.models import Word2Vec
import gensim
import nltk
from sklearn.cluster import KMeans
import numpy as np

def tokenize(text_list):
    data = []

    for text in text_list:

        for i in sent_tokenize(text):

            temp = []
            for j in word_tokenize(i):
                temp.append(j.lower())
        
            data.append(temp)
    return data

def create_bins(model, num_bins):
    words = list(model.wv.index_to_key)
    vectors = np.array([model.wv[word] for word in words])

    return KMeans(n_clusters=num_bins, random_state=42).fit(vectors)

def generate_bow_embedding(text, model, kmeans, k):
    bow_vector = np.zeros(k)
    words = text.split()
    if not words:
        return bow_vector
    for word in words:
        if word in model.wv:
            word_vector = model.wv[word].reshape(1, -1)
            cluster_label = kmeans.predict(word_vector)[0]
            bow_vector[cluster_label] += 1
    bow_vector /= len(words)
    return bow_vector

def main():
    if len(sys.argv) != 4:
        print("Usage: python w2vBOW.py <input_file> <output_file> <num_bins>")
        return
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    num_bins = int(sys.argv[3])

    nltk.download('punkt_tab')

    df = pd.read_csv(input_file)
    texts = df['text'].tolist()
    for i, text in enumerate(texts):
        cleaned = text.replace('\n', ' ').replace('\r', ' ')
        texts[i] = cleaned

    data = tokenize(texts)

    model2 = gensim.models.Word2Vec(data, min_count=1, vector_size=100, window=5, sg=1)

    kmeans_model = create_bins(model2, num_bins)

    embeddings = []

    for text in texts:
        bow_embedding = generate_bow_embedding(text, model2, kmeans_model, num_bins)
        embeddings.append(bow_embedding)

    df['bow_embedding'] = embeddings
    print('Outputing to file...')
    df.to_csv(output_file, index=False)

if __name__ == "__main__":
    main()