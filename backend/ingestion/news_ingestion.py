from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key="04c48cd310a74775bc3ca020e6ada83a")

articles = newsapi.get_everything(
    q="stock market crash",
    language="en"
)

print(articles)