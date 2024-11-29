# agents.py
from openai import OpenAI
from config import OPENAI_API_KEY

# Initialize the OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)

# Base Agent class for common functionality
class BaseAgent:
    def __init__(self, role_description=None, model="gpt-4o"):
        self.client = client
        self.model = model
        self.role_description = role_description or "You are a helpful AI assistant."

    def _generate_response(self, prompt, additional_context=None):
        messages = [
            {"role": "system", "content": self.role_description}
        ]
        
        if additional_context:
            messages.append({"role": "system", "content": additional_context})
            
        messages.append({"role": "user", "content": prompt})
        
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages
        )
        return response.choices[0].message.content

class AgentAlpha(BaseAgent):
    def __init__(self, role_description=None):
        super().__init__(role_description or "You are an analytical assistant specialized in data analysis. Provide detailed, accurate, and insightful analysis.")
    
    def analyze_data(self, data, context=None):
        prompt = f"Analyze this data: {data}"
        return self._generate_response(prompt, context)

class AgentBeta(BaseAgent):
    def __init__(self, role_description=None):
        super().__init__(role_description or "You are a creative assistant specialized in content generation. Create engaging, informative, and well-structured content.")
    
    def create_content(self, topic, context=None):
        prompt = f"Generate content on the topic: {topic}"
        return self._generate_response(prompt, context)
