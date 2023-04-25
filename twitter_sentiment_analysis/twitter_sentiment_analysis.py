# Analyze tweets about a certain topic with pandas, textblob and seaborn

import json
from textblob import TextBlob
with open ("data.json", "r") as fh:
    twitter_data = json.load(fh)
    obama_tweets = []
    for i in twitter_data:
        if "obama" in i["topic"]:
            obama_tweets.append(i)

for i in obama_tweets:
    sentiment = TextBlob(i["tweet"])
    i["sentiment"] = sentiment.sentiment.polarity
    if i["sentiment"] < -0.2:
        i["sentiment"] = "negative"
    elif i["sentiment"] > 0.2:
        i["sentiment"] = "positive"
    else:
        i["sentiment"] = "neutral"

with open ("sentiment_obama.json", "w") as fh:
    json.dump(obama_tweets, fh, indent=4)
    
import pandas as pd
obama_df = pd.read_json("sentiment_obama.json")
obama_sentiment_count = obama_df["sentiment"].value_counts()
obama_tweets = pd.DataFrame(obama_sentiment_count)


import seaborn as sns
sns.set_theme()
obama_plot = sns.barplot(data = obama_tweets, x = "sentiment" , y = obama_tweets.index)
obama_plot.get_figure().savefig("obama_tweets.png", bbox_inches = 'tight')