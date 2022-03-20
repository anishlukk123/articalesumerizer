import tkinter as tk
import nltk
from newspaper import Article
from textblob import TextBlob


nltk.download("punkt")
url = 'https://edition.cnn.com/2020/09/13/tech/microsoft-tiktok-bytedance/index.html'

article = Article(url);
article.download()
article.parse()

article.nlp()

print(article.summary);


analysis = TextBlob(article.text);

root = tk.Tk()
root.title("New Sumarizer")
root.geometry("1200x600")
root.mainloop()
tlabel = tk.label(root , text="title")