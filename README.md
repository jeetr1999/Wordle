# Wordle
A flask based wordle game 🕹️that can be played on your web browser

## How to play?
- The game will choose a 5 letter word at random
- You will have 6 attempts to guess the word
- For every guess you will the game will tell you which letters from the input were correct, mispositioned, and incorrect letters
- If you fail to guess the word after 6 attempts, it will show the actual word.

## Install Required Libraries

#### macOS/Linux - 
1. Create an environment.
      Create a project folder and a venv folder within:
    ```
    $ mkdir myproject
    $ cd myproject
    $ python3 -m venv venv
     ```
2. Activate the environment
      Before you work on your project, activate the corresponding environment:
      ```
      $ . venv/bin/activate
      ```
3. Install Flask¶
      Within the activated environment, use the following command to install Flask:
      ```
      $ pip install Flask
      ```

## Windows
1. Create an environment.
      Create a project folder and a venv folder within:
    ```
    > mkdir myproject
    > cd myproject
    > py -3 -m venv venv
    ```
2. Activate the environment
      Before you work on your project, activate the corresponding environment:
      ```
      > venv\Scripts\activate
      ```
3. Install Flask¶
      Within the activated environment, use the following command to install Flask:
      ```
      $ pip install Flask
      ```


## How to run?
- Clone the library by terminal using
  ```
  $ git clone git@github.com:strawberrylightningbolt/Wordle.git
  ```
- Make sure the python file and the template folder are in the same directory
- To run the python file, use the following command in terminal
  ```
  python wordle.py
  ```
- You will receive a message in the terminal that looks something like this
  ```
  Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
  ```
- To play the game, simply search for `http://127.0.0.1:5000` on your web browser
