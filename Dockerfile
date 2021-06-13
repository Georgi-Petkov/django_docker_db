FROM python:3.6

WORKDIR /random_quote

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "random_quote/manage.py", "runserver", "0.0.0.0:8000"]