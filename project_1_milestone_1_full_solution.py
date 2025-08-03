import os
import json
import pandas as pd
import openai
from dotenv import load_dotenv
import time
from google.colab import userdata

# Configure OpenAI API key using Colab Secrets
api_key = userdata.get('OPENAI_API_KEY')

# Initialize OpenAI client
client = openai.OpenAI(api_key=userdata.get('OPENAI_API_KEY'))

def test_openai_connection():
    """Test OpenAI API connection with a simple call."""
    try:
        client = openai.OpenAI(api_key=userdata.get('OPENAI_API_KEY'))
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": "Say 'API connection successful' if you can read this."}
            ],
            max_tokens=10,
            temperature=0
        )
        
        result = response.choices[0].message.content
        print(f"API Test Result: {result}")
        return True
        
    except Exception as e:
        print(f"API Connection Failed: {e}")
        return False

test_openai_connection()
