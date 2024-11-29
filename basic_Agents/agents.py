# agents.py
from openai import OpenAI
from config import OPENAI_API_KEY

# Initialize OpenAI client with API key from config
client = OpenAI(api_key=OPENAI_API_KEY)

class AgentAlpha:
    """Agent specialized in data analysis tasks"""
    def analyze_data(self, data):
        # Send data analysis request to GPT-4
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are an analytical assistant specialized in data analysis."},
                {"role": "user", "content": f"Analyze this data: {data}"}
            ]
        )
        # Return the AI's analysis
        return response.choices[0].message.content

class AgentBeta:
    """Agent specialized in content generation tasks"""
    def create_content(self, topic):
        # Send content generation request to GPT-4
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a creative assistant that generates engaging content."},
                {"role": "user", "content": f"Generate content on the topic: {topic}"}
            ]
        )
        # Return the generated content
        return response.choices[0].message.content
