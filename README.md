# Проектная работа 8 спринта

Инструкции по запуску находятся в директориях каждой части реализаций.

## Анализ хранилищ данных

[Результаты анализа.](benchmark/README.md)

Проведена работа по тестированию некоторых популярных баз данных на нагрузку с различными условиями, 
в ходе которых был выбран оптимальный для нас кандидат.

## API

[Инструкция по запуску](backend/README.md).

Написан API интерфейс для записи пользовательских действий в Kafka. 

## ETL

[Инструкция по запуску](etl/README.md).

Реализован механизм получения данных из Kafka в Clickhouse для последующего анализа.


## Юнит-тесты; TO BE, AS IS.

[Схема TO BE](docs/deployment_diagrams/to_be.png)
[Схема AS IS](docs/deployment_diagrams/as_is.png)

1) Подготовлены тесты на запись в API и последующей проверки отправленных значений в Kakfa.
2) Реализованы схемы текущего состояния и того, как мы видим дальнейшее развитие сервиса.

