FROM tiangolo/uwsgi-nginx-flask:python3.11

RUN pip install --upgrade pip

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . /app
