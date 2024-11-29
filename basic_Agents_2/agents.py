# agents.py
from openai import OpenAI
from config import OPENAI_API_KEY
from agent_config import AGENT_CONFIGS

client = OpenAI(api_key=OPENAI_API_KEY)

class BaseAgent:
    """Base class for all agents with common functionality."""
    def __init__(self, agent_type):
        if agent_type not in AGENT_CONFIGS:
            raise ValueError(f"Unknown agent type: {agent_type}")
        
        config = AGENT_CONFIGS[agent_type]
        self.role = config["role"]
        self.goal = config["goal"]
        self.prompts = config["prompts"]
    
    def _format_prompt(self, prompt_template, **kwargs):
        """Format prompt template with given parameters."""
        return prompt_template.format(
            role=self.role,
            goal=self.goal,
            **kwargs
        )
    
    def _create_completion(self, role_content, user_content):
        """Create a completion using OpenAI API."""
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": role_content},
                {"role": "user", "content": user_content}
            ]
        )
        return response.choices[0].message.content

class AgentAlpha(BaseAgent):
    def __init__(self):
        super().__init__("alpha")

    def analyze_data(self, data, tone="quick", context=None):
        prompt_config = self.prompts[tone]
        
        role_content = self._format_prompt(prompt_config["role_template"])
        user_content = self._format_prompt(prompt_config["user_template"], data=data)
        
        if context:
            user_content += f"\nAdditional Context: {context}"
        
        return self._create_completion(role_content, user_content)

class AgentBeta(BaseAgent):
    def __init__(self):
        super().__init__("beta")

    def create_content(self, topic, tone="quick", context=None):
        prompt_config = self.prompts[tone]
        
        role_content = self._format_prompt(prompt_config["role_template"])
        user_content = self._format_prompt(prompt_config["user_template"], topic=topic)
        
        if context:
            user_content += f"\nAdditional Context: {context}"
        
        return self._create_completion(role_content, user_content)
