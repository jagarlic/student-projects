from bs4 import BeautifulSoup
from nltk.corpus import wordnet
import urllib2
import re

satisfiablePercent = .8
start = "caddy"
goalString = "Shack"
goal = wordnet.synset("Shack.n.01")

def nextPage(link, visited):
	wiki = "https://en.wikipedia.org/wiki/"
	wiki += link
	website = urllib2.urlopen(wiki)
	html = website.read()
	soup = BeautifulSoup(html, "html.parser")
	links = soup.findAll('a', href=True)
	currentBest = ["", 0]
	for link in links:
		link = link['href']
		if (link[:5] == "/wiki" and link[:-3] != ("JPG" or "jpg" or "png") and (link[5:14] != "/Category")
		and link[6:16] != "Wikipedia:" and link[6:14] != "Special:" and link[6:10] != "File" and
		link[6:13] != "Portal:" and link[6:15] != "Main_Page" and link[6:10] != "Help"):
			link = link[6:]
			if link == goalString:
				return link
			if wordnet.synsets(link):
				if link not in visited:
					w1 = wordnet.synsets(link)[0]
					score = w1.wup_similarity(goal)
					if score >= satisfiablePercent:
						return link
					elif score >= currentBest[1]:
						currentBest[0] = link
						currentBest[1] = score
	return currentBest[0]

def greedy(nextStart, sV):
	if sV:
		startVisited = sV
	else:
		startVisited = [nextStart]
	pluralGoal = goalString
	pluralGoal += "s"
	if start:
		if nextStart == goalString or nextStart == pluralGoal:
			total = len(startVisited)
			print("You can reach the goal in " + str(total - 1) + " clicks.")
			print(startVisited)
		else:
			nextFromStart = nextPage(nextStart, startVisited)
			startVisited.append(nextFromStart)
			print(nextFromStart)
			greedy(nextFromStart, startVisited)

greedy(start, [])
