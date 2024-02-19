from newsapi import NewsApiClient
import json

# Init
newsapi = NewsApiClient(api_key='90751242556e4934bcaf54e2919c2c4b')

articles = newsapi.get_everything(q='Killers of the Flower Moon', 
                                          from_param='2023-11-23',
                                          to='2023-11-23',
                                          language='en',
                                    )

data = json.dumps(articles, indent=4)
with open('my-articles2', 'w') as file:
    file.write(data)

