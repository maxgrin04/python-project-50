<div align="center">
<h1>Вычислитель отличий / Diff calculator</h1>
</div>

### Python CI Badge:
[![Python CI](https://github.com/maxgrin04/python-project-50/actions/workflows/pyci.yml/badge.svg?branch=main)](https://github.com/maxgrin04/python-project-50/actions/workflows/pyci.yml)

### CodeClimate Badge:
[![Maintainability](https://api.codeclimate.com/v1/badges/e48b42d1d479d1e90b8e/maintainability)](https://codeclimate.com/github/maxgrin04/python-project-50/maintainability)

### Test Coverage Badge:
[![Test Coverage](https://api.codeclimate.com/v1/badges/e48b42d1d479d1e90b8e/test_coverage)](https://codeclimate.com/github/maxgrin04/python-project-50/test_coverage)

## Описание проекта

**«Вычислитель отличий»** — программа, которая определяет разницу между двумя структурами данных.

Возможности утилиты:

- Поддержка разных входных форматов: yaml, json
- Генерация отчета в виде plain text, stylish и json

## Требования:

- Python ^3.12
- uv ^0.5.21

## Инструкция по установке:

#### Python

> Перед установкой пакета убедитесь, что у вас установлен Python версии 3.12 или выше:

```bash
python --version
# Python 3.12.0+
```
#### UV

> Проект использует менеджер зависимостей uv. Для установки uv используйте инструкцию (https://github.com/Hexlet/ru-instructions/blob/main/uv.md).


### Установка пакета

> Чтобы использовать пакет, вам нужно скопировать репозиторий на свой компьютер. Это делается с помощью команды ``git clone``:

```bash
git clone https://github.com/maxgrin04/python-project-50
```

> Далее выполните установку пакета:

```bash
cd python-project-50
```

```bash
make build
make package-install
```


### Запуск тестов

```bash
make test
```

### Запуск проверки линтера

```bash
make lint
```


## Запуск программы

> Для программы игры используйте команду:
```bash
gendiff first_file second_file
```
где "first_file, second_file" - пути до файлов, которые сравнивает программа

> Пример запуска программы:
[![asciicast](https://asciinema.org/a/B3s2huMAgwxQWYBRer7ga58cs.svg)](https://asciinema.org/a/B3s2huMAgwxQWYBRer7ga58cs)


#### По умолчанию программа работает с форматтером "stylish"
##### Форматтер работает по флагу -f, --format (подробнее в справке -h, --help)

### Сравнение плоских файлов:

> Пример запуска программы с форматтером "stylish":
```bash
gendiff ./tests/test_data/file1.json ./tests/test_data/file2.json
```
```bash
gendiff -f stylish ./tests/test_data/file1.json ./tests/test_data/file2.json
```
```bash
gendiff ./tests/test_data/file1.yaml ./tests/test_data/file2.yaml
```
[![asciicast](https://asciinema.org/a/YsfVT9yYPd2zzV0dx2XFTbrJC.svg)](https://asciinema.org/a/YsfVT9yYPd2zzV0dx2XFTbrJC)

### Рекурсивное сравнение:

> Пример запуска рекурсивного сравнения:
```bash
gendiff ./tests/test_data/file3.json ./tests/test_data/file4.json
```
```bash
gendiff ./tests/test_data/file3.yaml ./tests/test_data/file4.yaml
```
[![asciicast](https://asciinema.org/a/H7MqX15Y1WF0rWsHjoEPcD2jp.svg)](https://asciinema.org/a/H7MqX15Y1WF0rWsHjoEPcD2jp)

#### Форматтер "plain"

> Пример запуска программы с форматтером "plain":
```bash
gendiff -f plain ./tests/test_data/file3.json ./tests/test_data/file4.json
```
```bash
gendiff -f plain ./tests/test_data/file3.yaml ./tests/test_data/file4.yaml
```
[![asciicast](https://asciinema.org/a/nmNTdgEvSytlmK7R1MQZOmpc3.svg)](https://asciinema.org/a/nmNTdgEvSytlmK7R1MQZOmpc3)

#### Форматтер "json"

> Пример запуска программы с форматтером "json":
```bash
gendiff -f json ./tests/test_data/file3.json ./tests/test_data/file4.json
```
```bash
gendiff -f json ./tests/test_data/file3.yaml ./tests/test_data/file4.yaml
```
[![asciicast](https://asciinema.org/a/pwuCiwfjbZMPdqoA24rIAeRZI.svg)](https://asciinema.org/a/pwuCiwfjbZMPdqoA24rIAeRZI)
