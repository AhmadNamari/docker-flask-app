from flask import Flask
import redis
import os

app = Flask(__name__)

redis_host = os.getenv("REDIS_HOST", "redis")
redis_port = int(os.getenv("REDIS_PORT", 6379))

cache = redis.Redis(host=redis_host, port=redis_port)

@app.route("/")
def home():
    count = cache.incr("visits")
    return f"Ahmad Alnamari DevOps Engineer - Visit Count: {count}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
