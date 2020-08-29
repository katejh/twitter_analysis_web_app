# Twitter Sentiment Analysis app
A simple web application made in Python and Flask.
Utilizes the Tweepy API and the TextBlob API to perform sentiment analysis on Tweets on Twitter

## Setup
To run this project, clone this repository onto your computer. You can use the code below:
```
$ mkdir ~/{REPO_NAME}
$ cd ~/{REPO_NAME}
$ git clone https://github.com/katejh/twitter_analysis_web_app
```

Make sure you have Flask installed. If Flask is not installed, run `sudo apt install python3-flask`

Make sure you have Tweepy installed. If Tweepy is not installed, run `pip install tweepy`

Make sure you have TextBlob installed. To install TextBlob, run `pip install textblob`

Register for a [Twitter Developer account](https://developer.twitter.com/en). Then create for a new app. In your Twitter
apps page, go to your new app and see "Keys and tokens". Generate your API keys and authentication tokens.
Then, cd into src/creds and create a new file named `credentials.json`. 
```
$ cd ~/{REPO_NAME}/src/creds
$ touch credentials.json 
```
Copy and paste the following code into `credentials.json`.
```javascript
{
    "API-key": "YOUR-API-KEY-HERE",
    "API-secret-key": "YOUR-API-TOKEN-HERE",
    "bearer-token": "YOUR-BEARER-TOKEN-HERE",
    "access-token": "YOUR-ACCESS-TOKEN-HERE",
    "access-token-secret": "YOUR-ACCESS-SECRET-TOKEN-HERE"
}
```
Replace the appropriate locations with the keys and tokens you generated.

Then, in the root directory of this project, run `flask run`
```
$ cd ~/{REPO_NAME}
$ flask run
```

## Features
* Enter a topic of your choosing and receive a select number of the most recent tweets within that topic and a measure of its positivity

### Todos
* Make it prettier
* Display tweets and sentiments in a more ordered and intuitive fashion e.g. a graph
* Explain topic request form more - explain how to structure a search query and also why user is requested to enter their number of tweets
* Instead of simply displaying the sentiment measurement, display it as "positive" or "negative" or maybe implement some sort of graphic
