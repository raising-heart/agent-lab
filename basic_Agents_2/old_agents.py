# agents.py
from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

class AgentAlpha:
    def __init__(self):
        self.role = "Data Analyst specializing in action movie analysis"
        self.goal = "Provide insightful analysis of movie data with focus on themes of revenge and resilience"

    def analyze_data(self, data, tone="quick"):
        if tone == "detailed":
            role_content = (
                f"You are a {self.role}. Your goal is to {self.goal}. "
                "Provide in-depth insights assuming limited movie specifics, but analyze it as if it were a typical high-action movie."
            )
            user_content = (
                f"Provide a detailed analysis of the movie story, assuming themes of revenge, resilience, and personal transformation. "
                "Do not request additional data, and base the response on common storytelling elements in action movies."
            )
        else:
            role_content = (
                "You are a quick and efficient data analyst. Provide a general, concise analysis assuming this is an action movie with typical revenge and resilience themes. "
                "Use basic movie structure points like narrative and character arcs without asking for further data."
            )
            user_content = (
                f"Provide a quick overview of the movie story, focusing on general action movie elements like structure and theme. "
                "Assume it's a high-action movie centered around revenge and resilience."
            )

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": role_content},
                {"role": "user", "content": user_content}
            ]
        )
        return response.choices[0].message.content


class AgentBeta:
    def __init__(self):
        self.role = "Content Generator focused on action movie themes"
        self.goal = "Generate engaging content that explores themes of revenge and resilience in action movies"

    def create_content(self, topic, tone="quick"):
        if tone == "detailed":
            role_content = (
                f"You are a {self.role}. Your goal is to {self.goal}. "
                "Provide detailed content based on typical elements in the genre without asking for more data."
            )
            user_content = (
                f"Create detailed content on the topic: {topic}, assuming it pertains to a high-action movie with revenge and resilience themes. "
                "Avoid requesting additional specifics and base content on general genre elements."
            )
        else:
            role_content = (
                "You are a concise content generator. Provide a brief, high-level overview on action movie topics with themes like revenge and resilience, "
                "focusing only on essential points without requesting additional data."
            )
            user_content = (
                f"Provide a quick overview on the topic: {topic}. Assume it is related to an action movie with revenge themes and keep the content concise."
            )

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": role_content},
                {"role": "user", "content": user_content}
            ]
        )
        return response.choices[0].message.content
