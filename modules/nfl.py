from BeautifulSoup import BeautifulSoup
import urllib2

def map_abv(abv):
	return abv.upper()

def score(abv):
	abv = map_abv(abv)
	u = urllib2.urlopen('http://m.espn.go.com/nfl/scoreboard?')
	s = u.read()
	soup = BeautifulSoup(s)
	soup_html = soup.html
	if (soup_html == None):
		raise Exception("Problem getting the scoreboard")
	abv_el = soup_html.find(text=abv)
	if (abv_el == None):
		raise Exception("Couldn't find a team with that abbreviation. Abbreviations are 3 letters (sometimes 2) that name the team's hometown.")
	game_el = abv_el.parent.parent.parent.parent
	game_text_els = game_el.findAll(text=True)
	out_text = ' '.join(game_text_els)
	return out_text

def get_score(phenny, input):
	abv = input.group(2)
	try:
		phenny.say(score(abv))
	except Exception as e:
		phenny.say(str(e))
get_score.commands = ['nfl']

if __name__ == '__main__':
	print __doc__.strip()
