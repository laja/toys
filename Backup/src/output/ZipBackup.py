#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, zipfile, glob

from Backup import Backup
import Logger, Config

logger = Logger.createLogger('ZipBackup.py')

class ZipBackup(Backup):
	
	def createSingleFile(self):
		logger.info("ZipBackup started")
		
		zipFileName = self.generateOutputFileName() + ".zip"
		
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
		return zipFileName
		
	def addFolderToZip(self, zipFile, folderName):
		for fileName in glob.glob(folderName+"/*"):
			if os.path.isfile(fileName):
				zipFile.write(fileName)
			elif os.path.isdir(fileName):
				# recursion, we don't support that
				pass
				
