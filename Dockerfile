FROM python:3.14-slim

WORKDIR /app
COPY ./main.py main.py
COPY ./settings.json settings.json
COPY ./word_frequency.json word_frequency.json
COPY ./words.txt words.txt
COPY ./words_i_like.txt words_i_like.txt

CMD [ "python", "main.py" ]
