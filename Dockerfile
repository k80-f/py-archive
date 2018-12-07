FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir waitress

COPY . /usr/src/app

CMD ["waitress-serve","main:app"]
