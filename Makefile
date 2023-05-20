pytest-coverage:
	pytest -vv --cov --cov-report=term-missing
pytest-collect:
	pytest --collect-only
mypy:
	mypy .
ruff:
	ruff check .
ruff-fix:
	ruff check --fix .
install-testing-req:
	pip3 install pytest pytest-cov
install-linting-req:
	pip3 install autopep8 mypy ruff
upgrade-pip:
	pip3 install --upgrade pip
venv-remove:
	rm -rf .venv
venv-activate:
	source .venv/bin/activate
venv-setup:
	python3 -m venv .venv
clean-package:
	rm -Rf ./build; rm -Rf ./dist; rm -Rf ./.eggs; rm -Rf ./*.egg-info; rm -Rf ./**/*.egg-info; rm -Rf ./.coverage; 
clean-pycache:
	rm -Rf ./.pytest_cache; rm -Rf ./**/__pycache__; rm -Rf ./**/**/__pycache__; rm -Rf ./**/**/**/__pycache__; rm -Rf ./**/**/**/**/__pycache__;rm -Rf ./**/**/**/**/**/__pycache__;rm -Rf ./**/**/**/**/**/**/__pycache__;
clean: clean-package clean-pycache