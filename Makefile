lint:
	poetry run flake8 gendiff

install:
	poetry install

test-coverage:
	poetry run pytest--cov=gendiff --cov-report xml

test:
	poetry run pytest

selfcheck:
	poetry check

check: selfcheck test lint

