#! /usr/bin/env python

import sys
import requests
import json
import emoji

URL = 'http://localhost:3000/note'

def cmd_add(text):
	'''
	Add note.
	'''
	r = requests.put(URL, json={"content": text})

def cmd_ls():
	'''
	List notes.
	'''
	r = requests.get(URL)
	note_list = json.loads(r.content.decode("utf-8"))
	for idx, note in enumerate(note_list):
		txt = note['content']
		time = note['time']
		print(' {0:<2} {1:<2} {2:<11}{3:<6} | {4:<}'\
				.format(emoji.emojize(":banana:"), idx, time[:10], time[11:16], txt))

def cmd_rm(idx):
	'''
	Remove note.
	'''
	# find note
	r = requests.get(URL)
	note_list = json.loads(r.content.decode('utf-8'))
	if idx > len(note_list): raise Exception('Error 1: {} not found'.format(idx))
	for pos, note in enumerate(note_list):
		if pos == idx:
			_id = note['_id']
			# delete note
			r = requests.delete(URL, json={'_id': _id})
			return
		raise Exception('Error: {} not found'.format(idx))
	
def cmd_help():
	'''
	Show help.
	'''
	print('usage: note [cmd]\r\n')
	print('  add - New note')
	print('  ls  - List notes')
	print('  rm  - Delete note')

if __name__ == '__main__':
	if len(sys.argv) == 2:
		if 	 sys.argv[1] == '--help': 	cmd_help()
		elif sys.argv[1] == 'ls':		cmd_ls()
		exit(0)
	elif len(sys.argv) > 2:
		cmd = sys.argv[1]
		if cmd == 'rm':
			idx = sys.argv[2]
			print('rm at index: ', idx)
			try:
				cmd_rm(int(idx))
			except Exception as ex:
				print(ex)
			finally:
				exit(0)
		elif cmd == 'add':
			text_start = 2
			text_input = ' '.join(sys.argv[text_start:])
			print(emoji.emojize(":lemon:") + ' | ' + text_input)
			#cmd_add(text_input)
			exit(0)
		else:
			print('Unknown command:', cmd)
	else:
		print("stange.....")
