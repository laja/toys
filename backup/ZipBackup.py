#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, zipfile, glob

from datetime import datetime
import time

import Logger
import Config

logger = Logger.createLogger('ZipBackup.py')

class ZipBackup:
	def __init__(self):
		pass
	
	def start(self):
		logger.info("ZipBackup started")
		d = datetime.now()
		
		zipFileName = Config.OUTPUT_FOLDER + \
			Config.OUTPUT_FILE_PREFIX + \
			d.strftime(Config.OUTPUT_TIMESTAMP_FORMAT) + \
			".zip"
		
		zipFile = zipfile.ZipFile(zipFileName, "w")
		
		for fileName in Config.INPUT_FILES:
			if os.path.isfile(fileName):
				zipFile.write(fileName)
				logger.info("adding file %s to the archive" % fileName)
			
		for folderName in Config.INPUT_FOLDERS:
			self.addFolderToZip(zipFile, folderName)
			logger.info("adding folder %s to the archive" % folderName)
			
		zipFile.close()
		logger.info("zipfile %s is ready." % zipFileName)
		
	def addFolderToZip(self, zipFile, folderName):
		for fileName in glob.glob(folderName+"/*"):
			if os.path.isfile(fileName):
				zipFile.write(fileName)
			elif os.path.isdir(fileName):
				# recursion, we don't support that
				pass
