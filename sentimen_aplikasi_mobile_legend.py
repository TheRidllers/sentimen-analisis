# -*- coding: utf-8 -*-
"""Sentimen Aplikasi Mobile Legend.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/174JYaSne-NXfxN5lZzgcDbiTPneF4gmq

# Bagian Baru
"""

!pip install sastrawi
!pip install tensorflow
!pip install scikit-learn
!pip install pandas nltk wordcloud requests matplotlib seaborn
!pip install lightgbm xgboost catboost
!pip install dask[dataframe]

!pip install google-play-scraper

from google_play_scraper import Sort, reviews
from google_play_scraper import app
import pandas as pd
import numpy as np

result, continuation_token = reviews(
      'com.mobile.legends',
      lang='id', #bahasa
      country='id', #negara
      sort=Sort.MOST_RELEVANT, #sorting yang paling relevan
      count=1000, #jumlah dataset
      filter_score_with= None #Isi dengan 1, 2, 3, 4, 5 None jika ingin bercampur
)

# Dataframe dengan nama
data = pd.DataFrame(np.array(result),columns=['review'])
data = data.join(pd.DataFrame(data.pop('review').tolist()))
data.head()

len(data)

data = data[['content','score']]
data.head()

data = data.rename(columns={'content': 'ulasan', 'score': 'value'}) #mengganti nama fitur
data.head()

data.to_csv("ulasan mole 1000 Data.csv", index = False  , encoding='utf-8')

dataMole = pd.read_csv('/content/ulasan mole 1000 Data.csv')
dataMole.head()

"""Selanjutnya mengolah data scrapp"""

df = pd.read_csv("ulasan mole 1000 Data.csv")

df.head(10)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
from nltk.corpus import stopwords
import nltk.tokenize as word_tokenize
from wordcloud import WordCloud

data = pd.read_csv('ulasan mole 1000 Data.csv') # Ganti 'nama_file.csv' dengan nama file anda

data.head()

import pandas as pd
import nltk
from nltk.corpus import stopwords

# ... (kode lainnya)

# Unduh stopwords
nltk.download('stopwords')

# Buat set stopwords
stop_words = set(nltk.corpus.stopwords.words('english'))

# Hapus stopwords dari teks
data['clean_text'] = data['clean_text'].apply(lambda x: ' '.join([word for word in x.split() if word not in stop_words]))

# menggabungkan semua ulasan menjadi satu
all_text = ' '.join(data['clean_text'])

# membuat wordcloud
wordcloud = WordCloud(width=800, height=500, max_font_size=150, random_state=42).generate(all_text)

# menampilkan wordcloud
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

stop_words = set(stopwords.words('indonesian'))
stop_words.update(['dan', 'yang', 'lalu', 'yg', 'gk', 'saya', 'lagi', 'di', 'ini', ''])

data['clean_text'] = data['ulasan'].str.replace('[^\w\s]', '')
data['clean_text'] = data['clean_text'].str.lower()
data['clean_text'] = data['clean_text'].apply(lambda x: ' '.join([word for word in x.split() if word not in stop_words]))

all_text = ' '.join(data['clean_text'])

wordcloud = WordCloud(width=800, height=400, max_font_size=150, random_state=42).generate(all_text)
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

"""melakukan sentimen analisis"""

import nltk
nltk.download('vader_lexicon')

from nltk.sentiment import SentimentIntensityAnalyzer

# menginisiasi SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

# menghitung sentimen untuk setiap ulasan
data['sentiment'] = data['clean_text'].apply(lambda x: sia.polarity_scores(x)['compound'])

# melabel sentimen (misalnya, 'positif', 'negatif', 'netral') berdasarkan nilai sentimen
data['sentiment_label'] = data['sentiment'].apply(lambda x: 'positif' if x > 0 else ('negatif' if x < 0 else 'netral'))

# menampilkan beberapa ulasan dan sentimen terkait
data[['ulasan', 'sentiment_label']].head(10)

data.to_csv("hasil ulasan mole 1000 Data.csv", index = False  , encoding='utf-8')