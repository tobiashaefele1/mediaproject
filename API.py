
from newsapi import NewsApiClient

# structure of the return object
# {‘status: ‘ok’,
#           ‘totalResults’: 11,
#            ‘articles’:  [   {
#                              source: {id: xxx, name: xxxx },
#                              author: xxxx,
#                              title: xxxxx,
#                              ‘url’: xxxx,
#                              ‘urlToImage’: xxxxx,
#                              ‘publishedAt’: xxxxxx,
#                              ‘content’: xxxxxx,
#                             },
#                             {   ….         },
#                             {   ….         },
#                          ]
# };

query_input = "impeachment"
from_input = "2019-11-06"
to_input = "2019-11-06"
page_size_input = 100
page_input = 1

# # Init for development: tobias_haefele@student.hks.harvard.edu
# newsapi = NewsApiClient(api_key='ab38b7cbd99144fda017ca64ba98df3b')

# key for heroku (tobiasahaefele@gmail.com)
newsapi = NewsApiClient(api_key='6842a92db4434ca28611f793977b03fe')

## get all the sources for Germany:
german_sources = newsapi.get_sources(country="us")

# for x in german_sources:
#     print (x.name)


for key, value in german_sources.items():
    if key == "sources":
        for article in value:
            print(article["name"])




#
#
#     # /v2/everything
# NYT = newsapi.get_everything(
#                                           # q=query_input,
#                                           # qintitle='impeach',
#                                           sources='the-new-york-times',
#                                           domains='nytimes.com',
#                                           from_param=from_input,
#                                           to=to_input,
#                                           language='en',
#                                           sort_by='relevancy',
#                                           page_size= page_size_input,
#                                           page=page_input)
# FOX = newsapi.get_everything(
#                                           # q=query_input,
#                                           # qintitle='impeach',
#                                           sources='fox-news',
#                                           domains='foxNEWS.com',
#                                           from_param=from_input,
#                                           to=to_input,
#                                           language='en',
#                                           sort_by='relevancy',
#                                           page_size= page_size_input,
#                                           page=page_input)
#
# CNN = newsapi.get_everything(
#                                           # q=query_input,
#                                           # qintitle='impeach',
#                                           sources='cnn',
#                                           domains='us.cnn.com',
#                                           from_param=from_input,
#                                           to=to_input,
#                                           language='en',
#                                           sort_by='relevancy',
#                                           page_size= page_size_input,
#                                           page=page_input)
#
# Huffington_Post = newsapi.get_everything(
#                                           # q=query_input,
#                                           # qintitle='impeach',
#                                           sources='the-huffington-post',
#                                           domains='huffingtonpost.com',
#                                           from_param=from_input,
#                                           to=to_input,
#                                           language='en',
#                                           sort_by='relevancy',
#                                           page_size= page_size_input,
#                                           page=page_input)
#
# USA_today = newsapi.get_everything(
#                                           # q=query_input,
#                                           # qintitle='impeach',
#                                           sources='usa-today',
#                                           domains='usatoday.com',
#                                           from_param=from_input,
#                                           to=to_input,
#                                           language='en',
#                                           sort_by='relevancy',
#                                           page_size= page_size_input,
#                                           page=page_input)
#
# Reuters = newsapi.get_everything(
#                                           # q=query_input,
#                                           # qintitle='impeach',
#                                           sources='reuters',
#                                           domains='reuters.com',
#                                           from_param=from_input,
#                                           to=to_input,
#                                           language='en',
#                                           sort_by='relevancy',
#                                           page_size= page_size_input,
#                                           page=page_input)
#
# Politico = newsapi.get_everything(
#                                           # q=query_input,
#                                           # qintitle='impeach',
#                                           sources='politico',
#                                           domains='politico.com',
#                                           from_param=from_input,
#                                           to=to_input,
#                                           language='en',
#                                           sort_by='relevancy',
#                                           page_size= page_size_input,
#                                           page=page_input)
#
#
# # do machine learning on all of these to "match" articles
#
# # NYT, FOX, CNN, Huffington_Post, USA_today, Reuters, Politico...
#
#
#
# # print(NYT)
#
# fox_test = Politico["articles"][9]["content"]
# print(fox_test)
#
#
# NYT_content = [];
# NYT_content.append(fox_test)
#
# for key, value in NYT.items():
#     if key == "articles":
#         for article in value:
#             for x,y in article.items():
#                 if x == "content" and y != None:
#                     NYT_content.append(y)
#
#
# # print(NYT_content)
#
#
# from sklearn.feature_extraction.text import TfidfVectorizer
# vect = TfidfVectorizer(min_df=1, stop_words="english")
# tfidf = vect.fit_transform(NYT_content)
# pairwise_similarity = tfidf * tfidf.T
#
# arr = pairwise_similarity.toarray()
#
# print(arr)
#
# import numpy as np
#
# arr = pairwise_similarity.toarray()
# np.fill_diagonal(arr, np.nan)
#
# input_doc = NYT_content[0]
# input_idx = NYT_content.index(input_doc)
# print(input_idx)
#
#
# result_idx = np.nanargmax(arr[input_idx])
# print(NYT_content[result_idx])
#
#
#
#
#
#
#
#
#
#
# #
# #
# # #### model code copy pasted from here: https://medium.com/@adriensieg/text-similarities-da019229c894
# #
# # module_url = "https://tfhub.dev/google/universal-sentence-encoder/1?tf-hub-format=compressed"
# #
# # # Import the Universal Sentence Encoder's TF Hub module
# # embed = hub.Module(module_url)
# #
# # # sample text
# # messages = [
# #     # Smartphones
# #     "My phone is not good.",
# #     "Your cellphone looks great.",
# #
# #     # Weather
# #     "Will it snow tomorrow?",
# #     "Recently a lot of hurricanes have hit the US",
# #
# #     # Food and health
# #     "An apple a day, keeps the doctors away",
# #     "Eating strawberries is healthy",
# # ]
# #
# # similarity_input_placeholder = tf.placeholder(tf.string, shape=(None))
# # similarity_message_encodings = embed(similarity_input_placeholder)
# # with tf.Session() as session:
# #     session.run(tf.global_variables_initializer())
# #     session.run(tf.tables_initializer())
# #     message_embeddings_ = session.run(similarity_message_encodings, feed_dict={similarity_input_placeholder: messages})
# #
# #     corr = np.inner(message_embeddings_, message_embeddings_)
# #     print(corr)
# #     heatmap(messages, messages, corr)
# #
# #
# # def heatmap(x_labels, y_labels, values):
# #     fig, ax = plt.subplots()
# #     im = ax.imshow(values)
# #
# #     # We want to show all ticks...
# #     ax.set_xticks(np.arange(len(x_labels)))
# #     ax.set_yticks(np.arange(len(y_labels)))
# #     # ... and label them with the respective list entries
# #     ax.set_xticklabels(x_labels)
# #     ax.set_yticklabels(y_labels)
# #
# #     # Rotate the tick labels and set their alignment.
# #     plt.setp(ax.get_xticklabels(), rotation=45, ha="right", fontsize=10,
# #              rotation_mode="anchor")
# #
# #     # Loop over data dimensions and create text annotations.
# #     for i in range(len(y_labels)):
# #         for j in range(len(x_labels)):
# #             text = ax.text(j, i, "%.2f" % values[i, j],
# #                            ha="center", va="center", color="w",
# #                            fontsize=6)
# #
# #     fig.tight_layout()
# #     plt.show()
# #
# # #
# # # view
# # # rawUniversal_sentence_encoder.py
# # # hosted
# # # with ❤ by GitHub
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# # print(len(NYT["articles"]))
# # print(NYT["totalResults"])
# #
# # for x in range(0, NYT["totalResults"]):
# #     print(NYT["articles"][x]["source"]["name"])
#
#
#
#
#
#
#
# # top_headlines = newsapi.get_top_headlines(q='impeach',
# #                                           sources='the-new-york-times,cnn, fox-news, the-huffington-post, usa-today',
# #                                           # domains='nytimes.com, cnn.com, foxNEWS.com, huffingtonpost.com, usatoday.com',
# #                                           # from_param='2019-11-06',
# #                                           # to='2019-11-06',
# #                                           language='en',
# #                                           # sort_by='relevancy',
# #                                           page=2)
#
#
# # print(all_articles)
#
#
#
# # download all articles from past 3 days from NYT, Fox News and MSNBC
# # all_articles = newsapi.get_everything(
# #                                           q='"impeachment"',
# #                                           # qintitle='impeach',
# #                                           sources='the-new-york-times,cnn, fox-news, the-huffington-post, usa-today',
# #                                           domains='nytimes.com, cnn.com, foxNEWS.com, huffingtonpost.com, usatoday.com',
# #                                           from_param='2019-11-06',
# #                                           to='2019-11-06',
# #                                           language='en',
# #                                           sort_by='relevancy',
# #                                           page_size= 100,
# #                                           page=1)
#
# # print(all_articles)
#
#
#
