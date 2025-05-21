from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/index.html')
@app.route('/')
def index():
    card_data = (
        ("David", "We are all about teaching, and passing on our information to others so that people can create better videos, faster and at a low cost", "Find Out More", "static/images/card1"),
        ("David", "Boost your editing speed with simple techniques! Learn shortcuts, key tools, and smooth workflows to refine text and visuals efficiently. Let’s get started! ", "Find Out More", "static/images/card2"),
        ("David", "Enhance precision and speed! Master advanced shortcuts, refine techniques, and optimize workflows for faster, high-quality edits. Let’s go!", "Find Out More", "static/images/card3"),
        ("David", "Master expert techniques, optimize workflows, and edit with unmatched speed and precision. Take your skills to the highest level!", "Find Out More", "static/images/card4"),
        ("David", "Some Text", "Find Out More", "static/images/card5"),
        ("David", "Some Text", "Find Out More", "static/images/card6"),
    )
    return render_template("index.html"), 200


if __name__ == '__main__':
    app.run(debug=True)
