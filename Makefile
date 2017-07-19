help:
	@echo 'Makefile for python-search-engine                                     '
	@echo '                                                                      '
	@echo 'Usage:                                                                '
	@echo '   install                             Install all dependencies to run'
	@echo '   setup                               Install all dependencies to dev'
	@echo '   test                                Run project tests              '

install:
	@pip install -r requirements.txt

setup:
	@pip install -r requirements_dev.txt

test:
	@py.test tests --cov-report term-missing --cov-report xml --cov=py_search_engine --pep8 --flakes

.PHONY: help, install, setup, test
