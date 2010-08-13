#!/usr/bin/python
# -*- coding: utf-8 -*-

from datetime import datetime
import hashlib, os

from encryption import AesEncryptor, EncryptionMethod
import Config

class Backup:
	def __init__(self):
		pass

	def start(self):
		singleFileName = self.createSingleFile()
		if Config.ENCRYPTION_METHOD != EncryptionMethod.NONE:
			self.encryptSingleFile(singleFileName)
			os.remove(singleFileName)

	def generateOutputFileName(self):
		d = datetime.now()
		return Config.OUTPUT_FOLDER + \
			Config.OUTPUT_FILE_PREFIX + \
			d.strftime(Config.OUTPUT_TIMESTAMP_FORMAT)
	
	def encryptSingleFile(self, singleFileName):
		key = self.retrieveKeyForEncryption()
		if Config.ENCRYPTION_METHOD == EncryptionMethod.AES:
			AesEncryptor.encrypt_file(key, singleFileName)
	
	def retrieveKeyForEncryption(self):
		f = open(Config.PASSWORD_FILE, 'r')
		password = f.readline()
		f.close
		key = hashlib.sha256(password).digest()
		return key
	