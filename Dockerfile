FROM python:3.7

RUN apt-get update 

COPY . /usr/src/app

WORKDIR /usr/src/app
RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

EXPOSE 8082
CMD python main.py