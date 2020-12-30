#! /bin/sh

#pipenv shell
source ./noteclienv/bin/activate &&
python notesClient.py $1 &&

exit