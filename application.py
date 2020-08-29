from flask import Flask, render_template, request
from src.sentiment_analysis import TwitterClient

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/topic", methods=["POST"])
def get_query():
    if request.method == "POST":
        search_query = request.form.get("search_query")
        count = int(request.form.get("count"))
    
    client = TwitterClient()
    tweet_sentiments = client.get_tweets(search_query, count = count)

    return render_template("tweets.html", tweet_sentiments=tweet_sentiments)