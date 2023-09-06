from flask import Flask, render_template, request


app = Flask(__name__)
app.secret_key = 'some_secret_key'

@app.route('/', methods=['GET', 'POST'])
def index():
    message = None
    if request.method == 'POST':
        comment = request.form.get('comment')
        if contains_swearword(comment):
            message = "Your comment contains inappropriate language!"
    return render_template('index.html', message=message)


def contains_swearword(text):
    swearwords = {"rude", "dirty"} 
    text = text.lower()
    return any(word in text.split() for word in swearwords)


if __name__ == "__main__":
    app.run(debug=True)
