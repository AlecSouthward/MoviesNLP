FROM pypy:latest
WORKDIR /MoviesNLP

COPY ./requirements.txt ./
COPY . .
RUN pip3 install -r requirements.txt

CMD python watch_next.py