#python app.py run cmd

from flask_cors import CORS  # Import CORS
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from flask import Flask, request, jsonify
from dotenv import load_dotenv  # Make sure to import dotenv

load_dotenv()

def aishit(text):
    # Load the Google API key from environment variables
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    # Initialize the Gemini model
    llm4 = ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key= os.getenv("apikey"))
    # Define your query
    # Get the response from the model
    response = llm4.predict(text)
    return(response)

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": ["https://komer6.github.io/ai_flask_gemini_front", "http://localhost:5500"]}})
@app.route('/post', methods=['POST'])
def post():
    # Get the text from the POST request's JSON body
    user_input = request.json.get('text')
    if user_input:
        response = aishit(user_input)
        return jsonify({"response": response})
    else:
        return jsonify({"error": "No text provided"}), 400

if __name__ == '__main__':
    app.run(debug=True)
    print( os.getenv("apikey"))