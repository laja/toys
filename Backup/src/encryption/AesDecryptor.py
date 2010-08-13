#!/usr/bin/python
# -*- coding: utf-8 -*-

# http://eli.thegreenplace.net/2010/06/25/aes-encryption-of-files-in-python-with-pycrypto/

import os, struct, sys
from Crypto.Cipher import AES

import Logger, Backup

logger = Logger.createLogger('AesDecryptor.py')

def decrypt_file(key, in_filename, out_filename=None, chunksize=24*1024):
	""" Decrypts a file using AES (CBC mode) with the
		given key. Parameters are similar to encrypt_file,
		with one difference: out_filename, if not supplied
		will be in_filename without its last extension
		(i.e. if in_filename is 'aaa.zip.enc' then
		out_filename will be 'aaa.zip')
	"""
	logger.info("Encryption has started.")
	if not out_filename:
		out_filename = os.path.splitext(in_filename)[0]

	with open(in_filename, 'rb') as infile:
		origsize = struct.unpack('<Q', infile.read(struct.calcsize('Q')))[0]
		iv = infile.read(16)
		decryptor = AES.new(key, AES.MODE_CBC, iv)

		with open(out_filename, 'wb') as outfile:
			while True:
				chunk = infile.read(chunksize)
				if len(chunk) == 0:
					break
				outfile.write(decryptor.decrypt(chunk))

			outfile.truncate(origsize)
	logger.info("Decryption is done.")

if __name__=='__main__':
	key = Backup.Backup().retrieveKeyForEncryption()
	fileName = sys.argv[1]
	decrypt_file(key, fileName)

