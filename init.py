from bs4 import BeautifulSoup
import urllib

# use this image scraper from the location that 
#you want to save scraped images to

def make_soup(url):
	html = urllib.request.urlopen(url).read()
	return BeautifulSoup(html, "html.parser")

def get_images(url):
	soup = make_soup(url)
	#this makes a list of bs4 element tags
	links = [a for a in soup.findAll('a')]
	print (str(len(links)) + "images found.")
	print 'Downloading images to current working directory.'
	#compile our unicode list of image links
	image_links = [each.get('href') for each in links]
	# remove non image files
	new_image_links = image_links[5:]
	for each in new_image_links:
		# instance of teh website's name
		filename="http://limbero.org/jl8/comics/" + each[-1]
		urllib.request.urlretrieve.urlretrieve(each, filename)
		
	return new_image_links

	# I need to find a way to skip the first couple of links as they aren't images

#a standard call looks like this
#