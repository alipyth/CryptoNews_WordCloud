import streamlit as st
import requests
from bs4 import BeautifulSoup
from wordcloud import WordCloud
import matplotlib.pyplot as plt

r = requests.get('https://www.tradingview.com/markets/cryptocurrencies/news/')

soup = BeautifulSoup(r.content , "html.parser")
news = []
for i in soup.select('.title-rY32JioV'):
    news.append(i.text)


wordcloud = WordCloud(width=400 , height=400 , max_words=10 , stopwords=["or","with","news","crypto","is","to","of","a","Price","Market","SEC","s","and","the","New","Hinman","U","as","on","for","US"])
wordcloud.generate(" ".join(news))

plt.imshow(wordcloud)
plt.axis('off')
st.pyplot()
