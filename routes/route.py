# route/chatbot_route.py
from flask import Blueprint, request, jsonify
from model.model import answer_question_from_named_websites, websites

# Define a blueprint for the chatbot
chatbot_bp = Blueprint('chatbot', __name__)

@chatbot_bp.route('/ask', methods=['POST'])
def ask():
    user_query = request.json.get('query')
    
    if not user_query:
        return jsonify({"error": "Query is required"}), 400
    
    try:
        # Get the response from test.py
        answer = answer_question_from_named_websites(user_query, websites)
        return jsonify({"answer": answer})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
