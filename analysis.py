import pandas as pd
from textblob import TextBlob

dataset_path = '/Users/rahulkanwar/Desktop/IOCL/kaggle/Tweets.csv' 
df = pd.read_csv(dataset_path)

for index, row in df.iterrows():
    tweet = row['text']
    blob = TextBlob(tweet)
    sentiment = blob.sentiment.polarity
    
    if sentiment >= 0.3:
        sentiment_label = 'positive'
    elif sentiment < 0.0:
        sentiment_label = 'negative'
    else:
        sentiment_label = 'neutral'
   
    print(f"Tweet #{index+1}: '{tweet}'")
    print(f"Sentiment: {sentiment:.2f} (Label: {sentiment_label})")
    print("---")