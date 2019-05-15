# Twitter Sentiment Analysis  

Performing Sentiment Analysis on Apple Tweets collected from the Twitter API Tweepy

## Overview

This project was broken up into 4 major parts:
  1. Gathering Data
  2. Data Preparation
  3. Vectorization and Embedding
  4. Model 

### Gathering Data

Using Twitters API "Tweepy" I collected tweets that contained "#apple". It's important for companies to be aware of how
others feel about them, and Apple is one the largest tech companies. 

### Data Preparation

As this is a NLP application, and with the foresight that we will need to vectorize these tweets, the tweets were cleaned and
tokenized. Additionally each Tweet was labeled with scores for Sentiment.


### Vectorization and Embedding

Using a TensorFlow backend and Keras, keras.layers was used to vectorize and embed each Tweet into an array to fit to a model
to analyze sentiment for 3 categories: Positives(1), Neutral(0), and Negatives(-1). 


### Model 

An RNN architecture was used to build a model to learn on. Lastly the model was fitted to the Test and Train Data Sets resulting in a final ~ 97% accuracy. 
