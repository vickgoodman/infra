# Default target: install and run tests.
all: install test

# Install tool:
install:
	pip3 install -r requirements.txt

install-dev:
	pip3 install -r requirements-dev.txt

# Run tests:
test:
	python3 -m pytest tests/ -v
