FROM python:3.9

ADD wordle.py .

RUN pip install flask nltk

CMD ["python", "./wordle.py"]