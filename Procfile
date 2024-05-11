service: uvicorn app.main:app --host 0.0.0.0 --port 8888
tests: pytest -s -vv
runserver: uvicorn app.main:app --reload
format: black . && isort .
format_check: black --check . && isort --check-only .
pylint_check: python -m pylint app tests
mypy_check: python -m mypy app tests
quality_check: python -m pylint app tests && python -m mypy .
coverage: pytest --cov=. --cov-report html