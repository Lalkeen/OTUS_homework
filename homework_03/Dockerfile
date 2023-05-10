# docker run -p 8000:8000 -it app
FROM python:3.9-buster

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install "poetry==1.4.2"
RUN poetry config virtualenvs.create false --local
COPY poetry.lock pyproject.toml ./
RUN poetry install --no-ansi --only main

COPY main.py views.py ./

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
EXPOSE 8000
