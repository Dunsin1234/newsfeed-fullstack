from flask import Flask,jsonify
import redis,os
app=Flask(__name__)
redis_client=redis.StrictRedis(host=os.getenv("REDIS_HOST","redis"),port=6379,decode_responses=True)
@app.route("/")
def home():
    return jsonify({"message":"Welcome to the NewsFeed API"})
@app.route("/news")
def get_news():
    cached=redis_client.get("news")
    if cached:
        return jsonify({"source":"cache","data":cached})
    news_data="Breaking: Redis caching in action 🚀"
    redis_client.set("news",news_data,ex=30)
    return jsonify({"source":"flask","data":news_data})
if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)
