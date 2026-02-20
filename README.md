# News App

A Python web application that fetches current news and top 10 headlines by category using the NewsAPI.

## Features

- Modern, responsive web interface
- Get top 10 headlines by category (business, entertainment, general, health, science, sports, technology)
- Search for news articles by keyword
- Beautiful card-based layout with images
- Real-time news updates

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Your API key is already configured in `app.py`

## Usage

1. Start the Flask server:
```bash
python app.py
```

2. Open your browser and go to:
```
http://localhost:5000
```

3. Browse news by clicking category buttons or use the search bar to find specific topics

## Available Categories

- Business
- Entertainment
- General
- Health
- Science
- Sports
- Technology

## Files Structure

```
News detection/
├── app.py              # Flask backend server
├── news_app.py         # CLI version (optional)
├── requirements.txt    # Python dependencies
├── templates/
│   └── index.html     # Main HTML page
└── static/
    ├── style.css      # Styling
    └── script.js      # Frontend JavaScript
```

## API Information

This app uses the [NewsAPI](https://newsapi.org/) which provides:
- Free tier: 100 requests per day
- Access to news from 80,000+ sources worldwide
- Real-time news updates
