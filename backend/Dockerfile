FROM python:3.11

RUN apt-get update && apt-get install -y kafkacat

WORKDIR /opt/app

ENV PYTHONPATH '/opt/app'

COPY pyproject.toml ./
RUN pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-dev

COPY bin bin
COPY libs libs

CMD ["python", "-m", "bin"]
