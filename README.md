### Линтеры

[![test lint](https://github.com/Vasiliii3/gendiff/actions/workflows/lint.yml/badge.svg)](https://github.com/Vasiliii3/gendiff/actions/workflows/lint.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/3e6d6cd7cbd233354e58/maintainability)](https://codeclimate.com/github/Vasiliii3/gendiff/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/3e6d6cd7cbd233354e58/test_coverage)](https://codeclimate.com/github/Vasiliii3/gendiff/test_coverage)

### Описание
Вычислитель отличий – программа, которая определяет разницу между двумя структурами данных. Это популярная задача, для решения которой существует множество онлайн-сервисов, например, jsondiff.  
Подобный механизм, например, используется при выводе тестов или при автоматическом отслеживании изменений в конфигурационных файлах.

##### Возможности утилиты:

* Поддержка разных входных форматов: yaml, json
* Генерация отчета в виде plain text, stylish и json

### Установка
* Используйте диспетчер пакетов pip:

`pip install --user git+https://github.com/Vasiliii3/gendiff`

или

* Клонируйте репозиторий и используйте poetry:
1. `git clone https://github.com/Vasiliii3/gendiff`
2. `cd brain_games`
3. `make install`
4. Для сборки пакета `make build`
5. Для установки пакета `make package-install`
6. Для удаление пакета `make uninstall`

### Требования
* Python 3.9 и выше
* Poetry 1.7 и выше


### Использования

`usage: gendiff [-h] [-f [type]] [--v] first_file second_file`

Для помощи

`gendiff -h`

Вы можете задать формат вывода: `stylish` (по умолчанию), `plain`, `json`. Для этого укажите параметр `-f`, например`gendiff -f plain filepath1 filepath2`

### Примеры работы различных форматов

##### Stylish format
json and json (pain)
[![asciicast](https://asciinema.org/a/DYyVw36GHzH959H9DSQvgmQYD.svg)](https://asciinema.org/a/DYyVw36GHzH959H9DSQvgmQYD)
yml and yml(pain)
[![asciicast](https://asciinema.org/a/DjkndiFbMdhlMbgrpTASrjwjR.svg)](https://asciinema.org/a/DjkndiFbMdhlMbgrpTASrjwjR)
json and json (tree)
[![asciicast](https://asciinema.org/a/hgjUuMl5ykZ9rlnvaiyWY3eyA.svg)](https://asciinema.org/a/hgjUuMl5ykZ9rlnvaiyWY3eyA)

yml and yml(tree) works similarly

##### Plain format
пример вызова  

`gendiff -f plain tests/fixtures/file3.json tests/fixtures/file4.json`

[![asciicast](https://asciinema.org/a/NWAH5oz2x1d0P9pBlDscowcc9.svg)](https://asciinema.org/a/NWAH5oz2x1d0P9pBlDscowcc9)

##### Json format
пример вызова  

`gendiff -f json tests/fixtures/file3.json tests/fixtures/file4.json`

[![asciicast](https://asciinema.org/a/dEvCzFlrogSe8E7a5hbR0FRae.svg)](https://asciinema.org/a/dEvCzFlrogSe8E7a5hbR0FRae)