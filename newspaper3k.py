import newspaper
from newspaper import Article
import nltk
from newspaper import fulltext

# nltk.download()

url = "https://www.welt.de/politik/ausland/article203659270/Impeachment-Trump-Die-Befragung-von-Vindman-wird-zum-Justizthriller.html"
article = Article(url)

article.download()

article.parse()
#
# print(article.authors)
# print(article.publish_date)
# print(article.text)
# print(article.top_image)
# print(article.summary)
# #
# article.nlp()
# print(article.keywords)
#
# welt_paper = newspaper.build('http://welt.de')
welt_paper = newspaper.build('https://www.sueddeutsche.de/')

#
counter = 0
for article in welt_paper.articles:
    counter += 1
    print(article.url)
    print(counter)

print(counter)