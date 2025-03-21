from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

# כתובת האתר שלך (יש לשנות לכתובת האתר בפועל)
WEBSITE_URL = "https://shsy66erft.github.io/genretorcodes"

def fetch_website_text(url):
    """פונקציה ששואבת את התוכן מהאתר"""
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # מחפש רק טקסט מתוך התגיות הרלוונטיות (למשל <p>, <h1> וכו')
    text = " ".join([p.get_text() for p in soup.find_all(["p", "h1", "h2"])])
    
    return text if text else "לא נמצא מידע מתאים באתר."

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    user_question = data.get("question", "").lower()

    # קבלת תוכן האתר שלך
    website_content = fetch_website_text(WEBSITE_URL)

    # לוגיקה פשוטה למציאת תשובה בטקסט
    if user_question in website_content.lower():
        response = "מצאתי מידע באתר שלך שמתאים לשאלה!"
    else:
        response = "לא מצאתי תשובה באתר, נסה לשאול משהו אחר."

    return jsonify({"answer": response})

if __name__ == '__main__':
    app.run(debug=True)