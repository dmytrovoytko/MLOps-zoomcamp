# FROM python:3.10.13-slim

# WORKDIR /app
# COPY [ "model2.bin", "model.bin" ]

FROM agrigorev/zoomcamp-model:mlops-2024-3.10.13-slim

RUN pip install -U pip
RUN pip install pipenv 

WORKDIR /app

COPY [ "Pipfile", "Pipfile.lock", "./" ]

RUN pipenv install --system --deploy

COPY [ "predict.py", "./" ]

ENTRYPOINT [ "python3", "predict.py"]

# EXPOSE 9696

# ENTRYPOINT [ "gunicorn", "--bind=0.0.0.0:9696", "predict:app" ]