import flask
from flask import Flask
from newsapi import NewsApiClient
from flask import request, redirect

app = Flask(__name__)
app.debug = True
# app.run(debug=True)

# Init
newsapi = NewsApiClient(api_key='ab38b7cbd99144fda017ca64ba98df3b')
query_input = "Democratic primary"
from_input = "2019-11-06"
to_input = "2019-11-06"
page_size_input = 100
page_input = 1
date = to_input[5:7] + "/" + to_input[8:10] + "/" + to_input[0:4]
print(date)

# download all articles from past 3 days from NYT, Fox News and MSNBC

# /v2/everything
def retrieve_everything(query_input,from_input, to_input):

    NYT = newsapi.get_everything(
        q=query_input,
        # qintitle='impeach',
        sources='the-new-york-times',
        domains='nytimes.com',
        from_param=from_input,
        to=to_input,
        language='en',
        sort_by='relevancy',
        page_size=page_size_input,
        page=page_input)

    FOX = newsapi.get_everything(
                                              q=query_input,
                                              # qintitle='impeach',
                                              sources='fox-news',
                                              domains='foxNEWS.com',
                                              from_param=from_input,
                                              to=to_input,
                                              language='en',
                                              sort_by='relevancy',
                                              page_size= page_size_input,
                                              page=page_input)

    CNN = newsapi.get_everything(
                                              q=query_input,
                                              # qintitle='impeach',
                                              sources='cnn',
                                              domains='us.cnn.com',
                                              from_param=from_input,
                                              to=to_input,
                                              language='en',
                                              sort_by='relevancy',
                                              page_size= page_size_input,
                                              page=page_input)

    Huffington_Post = newsapi.get_everything(
                                              q=query_input,
                                              # qintitle='impeach',
                                              sources='the-huffington-post',
                                              domains='huffingtonpost.com',
                                              from_param=from_input,
                                              to=to_input,
                                              language='en',
                                              sort_by='relevancy',
                                              page_size= page_size_input,
                                              page=page_input)

    USA_today = newsapi.get_everything(
                                              q=query_input,
                                              # qintitle='impeach',
                                              sources='usa-today',
                                              domains='usatoday.com',
                                              from_param=from_input,
                                              to=to_input,
                                              language='en',
                                              sort_by='relevancy',
                                              page_size= page_size_input,
                                              page=page_input)

    Reuters = newsapi.get_everything(
                                              q=query_input,
                                              # qintitle='impeach',
                                              sources='reuters',
                                              domains='reuters.com',
                                              from_param=from_input,
                                              to=to_input,
                                              language='en',
                                              sort_by='relevancy',
                                              page_size= page_size_input,
                                              page=page_input)

    Politico = newsapi.get_everything(
                                              q=query_input,
                                              # qintitle='impeach',
                                              sources='politico',
                                              domains='politico.com',
                                              from_param=from_input,
                                              to=to_input,
                                              language='en',
                                              sort_by='relevancy',
                                              page_size= page_size_input,
                                              page=page_input)


    Msnbc = newsapi.get_everything(
                                              q=query_input,
                                              # qintitle='impeach',
                                              sources='msnbc',
                                              domains='msnbc.com',
                                              from_param=from_input,
                                              to=to_input,
                                              language='en',
                                              sort_by='relevancy',
                                              page_size= page_size_input,
                                              page=page_input)

    content = [Msnbc, Huffington_Post, CNN, Politico, NYT, Reuters, USA_today, FOX]
    return content

@app.route('/')
def index():
    # print(content)
    return flask.render_template('index.html', content=retrieve_everything(query_input, from_input, to_input), date = date)
# NYT=NYT, Huffington_Post=Huffington_Post, Politico=Politico, Reuters=Reuters, USA_today=USA_today,CNN=CNN,FOX=FOX)


@app.route('/', methods = ['POST'])
def re_load():
    form = request.form["query"]
    date = request.form["date"]

    print(form)
    print(date)
    date_reformat=  date[-4:]+ "-"+date[0:2]+"-"+date[3:5]
    print(date_reformat)
    from_input = date_reformat
    to_input = date_reformat

    query_input = form
    return flask.render_template('index.html', content=retrieve_everything(query_input, from_input, to_input), date=date)





if __name__ == '__main__':
    app.run()
