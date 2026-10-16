PYTHON = python
PIP = pip

all: install test run

install:
	$(PIP) install -r requirements.txt

run:
	$(PYTHON) main.py


test:
	$(PYTHON) -m pytest tests/

coverage:
	$(PYTHON) -m pytest --cov=. --cov-report=term-missing tests/

clean:
	python -c "import shutil, glob, os; [shutil.rmtree(p, ignore_errors=True) for p in glob.glob('**/__pycache__', recursive=True) + ['.pytest_cache', 'htmlcov']]; [os.remove(f) for f in ['.coverage'] if os.path.exists(f)]"

.PHONY: all install run test coverage clean
