from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Data training sangat sederhana
texts = [
    "Gratis hadiah pulsa 50rb klik link ini",
    "Segera transfer uang Anda ke rekening kami",
    "Meeting besok jam 10 ya",
    "Jangan lupa bawa dokumen kantor",
    "Anda menang undian! Hubungi segera",
    "Ibu sudah masak di rumah"
]
labels = ["spam", "spam", "ham", "ham", "spam", "ham"]

# Convert text ke fitur numerik
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

# Train model Naive Bayes
model = MultinomialNB()
model.fit(X, labels)

print("=== AI Klasifikasi Spam Sederhana ===")
print("Ketik pesan, nanti akan diklasifikasikan sebagai 'spam' atau 'ham'")
print("Ketik 'exit' untuk keluar.\n")

while True:
    user_input = input("Pesan: ")
    if user_input.lower() == "exit":
        print("Sampai jumpa!")
        break
    X_new = vectorizer.transform([user_input])
    pred = model.predict(X_new)[0]
    print(f"AI: Pesan ini terdeteksi sebagai => {pred.upper()}\n")
