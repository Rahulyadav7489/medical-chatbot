from chatbot import chatbot

from flask import Flask, render_template, jsonify, request

app= Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/get", methods=["POST"])
def chat():
    data = request.get_json()       
    user_msg = data["msg"]          
    bot_reply= chatbot(user_msg)
    
    return jsonify({"response": bot_reply})

if __name__== "__main__":
    app.run(host= "0.0.0.0",port=8080, debug=True)









