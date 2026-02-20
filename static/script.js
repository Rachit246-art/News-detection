let currentCategory = 'general';

// Load news on page load
document.addEventListener('DOMContentLoaded', () => {
    loadNews('general');
    
    // Category buttons
    document.querySelectorAll('.category-btn').forEach(btn => {
        btn.addEventListener('click', () => {
            document.querySelectorAll('.category-btn').forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            currentCategory = btn.dataset.category;
            loadNews(currentCategory);
        });
    });
    
    // Search functionality
    document.getElementById('searchBtn').addEventListener('click', performSearch);
    document.getElementById('searchInput').addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            performSearch();
        }
    });
});

function performSearch() {
    const query = document.getElementById('searchInput').value.trim();
    if (query) {
        searchNews(query);
    }
}

async function loadNews(category) {
    showLoading(true);
    hideError();
    
    try {
        const response = await fetch(`/api/headlines/${category}`);
        const data = await response.json();
        
        if (data.success) {
            displayNews(data.articles);
        } else {
            showError(data.error || 'Failed to load news');
        }
    } catch (error) {
        showError('Network error. Please try again.');
    } finally {
        showLoading(false);
    }
}

async function searchNews(query) {
    showLoading(true);
    hideError();
    
    try {
        const response = await fetch(`/api/search?q=${encodeURIComponent(query)}`);
        const data = await response.json();
        
        if (data.success) {
            displayNews(data.articles);
        } else {
            showError(data.error || 'Failed to search news');
        }
    } catch (error) {
        showError('Network error. Please try again.');
    } finally {
        showLoading(false);
    }
}

function displayNews(articles) {
    const container = document.getElementById('newsContainer');
    container.innerHTML = '';
    
    if (!articles || articles.length === 0) {
        container.innerHTML = '<p style="color: white; text-align: center; font-size: 1.2rem;">No articles found.</p>';
        return;
    }
    
    articles.forEach(article => {
        const card = createNewsCard(article);
        container.appendChild(card);
    });
}

function createNewsCard(article) {
    const card = document.createElement('div');
    card.className = 'news-card';
    
    const imageUrl = article.urlToImage || 'https://via.placeholder.com/400x200?text=No+Image';
    const title = article.title || 'No title';
    const description = article.description || 'No description available';
    const source = article.source?.name || 'Unknown';
    const author = article.author || 'Unknown';
    const publishedAt = article.publishedAt ? new Date(article.publishedAt).toLocaleDateString() : 'Unknown date';
    const url = article.url || '#';
    
    card.innerHTML = `
        <img src="${imageUrl}" alt="${title}" class="news-image" onerror="this.src='https://via.placeholder.com/400x200?text=No+Image'">
        <div class="news-content">
            <div class="news-source">${source}</div>
            <h2 class="news-title">${title}</h2>
            <p class="news-description">${description}</p>
            <div class="news-meta">
                <span>By ${author}</span>
                <span>${publishedAt}</span>
            </div>
            <a href="${url}" target="_blank" class="news-link">Read More →</a>
        </div>
    `;
    
    return card;
}

function showLoading(show) {
    document.getElementById('loading').style.display = show ? 'block' : 'none';
}

function showError(message) {
    const errorDiv = document.getElementById('error');
    errorDiv.textContent = message;
    errorDiv.style.display = 'block';
}

function hideError() {
    document.getElementById('error').style.display = 'none';
}
