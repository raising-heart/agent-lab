# tasks.py - Defines high-level tasks that utilize the agents

from agents import AgentAlpha, AgentBeta

def analyze_position_task(name, context):
    # Create analyzer agent and get analysis report
    alpha = AgentAlpha()
    report = alpha.analyze_data(context)
    return f"Report for {name}: {report}"

def generate_content_task(topic):
    # Create content generator agent and get content
    beta = AgentBeta()
    content = beta.create_content(topic)
    return content
