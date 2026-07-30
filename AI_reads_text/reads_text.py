from sklearn.feature_extraction.text import CountVectorizer

email = [
    "win money now",
    "free money",
    "happy birthday"
]
vectorizer = CountVectorizer()

vectorizer.fit(email)
print("Vocabulary :")
print(vectorizer.vocabulary_)

x = vectorizer.transform(email)

print("\n Numeric Representation :")
print(x.toarray())