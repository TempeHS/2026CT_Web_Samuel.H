from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html"), 200

@app.route('/page2')
def page2():
    return render_template("page2.html"), 200

if __name__ == '__main__':
    app.run(debug=True)
