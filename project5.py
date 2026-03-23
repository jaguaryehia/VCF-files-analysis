from textblob import TextBlob

b = TextBlob("This is a test")
translated = b.translate(to="ar", from_lang="en")
print(translated)
