import requests

# Function to fetch the latest news articles based on a query
def get_news_articles(query):
    api_key = "a9315fe0d17c4f13983b0e620acb9dfe"  # Replace with your actual API key
    url = f"https://newsapi.org/v2/everything?q={query}&language=en&apiKey={api_key}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        articles = response.json().get('articles', [])

        if not articles:
            return "No news articles found for that topic."

        news_summary = ""
        for idx, article in enumerate(articles[:5], start=1):  # Limit to the first 5 articles
            title = article.get('title')
            description = article.get('description', 'No description available')
            content = article.get('content', 'No detailed content available')
            source = article.get('source', {}).get('name', 'Unknown source')
            url = article.get('url')

            news_summary += (
                f"\nArticle {idx}:\n"
                f"Title: {title}\n"
                f"Description: {description}\n"
                f"Content: {content}\n"
                f"Source: {source}\n"
                f"Link: {url}\n"
                "------------------------------------------------------------\n"
            )

        return news_summary.strip()

    except requests.exceptions.RequestException as e:
        return f"Error fetching news: {str(e)}"


# Main chat loop
def main():
    print("Welcome to the News Research Chatbot (NewsAPI Based Only)")
    print("Type 'exit' to quit.\n")

    while True:
        query = input("You: ").strip()

        if query.lower() == "exit":
            print("Goodbye!")
            break

        print("\nFetching news...\n")
        print(get_news_articles(query))


if __name__ == "__main__":
    main()
