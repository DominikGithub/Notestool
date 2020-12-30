venv: requirements.txt
	virtualenv noteclienv -p 3.7
	source ./noteclienv/bin/activate
	pip install -r requirements.txt

build: venv
	python notesclient.py -h