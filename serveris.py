from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return "Labrīt!"
@app.route('/sveiki')
def index():
  return('Nav rīts!')

if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)
