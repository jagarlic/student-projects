from bs4 import BeautifulSoup
from nltk.corpus import wordnet
import urllib2
import re

satisfiablePercent = .8
start = "divorce"
goalString = "Margarine"
goal = wordnet.synset("Margarine.n.01")

def nextPage(link, visited, aim):
	aim = wordnet.synsets(aim)[0]
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
			if link == start:
				return link
			if wordnet.synsets(link):
				if link not in visited:
					w1 = wordnet.synsets(link)[0]
					score = w1.wup_similarity(aim)
					if score >= satisfiablePercent:
						return link
					elif score >= currentBest[1]:
						currentBest[0] = link
						currentBest[1] = score
	return currentBest[0]

def bidirectional(nextStart, nextGoal, sV, gV):
	keepGoing = True
	if sV:
		startVisited = sV
	else:
		startVisited = [nextStart]
	if gV:
		goalVisited = gV
	else:
		goalVisited = [nextGoal]
	if start:
		if nextStart == goalString:
			total = len(startVisited)
			print("You can reach the goal in " + str(total - 1) + " clicks.")
			print(startVisited)
			keepGoing = False
		if nextGoal == start:
			total = len(goalVisited)
			print("You can reach the goal in " + str(total - 1) + " clicks.")
			print(goalVisited)
			keepGoing = False
		if (nextStart in goalVisited and keepGoing):
			i = goalVisited.index(nextStart)
			goalVisited = goalVisited[::-1]
			goalVisited = goalVisited[1:]
			path = startVisited
			path.extend(goalVisited[:i + 1])
			total = len(path) - 2
			print("You can reach the goal in " + str(total) + " clicks.")
			print(path)
			keepGoing = False
		else:
			nextFromStart = nextPage(nextStart, startVisited, nextGoal)
			startVisited.append(nextFromStart)
	if keepGoing:
		if nextGoal in startVisited:
			r = startVisited.index(nextGoal)
			goalVisited = goalVisited[::-1]
			path = startVisited[:r + 1]
			path.extend(goalVisited[1:])
			total = len(path) - 2
			print("You can reach the goal in " + str(total) + " clicks.")
			print(path)
			keepGoing = False
		else:
			nextFromGoal = nextPage(nextGoal, goalVisited, nextFromStart)
			goalVisited.append(nextFromGoal)
	if keepGoing:
		print(nextFromStart)
		print(nextFromGoal)
		bidirectional(nextFromStart, nextFromGoal, startVisited, goalVisited)

bidirectional(start, goalString, [], [])
