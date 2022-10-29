FROM python:3.10


COPY requirements.txt .
RUN pip install -r requirements.txt
ENV FLASK_APP=run.py
ENV FLASK_ENV='development'
WORKDIR /code
COPY ./project ./project
COPY ./tests ./tests
COPY project.db .
COPY run.py .
COPY create_tables.py .
COPY load_fixtures.py .
CMD ['python', 'create_tables.py']
CMD ['python', 'load_fixtures.py']


CMD flask run -h 0.0.0.0 -p 80