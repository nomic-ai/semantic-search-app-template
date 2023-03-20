import nomic
from nomic import AtlasProject
import pandas


#load a demo dataset of 25k news articles
news_articles = pandas.read_csv('https://raw.githubusercontent.com/nomic-ai/maps/main/data/ag_news_25k.csv').to_dict('records')

#create a project in the Atlas Embedding Database
project = AtlasProject(name='10k News Articles', unique_id_field='id')
#
# project = atlas.map_text(data=news_articles,
#                          indexed_field='text',
#                          id_field='id',
#                          name='News Articles 25k',
#                          description='25k News articles.',
#                          colorable_fields=['label'],
#                          )




