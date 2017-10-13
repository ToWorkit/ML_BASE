import bs4
soup = bs4.BeautifulSoup(open('../one.html'),'lxml')
# print(soup.prettify())

a_tag = soup.find_all('a')

print(a_tag[0])
print(a_tag[0].contents)

title_tag = soup.head.contents[0]
print(title_tag.contents)
for child in title_tag.children:
	print(child)

# soup.find_all('a')	