FROM python:alpine3.7
COPY . /app
WORKDIR /app
RUN pip install redis
RUN pip install rq
EXPOSE 5000
CMD python ./worker.py