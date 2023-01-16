"""
Import the required libraies - 
1. flask 
2. nltk - to get the nltk word corpus
3. Random - to randomize word choice
"""

from flask import Flask, render_template, request, session
import nltk
import random
nltk.download("words")
from nltk.corpus import words

app = Flask(__name__)
app.secret_key = "mysecretkey"
word_list = words.words()
# choose 5 letter words from the word list downloaded from nltk
words_five = [word for word in word_list if len(word) ==5]

@app.route('/', methods=["GET", "POST"])
def wordle():
    
    # check if it is a new session
    # if not, set set the word to be guessed and set attempt to 0
    if "word" not in session: 
        session["word"] = random.choice(words_five)
    if "attempt" not in session: 
        session["attempt"] = 0

    # initialize required variables

    word = session["word"] # the word to be guessed
    attempt = session["attempt"] # the number of attempts
    correct_letters = '' # string to store correct letters
    incorrect_letters = '' # string to store incorrect letters
    mispositioned = '' # string to store mispositioned letters
    result = '' # string to store the results of the game

    if request.method == 'POST':

        # get the user input and store it in a variable called guess
        # and increment attempt by 
        guess = request.form["guess"].lower()
        session["attempt"] +=1
        attempt = session["attempt"]

        # if the user guessed the word correctly, end the game

        if guess == word:
            result = "You Guessed The Word!"
            session.pop("word")
            session.pop("attempt")

        # if the attempt is 6, end the game and show the results

        elif attempt == 6:
            result = "Sorry, you have reached the maximum number of attempts. The word was {}".format(word)
            session.pop("word")
            session.pop("attempt")
        
        # if attempt is not 6, and user didn't guess the word - 
        # run a loop for iterations = lenght of guess (5, set in the html file)

        else:
            for i in range(len(guess)):

                # check if the letter from user input is present in the word
                # and not at the position

                if guess[i] in word and guess[i] != word[i]:
                    mispositioned = mispositioned + guess[i] + ' '
                
                # check if the letter position of input and the word are same
                elif guess[i] == word[i]:
                    correct_letters = correct_letters +  guess[i] + ' '

                # if none of the above conditions satisfy
                # the letter is incorrect
                else:
                    incorrect_letters = incorrect_letters + guess[i] + ' '

    return render_template("wordle.html", 
                           correct_letters=correct_letters, 
                           mispositioned=mispositioned, 
                           incorrect_letters=incorrect_letters, 
                           result=result)

if __name__ == '__main__':
    app.run(debug=True)
