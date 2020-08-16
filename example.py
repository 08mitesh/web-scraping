import requests
from bs4 import BeautifulSoup

data = []



## URL from where we want to scrap the data
blog_list = requests.get("https://www.codeheroku.com/blog.html")

## Get the page content
blog_conent = blog_list.content

## Now converting string output to HTML using html-parser
blog_html_content = BeautifulSoup(blog_conent,'html.parser')

## prettify the blog html contnet using prettify method
##final_content = blog_html_content.prettify()

##printing an outut
##print(final_content)

## To access body of the page 
## print(blog_html_content.body)

##access sepcific section from the page
section = blog_html_content.find('section', attrs={'class':'card-group-2'})


## accessing child element using paent 
all_cards = section.find_all('div',attrs={'class':'card'})

##find all tiles
for card in all_cards:
	blog = {}
	title = card.find('h2',class_='card-title')
	date = card.find('p',class_="card-date")

	## get the text from the title 
	title_text = title.string
	date_text = date.string

	##remove the extra spaces from the title text
	title_of_blog = title_text.strip()
	date_of_blog = date_text.strip()

	## setting title as object value
	blog['title'] = title_of_blog
	blog['date'] = date_of_blog

	## appending each title to final array
	data.append(blog)

print(data)