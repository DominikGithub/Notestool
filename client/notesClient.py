#! /usr/bin/env python

import os
import sys
import argparse
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("NotesCLI")
import requests
import json
import emoji
from dotenv import load_dotenv
load_dotenv()

# config
HOST_PORT = os.getenv("HOST_PORT")
URL = HOST_PORT + '/note'

# symbols
EMJ_LEMON = emoji.emojize(":lemon:")
EMJ_BANANA = emoji.emojize(":banana:")


def cmd_add(text):
	"""
	Add note.
	"""
	txt = ' '.join(text)
	print(f"{EMJ_LEMON} {txt} \033[2m >> saved \033[0m")
	r = requests.put(URL, json={"content": txt})


def cmd_ls():
	"""
	List notes.
	"""
	r = requests.get(URL)
	note_list = json.loads(r.content.decode("utf-8"))
	for idx, note in enumerate(note_list):
		#db_id = note['_id']
		txt = note['content']
		time = note['time']
		print(" {0:<2} {1:<2} \033[2m{2:<11}{3:<6}\033[0m {4:<}"\
			.format(EMJ_BANANA, idx, time[:10], time[11:16], txt))		#db_id,


def cmd_rm(idx):
	"""
	Remove note.
	"""
	# find note
	r = requests.get(URL)
	note_list = json.loads(r.content.decode('utf-8'))
	for pos, note in enumerate(note_list):
		if pos == idx:
			_id = note['_id']
			# delete note
			r = requests.delete(URL, json={'_id': _id})
			return
	print(f'Note {idx} not found')


def cli_args():
	"""
	Initialize cli arguments.
	"""
	parser = argparse.ArgumentParser(description='Maintain notes.')
	group_note = parser.add_mutually_exclusive_group()
	group_note.add_argument('-add', type=str, nargs='+', help='Add a note')
	group_note.add_argument('-ls',  action='store_true', help='Show notes')	# add optional param for number of first N notes to be shown
	group_note.add_argument('-rm',  type=str, 			 help='Delete note i')
	
	group_conf = parser.add_argument_group(title="Config")
	group_conf.add_argument('-c', action='store_true', help='Show configs')
	return parser


if __name__ == '__main__':
	cli_parser = cli_args()
	args = cli_parser.parse_args()

	if args.add:
		cmd_add(args.add)
	if args.rm:
		cmd_rm(int(args.rm))
	if args.ls:
		cmd_ls()
	if args.c:
		print(f"Endpoint: {URL}")
