# Task wrappers for the AI agents
from agents import AgentAlpha, AgentBeta

def analyze_position_task(name, context, role=None, additional_context=None):
    # Use AgentAlpha to analyze data and return formatted report
    alpha = AgentAlpha(role_description=role)
    report = alpha.analyze_data(context, additional_context)
    return f"Report for {name}: {report}"

def generate_content_task(topic, role=None, additional_context=None):
    # Use AgentBeta to generate content on given topic
    beta = AgentBeta(role_description=role)
    content = beta.create_content(topic, additional_context)
    return content
