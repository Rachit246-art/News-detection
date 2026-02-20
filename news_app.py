import requests
from datetime import datetime
from typing import List, Dict, Optional

class NewsApp:
    """A simple news application that fetches current news and top headlines by category."""
    
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://newsapi.org/v2"
    
    def get_top_headlines(self, category: str = "general", country: str = "us", limit: int = 10) -> List[Dict]:
        """
        Fetch top headlines for a specific category.
        
        Args:
            category: News category (business, entertainment, general, health, science, sports, technology)
            country: Country code (us, gb, ca, etc.)
            limit: Number of articles to return (max 10)
        
        Returns:
            List of news articles
        """
        endpoint = f"{self.base_url}/top-headlines"
        params = {
            "apiKey": self.api_key,
            "category": category,
            "country": country,
            "pageSize": min(limit, 10)
        }
        
        try:
            response = requests.get(endpoint, params=params)
            response.raise_for_status()
            data = response.json()
            
            if data["status"] == "ok":
                return self._format_articles(data["articles"])
            else:
                return []
        except Exception as e:
            print(f"Error fetching headlines: {e}")
            return []
    
    def search_news(self, query: str, limit: int = 10) -> List[Dict]:
        """
        Search for news articles by keyword.
        
        Args:
            query: Search query
            limit: Number of articles to return
        
        Returns:
            List of news articles
        """
        endpoint = f"{self.base_url}/everything"
        params = {
            "apiKey": self.api_key,
            "q": query,
            "pageSize": min(limit, 10),
            "sortBy": "publishedAt"
        }
        
        try:
            response = requests.get(endpoint, params=params)
            response.raise_for_status()
            data = response.json()
            
            if data["status"] == "ok":
                return self._format_articles(data["articles"])
            else:
                return []
        except Exception as e:
            print(f"Error searching news: {e}")
            return []
    
    def _format_articles(self, articles: List[Dict]) -> List[Dict]:
        """Format articles for display."""
        formatted = []
        for article in articles:
            formatted.append({
                "title": article.get("title", "No title"),
                "description": article.get("description", "No description"),
                "source": article.get("source", {}).get("name", "Unknown"),
                "author": article.get("author", "Unknown"),
                "url": article.get("url", ""),
                "published_at": article.get("publishedAt", "")
            })
        return formatted
    
    def display_headlines(self, category: str = "general"):
        """Display top 10 headlines for a category."""
        print(f"\n{'='*80}")
        print(f"TOP 10 HEADLINES - {category.upper()}")
        print(f"{'='*80}\n")
        
        articles = self.get_top_headlines(category=category)
        
        if not articles:
            print("No articles found.")
            return
        
        for idx, article in enumerate(articles, 1):
            print(f"{idx}. {article['title']}")
            print(f"   Source: {article['source']} | Author: {article['author']}")
            print(f"   {article['description']}")
            print(f"   URL: {article['url']}")
            print(f"   Published: {article['published_at']}")
            print()


def main():
    # Your NewsAPI key from https://newsapi.org/
    API_KEY = "b95c13f0917c4230bdab159c60532b57"

    app = NewsApp(API_KEY)
    
    # Available categories
    categories = ["business", "entertainment", "general", "health", "science", "sports", "technology"]
    
    print("Welcome to News App!")
    print("\nAvailable categories:")
    for i, cat in enumerate(categories, 1):
        print(f"{i}. {cat.capitalize()}")
    
    print("\nOptions:")
    print("- Enter category name or number to view top 10 headlines")
    print("- Type 'search <keyword>' to search for specific news")
    print("- Type 'quit' to exit")
    
    while True:
        user_input = input("\nEnter your choice: ").strip().lower()
        
        if user_input == "quit":
            print("Thank you for using News App!")
            break
        
        if user_input.startswith("search "):
            query = user_input[7:]
            print(f"\nSearching for: {query}")
            articles = app.search_news(query)
            if articles:
                for idx, article in enumerate(articles, 1):
                    print(f"\n{idx}. {article['title']}")
                    print(f"   Source: {article['source']}")
                    print(f"   URL: {article['url']}")
            else:
                print("No articles found.")
        
        elif user_input.isdigit() and 1 <= int(user_input) <= len(categories):
            category = categories[int(user_input) - 1]
            app.display_headlines(category)
        
        elif user_input in categories:
            app.display_headlines(user_input)
        
        else:
            print("Invalid input. Please try again.")


if __name__ == "__main__":
    main()
