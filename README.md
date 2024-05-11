# Repositories API

## Overview

A simple FastAPI service built on top of the [GitHub API](https://docs.github.com/en/rest?apiVersion=2022-11-28) service that
returns the top repositories sorted by stars.

## Project Dependencies

These are some of the project's main dependencies. For a full list of dependencies refer to [pyproject.toml](./pyproject.toml).

Production:

- [fastapi](https://fastapi.tiangolo.com/): A back-end framework.
- [gidgethub](https://gidgethub.readthedocs.io/en/latest/): An async GitHub API client.
- [cachetools](https://cachetools.readthedocs.io/en/latest/): A GitHub API client's cache.
- [uvicorn](https://www.uvicorn.org/): An ASGI web server.

Development:

- [pytest](https://docs.pytest.org/en/8.2.x/): A test framework.
- [vcrpy](https://vcrpy.readthedocs.io/en/latest/): A mocker that records and mocks actual GitHub API requests.
- [honcho](https://honcho.readthedocs.io/en/latest/): An application manager.

## Development

### Create a Virtual Environment

For convenience, we will create an specific virtual environment for development:

```bash
python -m venv venv
source venv/bin/activate
```

### Install the Dependencies

```bash
poetry config virtualenvs.in-project true
poetry install
```

This will install the dependencies in our development virtual environment rather than globally.

### Run Tests

```bash
pytest -s -vvv
```

You may also use honcho:

```bash
honcho start tests
```

It's possible to generate coverage reports:

```bash
pytest --cov=. --cov-report html
```

![Web Browser View of the Coverage Reports](./docs/images/coverage-reports-1.png)

You may also use honcho:

```bash
honcho start coverage
```


### Run in Development Mode

This application requires a GitHub API access token. Once you obtain your token, export the following variable with your own:

```bash
export GITHUB_API_ACCESS_TOKEN="YOUR ACCESS TOKEN"
```

Now you can start the service in development mode:

```bash
honcho start runserver
```

The service should be available [here](http://127.0.0.1:8000/):

![Web Browser View of the OpenAPI Page](./docs/images/openapi-view-1.png)

### Hints

This project uses honcho to manage tasks. The following tasks are available:

| Task                         | Purpose                                                                                      |
|:-----------------------------|:---------------------------------------------------------------------------------------------|
| `honcho start service`       | Used to start the service with ASGI server.                                                  |
| `honcho start runserver`     | Used to start the service in development mode.                                               |
| `honcho start tests`         | Run tests.                                                                                   |
| `honcho start format`        | Formats code and organize imports using black and isort.                                     |
| `honcho start format_check`  | Only checks formatting (meant to be used in CI).                                             |
| `honcho start pylint_check`  | PyLint (configuration [here](./.pylintrc)) checks.                                           |
| `honcho start mypy_check`    | MyPy (configuration [here](./mypy.ini)) checks.                                              |
| `honcho start quality_check` | PyLint & MyPy checks.                                                                        |
| `honcho start coverage`      | Generate test coverage reports. They should be available [here](./htmlcov/index.html).       |

## Production

There's a [Dockerfile](./Dockerfile) ready for deployment. All that is needed is providing the proper
configuration through environment variables. This image could be pushed to an image registry and then deployed
to a Kubernetes cluster for instance.

You may also run the service using docker:

```
docker build -t repositories-api .
docker run -d -p 8000:8000 -e GITHUB_API_ACCESS_TOKEN="YOUR ACCESS TOKEN"... repositories-api
```

Note that you will need to configure the application through environment variables, in this case passing command-line arguments.