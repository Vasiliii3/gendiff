install:
	poetry install

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=hexlet_python_package --cov-report xml

selfcheck:
	poetry check

check: selfcheck test lint

build: check
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

uninstall:
	pip uninstall hexlet_code -y

lint:
	poetry run flake8 brain_games

.PHONY: install test lint selfcheck check build

gendiff:
	poetry run gendiff -h

super:
	pip uninstall hexlet_code -y
	poetry build
	poetry publish --dry-run
	python -m pip install dist/*.whl