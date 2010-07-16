#!/usr/bin/python
# -*- coding: utf-8 -*-

import Logger
import Config
import OutputMethod

from ZipBackup import ZipBackup

logger = Logger.createLogger('backup.py')

if __name__=='__main__':
	if Config.OUTPUT_METHOD == OutputMethod.ZIP:
		ZipBackup().start()
	else:
		print "not supported OutputMethod"

