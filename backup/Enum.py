#!/usr/bin/python
# -*- coding: utf-8 -*-

class Enum:
   def __init__(self, name):
       self.name = name

   def __str__(self):
       return self.name

   def __repr__(self):
       return "<%s: %s>" % (self.__class__.__name__, self)
