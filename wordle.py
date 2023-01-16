from flask import Flask, render_template, request, session
import nltk
import random
nltk.download("words")
from nltk.corpus import words

app = Flask(__name__)
app.secret_key = "mysecretkey"
word_list = words.words()
words_five = [word for word in word_list if len(word) ==5]

@app.route('/', methods=["GET", "POST"])
def wordle():
    if "word" not in session: 
        session["word"] = random.choice(words_five)
    if "attempt" not in session: 
        session["attempt"] = 0
    word = session["word"]
    attempt = session["attempt"]
    correct_letters = ''
    incorrect_letters = ''
    mispositioned = ''
    result = ''
    if request.method == 'POST':
        guess = request.form["guess"].lower()
        session["attempt"] +=1
        attempt = session["attempt"]
        if guess == word:
            result = "You Guessed The Word!"
            session.pop("word")
            session.pop("attempt")
        elif attempt == 6:
            result = "Sorry, you have reached the maximum number of attempts. The word was {}".format(word)
            session.pop("word")
            session.pop("attempt")
        else:
            for i in range(len(guess)):
                if guess[i] in word and guess[i] != word[i]:
                    mispositioned += guess[i]
                elif guess[i] == word[i]:
                    correct_letters += guess[i]
                else:
                    incorrect_letters += guess[i]
    return render_template("wordle.html", 
                           correct_letters=correct_letters, 
                           mispositioned=mispositioned, 
                           incorrect_letters=incorrect_letters, 
                           result=result)

if __name__ == '__main__':
    app.run(debug=True)
