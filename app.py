from flask import Flask, jsonify, request
from flask_cors import CORS
from newsapi import NewsApiClient

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend requests

# Initialize NewsAPI Client
NEWS_API_KEY = "e6ef91b11da3498b85eaf41692919ec6"  # Replace with your actual key
newsapi = NewsApiClient(api_key=NEWS_API_KEY)

@app.route('/get_news', methods=['GET'])
def get_news():
    topic = request.args.get('q', 'finance')  # Default to "finance" if no query is provided
    try:
        articles = newsapi.get_everything(q=topic, language='en', sort_by='publishedAt', page=1)
        return jsonify(articles)  # Return news articles as JSON
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Return error if API call fails

if __name__ == "__main__":
    app.run(debug=True)
