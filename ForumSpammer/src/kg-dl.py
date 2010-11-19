import urllib2
import re

BASE = "http://www.kindgirls.com"
DEFAULT_FOLDER = "default"
TEST_LIST = [
	"http://www.kindgirls.com/gallery/hegre/anna_brigi_05573/anna-brigi/12/03-2010",
	"http://www.kindgirls.com/gallery/metart/tina_39034/tina/15/02-2010/",
	"http://www.kindgirls.com/gallery/hegre/muriel_64509/muriel/16/02-2010",
	"http://www.kindgirls.com/gallery/errotica/kami_45635/kami/12/05-2010/",
	"http://www.kindgirls.com/gallery/femjoy/angelina_37664/angelina-aka-indiana/12/01-2010",
	"http://www.kindgirls.com/gallery/javmodel/javmodels_04994/javmodels-mix/30/01-2010",
	"http://www.kindgirls.com/gallery/x-art/megan_09345/megan-aka-emma/12/12-2009",
	"http://www.kindgirls.com/gallery/x-art/georgia_francesca_83944/georgia-francesca/16/09-2009",
	"http://www.kindgirls.com/gallery/mcn/alida_melanie_38746/alida-melanie/12/04-2009",
	"http://www.kindgirls.com/gallery/javmodel/kirara_asuka_85474/kirara-asuka/12/04-2009",
	"http://www.kindgirls.com/gallery/photodromm/ariel_24532/ariel/12/02-2009",
	"http://www.kindgirls.com/gallery/metart/avia_29873/avia/16/02-2009",
	"http://www.kindgirls.com/gallery/ftv/franziska_04871/franziska-aka-francesca/16/12-2008",
	"http://www.kindgirls.com/gallery/femjoy/corinna_03983/corinna/12/12-2008/"
]

regexListing = re.compile("<div class=\"gallery_list\">.*<a href=\"([^\"]*)\" .*")
regexFolder = re.compile("http://www.kindgirls.com/gallery/[^/]*/([^/]*)/.*")
regexAlbum = re.compile("href=\"(/gallery/[^\"]*)\" >")

def download(url, folder = DEFAULT_FOLDER):
	print "# downloading url: " + url
	print "mkdir " + folder
	print "cd " + folder
	response = urllib2.urlopen(url)
	for line in response.readlines():
		result = regexListing.search(line)
		if result:
			out = "wget " + BASE + result.group(1)
			print out
	response.close()
	print "cd .."

def getListForTop100():
	urlTop100 = "http://www.kindgirls.com/top100"
	return createListUsingUrl(urlTop100)

def getListForArchive():
	url = "http://www.kindgirls.com/photo-archive/04-2010"
	return createListUsingUrl(url)

def createListUsingUrl(url):
	dl = []
	response = urllib2.urlopen(url)
	for line in response.readlines():
		result = regexAlbum.search(line)
		if result:
			dl.append(BASE + result.group(1))
	response.close()
	return dl

def getFolderFromUrl(url):
	result = regexFolder.search(url)
	if result:
		return result.group(1)
	return DEFAULT_FOLDER

def downloadList(DL = TEST_LIST):
	for item in DL:
		download(item, getFolderFromUrl(item))

if __name__=="__main__":
	downloadList(getListForArchive())
	print "# done"

