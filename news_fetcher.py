import requests

# ✅ HARDCODE API KEY HERE (TEMPORARY)
NEWS_API_KEY = "a9315fe0d17c4f13983b0e620acb9dfe"

def get_news(query):
    print(f"🟢 Using API key: {NEWS_API_KEY}")
    print(f"🟢 Searching for news on: {query}")

    url = f"https://newsapi.org/v2/everything?q={query}&sortBy=publishedAt&language=en&apiKey={NEWS_API_KEY}"

    response = requests.get(url)
    print(f"🟡 Status Code: {response.status_code}")
    data = response.json()
    print("🟠 Raw response:", data)

    articles = data.get("articles", [])
    news_texts = []

    for article in articles:
        title = article.get("title", "")
        description = article.get("description", "")
        if title and description:
            news_texts.append(f"{title}. {description}")

    return news_texts
