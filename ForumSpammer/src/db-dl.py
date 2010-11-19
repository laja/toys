import mechanize
import re

BASE = "http://dailybeachgirls.com/"
PROXIES = {"http" : "http://proxy:8080"}

br = mechanize.Browser()
br.set_proxies(PROXIES)

regex = re.compile("<td[^<]*<img.*src=\"(.*)\"")

def download(url):
	response = br.open(url)
	for line in response.readlines():
		result = regex.search(line)
		if result:
			out = "wget " + BASE + result.group(1)
			print out

def downloadList():
	DL = [
			"http://dailybeachgirls.com/kazantip-nude-beach-gallery14.html",
			"http://dailybeachgirls.com/kazantip-nude-beach-gallery13.html",
			"http://dailybeachgirls.com/romania-nude-beaches-gallery6.html",
			"http://dailybeachgirls.com/nude-on-yachts-gallery2.html",
			"http://dailybeachgirls.com/nude-on-yachts-gallery1.html",
			"http://dailybeachgirls.com/romania-nude-beaches-gallery5.html",
			"http://dailybeachgirls.com/kazantip-nude-beach-gallery12.html",
			"http://dailybeachgirls.com/kazantip-nude-beach-gallery11.html",
			"http://dailybeachgirls.com/romania-nude-beaches-gallery4.html",
			"http://dailybeachgirls.com/busty-girls-topless-on-beach2.html",
			"http://dailybeachgirls.com/kazantip-nude-beach-gallery10.html",
			"http://dailybeachgirls.com/hydropark-naked-beach-gallery7.html",
			"http://dailybeachgirls.com/busty-girls-topless-on-beach.html",
			"http://dailybeachgirls.com/busty-girls-topless-on-beach.html",
			"http://dailybeachgirls.com/kazantip-nude-beach-gallery9.html",
			"http://dailybeachgirls.com/bulgaria-topless-beaches-gallery1.html",
			"http://dailybeachgirls.com/greece-topless-beaches-gallery2.html",
			"http://dailybeachgirls.com/greece-topless-beaches-gallery1.html",
			"http://dailybeachgirls.com/kazantip-nude-beach-gallery8.html",
			"http://dailybeachgirls.com/hainan-beach-topless-russian-women.html",
			"http://dailybeachgirls.com/dominican-adult-resort-gallery1.html",
			"http://dailybeachgirls.com/hedonism-jamaica-pics-gallery2.html",
			"http://dailybeachgirls.com/hedonism-jamaica-pics-gallery1.html",
			"http://dailybeachgirls.com/stmaarten-topless-beaches-pics-gallery1.html",
			"http://dailybeachgirls.com/hydropark-naked-beach-gallery6.html",
			"http://dailybeachgirls.com/hydropark-naked-beach-gallery5.html",
			"http://dailybeachgirls.com/naked-beaches-of-croatia-gallery12.html",
			"http://dailybeachgirls.com/naked-beaches-of-croatia-gallery11.html",
			"http://dailybeachgirls.com/naked-beaches-of-croatia-gallery10.html",
			"http://dailybeachgirls.com/naked-beaches-of-croatia-gallery9.html",
			"http://dailybeachgirls.com/naked-beaches-of-croatia-gallery8.html",
			"http://dailybeachgirls.com/ibiza-topless-beaches-gallery5.html",
			"http://dailybeachgirls.com/ibiza-topless-beaches-gallery4.html",
			"http://dailybeachgirls.com/ibiza-topless-beaches-gallery3.html",
			"http://dailybeachgirls.com/hydropark-naked-beach-gallery4.html",
			"http://dailybeachgirls.com/kazantip-nude-beach-gallery7.html",
			"http://dailybeachgirls.com/kazantip-nude-beach-gallery6.html",
			"http://dailybeachgirls.com/kazantip-nude-beacah-gallery5.html",
			"http://dailybeachgirls.com/kazantip-nude-beacah-gallery4.html"]

	for item in DL:
		download(item)

def downloadByNumber():
	for i in range(1,2):
		url = BASE + str(i) + ".html"
		download(url)

if __name__=="__main__":
	downloadByNumber()
	print 'done'
