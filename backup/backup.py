#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging

def createLogger(loggerName):
	logger = logging.getLogger(loggerName)
	logger.setLevel(logging.DEBUG)
	ch = logging.StreamHandler()
	ch.setLevel(logging.DEBUG)
	formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
	ch.setFormatter(formatter)
	logger.addHandler(ch)
	return logger

logger = createLogger('backup.py')

class Backup:
	def __init__(self):
		logger.info('A Backup object has been created.')

	def start(self):
		logger.info('a backup was started')

if __name__=='__main__':
	backup = Backup()
	backup.start()
