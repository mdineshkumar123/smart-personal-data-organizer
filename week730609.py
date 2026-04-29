from sklearn.feature_extraction.text import TfidfVectorizer

def semantic_search(query):
    notes = load_notes()
    texts = [n["text"] for n in notes]

    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(texts)

    q_vec = vectorizer.transform([query])
    scores = (X * q_vec.T).toarray()

    return scores