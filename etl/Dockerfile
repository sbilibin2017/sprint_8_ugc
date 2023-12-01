FROM python:3.11

WORKDIR /opt/app

ENV PYTHONPATH '/opt/app'

COPY pyproject.toml kafka_producer.py ./
RUN pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-dev

COPY bin bin
COPY libs libs

CMD ["python", "-m", "bin"]