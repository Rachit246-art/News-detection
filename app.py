from flask import Flask, render_template, jsonify, request
import requests

app = Flask(__name__)

# Your NewsAPI key
API_KEY = "b95c13f0917c4230bdab159c60532b57"
BASE_URL = "https://newsapi.org/v2"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/headlines/<category>')
def get_headlines(category):
    """Get top 10 headlines for a category."""
    endpoint = f"{BASE_URL}/top-headlines"
    params = {
        "apiKey": API_KEY,
        "category": category,
        "country": "us",
        "pageSize": 10
    }
    
    try:
        response = requests.get(endpoint, params=params)
        response.raise_for_status()
        data = response.json()
        
        if data["status"] == "ok":
            return jsonify({
                "success": True,
                "articles": data["articles"]
            })
        else:
            return jsonify({
                "success": False,
                "error": "Failed to fetch news"
            })
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        })

@app.route('/api/search')
def search_news():
    """Search for news articles."""
    query = request.args.get('q', '')
    
    if not query:
        return jsonify({
            "success": False,
            "error": "Search query is required"
        })
    
    endpoint = f"{BASE_URL}/everything"
    params = {
        "apiKey": API_KEY,
        "q": query,
        "pageSize": 10,
        "sortBy": "publishedAt"
    }
    
    try:
        response = requests.get(endpoint, params=params)
        response.raise_for_status()
        data = response.json()
        
        if data["status"] == "ok":
            return jsonify({
                "success": True,
                "articles": data["articles"]
            })
        else:
            return jsonify({
                "success": False,
                "error": "Failed to search news"
            })
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
