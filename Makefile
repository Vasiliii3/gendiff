install:
	poetry install

test:
	poetry run pytest -v

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

test-coverage2:
	poetry run pytest --cov=gendiff

selfcheck:
	poetry check

check: selfcheck test lint

build: check
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

package-install2:
	python -m pip install hexlet-code dist/hexlet_code-0.3.0-py3-none-any.whl
	# install specific version, sample 0.3.0

uninstall:
	pip uninstall hexlet-code -y

lint:
	poetry run flake8 gendiff

lint-test:
	poetry run flake8 tests

.PHONY: install test lint selfcheck check build

gendiff:
	poetry run gendiff -h

super:
	pip uninstall hexlet_code -y
	poetry build
	poetry publish --dry-run
	python -m pip install dist/*.whl
