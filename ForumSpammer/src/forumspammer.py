'''
Created on Aug 13, 2010

@author: lajosu
'''

import mechanize
import Config

br = mechanize.Browser()
br.set_proxies(Config.proxies)

br.open("http://hangmester.hu/newforum/bejelentkez.php")
br.select_form(nr=0)
br["usernev"] = Config.name
br["password"] = Config.password
br.submit()

br.open("http://hangmester.hu/newforum/listazas.php?topik=64&start=0")
br.select_form(name="kbmsg")
br["topi"] = "64"
br["rp"] = "" # used when this msg is a reply to another message
br["user"] = "laja"
br["msg"] = Config.message
br.submit()

print "done"
