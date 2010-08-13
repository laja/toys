#!/usr/bin/python
# -*- coding: utf-8 -*-

from Enum import Enum

class OutputMethod(Enum):
	pass

ZIP = OutputMethod("ZIP")
TAR = OutputMethod("TAR")
TARGZ = OutputMethod("TARGZ")
TARBZ2 = OutputMethod("TARBZ2")

