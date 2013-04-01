from BeautifulSoup import BeautifulSoup
import urllib2

def area(code):
	u = urllib2.urlopen('http://www.allareacodes.com/' + code)
	s = u.read()
	soup = BeautifulSoup(s[s.index('<html>'):]) # doctype tag preceding html tag fucks it up, apparently
	soup_html = soup.html
	if (soup_html == None):
		raise Exception("Problem getting info on area code " + code)
	details_tbl = soup_html.find('table', {'class': 'npa_details'})
	state_txt = details_tbl.find(text='State').findParent('tr').contents[1].text
	city_txt = details_tbl.find(text='Major City').findParent('tr').contents[1].text
	return 'Area code %s: %s, %s' % (code, city_txt, state_txt)

def get_area(phenny, input):
        code = input.group(2)
        try:   
                phenny.say(area(code))
        except Exception as e:
                phenny.say(str(e))

get_area.commands = ['area']

if __name__ == '__main__':
	# print area('404')
	print __doc__.strip()
