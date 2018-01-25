# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

import scraperwiki
import lxml.html
#
# # Read in a page
html = scraperwiki.scrape("https://int.soccerway.com/teams/england/chelsea-football-club/661/")

#create an empty dictionary variable to hold our data later
record = {}
mydictionary = {"name" : "Paul"}

'''
# # Find something on the page using css selectors
root = lxml.html.fromstring(html)
names = root.cssselect("td div a")
for name in names:
  print name.text.encode('ascii', 'ignore')
  print name.attrib['href']
  #store the link in the variable 'record' under the key 'link'
  record['link'] = name.attrib['href']
  record['name'] = name.text.encode('ascii', 'ignore')
  print record
  scraperwiki.sqlite.save(unique_keys=['link'], data=record, table_name = "players")
'''

players = root.cssselect("td")
for picture in pictures:
  links = picture.cssselect("div span")
  for link in links:
    record['img'] = link.attrib['class']
    #record['name'] = link.text.encode('ascii', 'ignore')
    print record
    scraperwiki.sqlite.save(unique_keys=['img'], data=record, table_name = "pictures")
#
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
