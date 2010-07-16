#!/usr/bin/python
# -*- coding: utf-8 -*-

import OutputMethod, EncryptionMethod

INPUT_FILES = ["/home/lajosu/Documents/trash.png", "/home/lajosu/Documents/Personal/vers.txt"]
INPUT_FOLDERS = ["/home/lajosu/bin", "/home/lajosu/Downloads"]

OUTPUT_FOLDER = "/home/lajosu/saves/"
OUTPUT_FILE_PREFIX = "laja-office-backup-"
OUTPUT_TIMESTAMP_FORMAT = "%Y-%m-%d-%H-%M-%S"

OUTPUT_METHOD = OutputMethod.ZIP
ENCRYPTION_METHOD = EncryptionMethod.NONE

