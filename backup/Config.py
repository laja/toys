#!/usr/bin/python
# -*- coding: utf-8 -*-

import OutputMethod, EncryptionMethod

INPUT_FILES = [
			"/home/lajosu/.bashrc",
			"/home/lajosu/.gitconfig",
			"/home/lajosu/.gtkrc-2.0-kde4",
			"/home/lajosu/.kderc",
			"/home/lajosu/.nvidia-settings-rc",
			"/home/lajosu/Programs/backup/Config.py"
]
INPUT_FOLDERS = [
			"/home/lajosu/bin", 
			"/home/lajosu/Documents/Personal/versek",
			"/home/lajosu/Documents/Personal/pictures"
]

OUTPUT_FOLDER = "/home/lajosu/ildiko/Groups/Development/Home/lajosu/saves/"
OUTPUT_FILE_PREFIX = "lajosu-office-backup-"
OUTPUT_TIMESTAMP_FORMAT = "%Y-%m-%d-%H-%M-%S"

OUTPUT_METHOD = OutputMethod.ZIP
ENCRYPTION_METHOD = EncryptionMethod.AES

PASSWORD_FILE = "/home/lajosu/.backup-key"

