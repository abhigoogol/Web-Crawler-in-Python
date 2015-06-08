import urllib
import re


def store_links(seed):
	tocrawl = [seed]
	crawled = []
	while tocrawl:
		new_links = []
		page = tocrawl[len(tocrawl)-1]
		if page not in crawled:
			new_links = get_all_links(page)
			
			# Making pop() measns we are taking last link first i.e. Depth First Search
			crawled.append(tocrawl.pop())
			for x in new_links:
				tocrawl.append(x)
		else:
			tocrawl.pop()
	return crawled
	
	
def get_all_links(url):
	uf = urllib.urlopen(url)
	match = re.findall(r'<a href=[\'"]?([^\'" >]+)', uf.read())
	links = []
	for m in match:
		links.append(m)
	return links
	
	
def main():
	seed = 'https://www.udacity.com/cs101x/index.html'
	links = store_links(seed)
	print links
	
	
if __name__ == '__main__':
	main()