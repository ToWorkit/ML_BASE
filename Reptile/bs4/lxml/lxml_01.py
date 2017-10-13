import bs4
soup = bs4.BeautifulSoup(open('../one.html'),'lxml')
print(soup.prettify())
