SHELL=bash

.PHONY: test
test:
	PYTHONPATH=$PYTHONPATH:./ python2.7 ./tests/test_flatten.py

.PHONY: lint
lint:
	pep8 flatten_json/
	pylint --rcfile=.pylintrc flatten_json/

.PHONY: clean
clean:
	find . -name \*.pyc -delete

.PHONY: requirements
requirements:
	pip install -r requirements.txt
