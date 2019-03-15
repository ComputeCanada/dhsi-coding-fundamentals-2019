# Uses the python3 newspaper library to scrape G&M directly rather than newsapi.org
# November 28, 2018
# John Simpson

# Note that Config options do not currently seem to work with newspaper.  Everything must be passed as parameters.

import newspaper
import re

category_extract = re.compile("(?<=\/).+?(?=\/)")

paper_url='https://www.thestar.com/'
paper = newspaper.build(paper_url,memoize_articles=False, browser_user_agent = "Mozilla/5.0")

#print(gm_paper.size())
print(len(paper.articles))

for article in paper.articles:
    article.download()
    article.parse()
    #print(article.top_node,article.clean_top_node)
    print(article.title,article.url,article.authors,article.summary)

"""            
            collection.insert_one({
                'source' : "The Globe And Mail",
                'title' : article.title,
                'url' : url_clean.sub("",article.url),
                'category' : category_extract.findall(article.url)[1:-1],
                'publishedAt' : article.publish_date,
                'authors' : article.authors,
                'description' : article.meta_description,
                'body' : article.text,
                'bodyRaw' : article.html,
"""