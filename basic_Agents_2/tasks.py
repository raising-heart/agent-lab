# tasks.py
from agents import AgentAlpha, AgentBeta

def analyze_position_task(name, context, tone="quick", additional_context=None):
    """Analyze data using AgentAlpha."""
    try:
        alpha = AgentAlpha()
        report = alpha.analyze_data(context, tone=tone, context=additional_context)
        return f"**Report for {name}:**\n\n{report}"
    except Exception as e:
        return f"Error in analysis: {str(e)}"

def generate_content_task(topic, tone="quick", context=None):
    """Generate content using AgentBeta."""
    try:
        beta = AgentBeta()
        content = beta.create_content(topic, tone=tone, context=context)
        return f"**Generated Content for Topic '{topic}':**\n\n{content}"
    except Exception as e:
        return f"Error in content generation: {str(e)}"
