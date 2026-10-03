from flask import Flask 
import redis 

app = Flask(__name__)

r = redis.Redis(host='redis', port=6379, decode_responses=True)

@app.route("/")
def hello_world():
    return "Hello, world"

@app.route('/count')
def visit():
    updated_count = r.incr('vistor_count')
    return f"you are vistor number: {updated_count}"
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

