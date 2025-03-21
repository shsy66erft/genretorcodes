from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

# כתובת האתר שלך (עדכן בהתאם)
WEBSITE_URL = "https://yourwebsite.com"

def fetch_website_text(url):
    """שואב את התוכן של האתר לצורך חיפוש תשובות"""
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    text = " ".join([p.get_text() for p in soup.find_all(["p", "h1", "h2"])])
    return text if text else "לא נמצא מידע מתאים באתר."

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    user_input = data.get("question", "").lower()

    # **בדיקת בקשה למעבר לאתר**
    if "לך לאתר" in user_input or "פתח" in user_input or "מעבר ל" in user_input:
        return jsonify({"redirect": "https://www.google.com"})  # שנה לכתובת הרלוונטית

    # **בדיקת שאלה על האתר**
    website_content = fetch_website_text(WEBSITE_URL)
    if user_input in website_content.lower():
        response = "מצאתי מידע באתר שמתאים לשאלה שלך!"
    else:
        response = "לא מצאתי תשובה באתר, נסה לשאול משהו אחר."

    return jsonify({"answer": response})

if __name__ == '__main__':
    app.run(debug=True)