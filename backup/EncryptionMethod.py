#!/usr/bin/python
# -*- coding: utf-8 -*-

from Enum import Enum

class EncryptionMethod(Enum):
	pass

NONE = EncryptionMethod("NONE")
TWOFISH = EncryptionMethod("TWOFISH")
