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
	
def test():
	logger = createLogger('logger.py')
	logger.info('A logger has been created for logger.py')
	
if __name__=='__main__':
	test()