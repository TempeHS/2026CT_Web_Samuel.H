from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/index.html')
@app.route('/')
def index():
    card_data = (
        ("", "We are all about teaching, and passing on our information to others so that people can create better videos, faster and at a low costㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ", "Find Out More", "static/images/card1.png"),
        ("", "Boost your editing speed with simple techniques! Learn shortcuts, key tools, and smooth workflows to refine text and visuals efficiently. Let’s get started!ㅤㅤㅤㅤㅤㅤ", "Find Out More", "static/images/card2.png"),
        ("", "Enhance precision and speed! Master advanced shortcuts, refine techniques, and optimize workflows for faster, high-quality edits. Let’s go!ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ", "Find Out More", "static/images/card3.png"),
        ("", "Master expert techniques, optimize workflows, and edit with unmatched speed and precision. Take your skills to the highest level!ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ", "Find Out More", "static/images/card4.png"),
        ("", "Video editing is about refining footage efficiently, using smart techniques to speed up trimming, transitions, and enhancements—maximizing quality while saving time.", "Find Out More", "static/images/card5.png"),
        ("", "Our Goal is to optimize editing speeds to save time while keeping quality high—smart techniques make the process faster and more efficient.ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ", "Find Out More", "static/images/card6.png"),
    )
    return render_template("index.html", cards=card_data), 200


@app.route('/contact.html')
def contact():
    return render_template("contact.html"), 200

@app.route('/faq.html')
def faq():
    return render_template("faq.html"), 200

@app.route('/signup.html')
def signup():
    return render_template("signup.html"), 200

if __name__ == '__main__':
    app.run(debug=True)
