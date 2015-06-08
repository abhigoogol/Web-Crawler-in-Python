__author__ = "Abhishek Singh Sambyal"
__email__ = "abhishek.sambyal@gmail.com"
__license__ = "GNU GENERAL PUBLIC LICENSE Version 3"

# Usuage: python crawler.py

import urllib
import re
import urlparse

''' Find all the links on the page, crawl each of them and store it in crawled list
The crawling is done in Depth First Search (DFS) fashion.
Will crawl from the last link of the page and keep crawling until there is no
link left.
'''
def crawledlinks(seed):
	tocrawl = [seed]
	crawled = []
	
	# Crawl until 'tocrawl' list in not empty
	while tocrawl:
		new_links = []
		page = tocrawl[len(tocrawl)-1]
		
		# Check if page is already crawled or not
		if page not in crawled:
			try:
				# Get all the links of the page
				new_links = get_all_links(page)
			except:
				print 'Crawling stopped at: ' + page
				return crawled
				
			# Store crawled link in 'crawled' list from 'tocrawl' list
			crawled.append(tocrawl.pop())
			for x in new_links:
				tocrawl.append(x)
		else:
			tocrawl.pop()
			
	return crawled
	
	
	
# Get all the links from the page
def get_all_links(url):
	uf = urllib.urlopen(url)
	
	# Parsing the current url
	parseurl = urlparse.urlparse(url)
	
	# Find all the links in a page
	match = re.findall(r'<a href=[\'"]?([^\'" >]+)', uf.read())
	links = []
	
	''' Parse each 'm'
		Check whether 'm' is a complete url, path or #
		if m is a complete url then take 'm' as it is
		if m is a path, add the current url to the path
		if m is a '#' add current url to '#'
		'''
	for m in match:
		
		parse_m = urlparse.urlparse(m)
		if parse_m.netloc != '':
			links.append(m)
			
		# Add current url to 'm' to get the full url path
		elif m != '#':
			full_url = parseurl.scheme + '://' + parseurl.netloc + m
			links.append(full_url)
		else:
			full_url = parseurl.scheme + '://' + parseurl.netloc + '/' + m
			links.append(full_url)
	return links
	
	
def main():
	seed = 'http://python.org/'
	links = crawledlinks(seed)
	print links
	
	# Save crawled links in a links file
	'''f = open('links.txt', 'w')
	for x in links:
		f.write('\n')
		f.write(x)
	f.close()'''
	
	
	
if __name__ == '__main__':
	main()