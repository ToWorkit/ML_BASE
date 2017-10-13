import bs4
soup = bs4.BeautifulSoup(open('../one.html'),'html.parser')
print(soup.prettify())
