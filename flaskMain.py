import start


from flask import Flask, render_template, request 


app = Flask(__name__)

score = 0;


@app.route('/entered')
def my_form():
    return render_template('my-form.html')

# @app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text.upper()
    return processed_text


@app.route('/googFinisher', methods = ['GET', 'POST'])
def reset():
    return ('googFinisher.html')
    

@app.route('/send', methods = ['GET', 'POST'])
def send():
    if request.method == "POST":
        age = request.form['age'];
    return ('googFinisher.html')

def index():
    render_template('playButton.html');
    return "hello"

def GetTheRightStuff():
    rWord = start.getRandomWord();
    allWords = start.getAllAutoFromRandomWord(rWord);
    allWords[0] = rWord;
    print(allWords);
    return allWords;

@app.route('/googFinisher')
def play():
    return render_template('googFinisher.html', words=GetTheRightStuff());


if __name__ == "__main__":
    app.run(debug=True);
