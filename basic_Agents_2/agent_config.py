"""
Configuration settings for different agents and their prompts.
This allows for easy modification of agent behaviors without changing the core code.
The configurations are now loaded from agent_configs.yaml using ConfigManager.
"""

from config_manager import ConfigManager

# Initialize the configuration manager
config_manager = ConfigManager()

# Load configurations from YAML file
AGENT_CONFIGS = config_manager.load_configs()

# Function to reload configurations (can be called when configs need to be refreshed)
def reload_configs():
    """Reload configurations from YAML file."""
    global AGENT_CONFIGS
    AGENT_CONFIGS = config_manager.load_configs()

# Function to update configurations (can be called to update specific agent configs)
def update_agent_config(agent_type: str, new_config: dict):
    """Update configuration for a specific agent and save to YAML."""
    config_manager.update_agent_config(agent_type, new_config)
    reload_configs()  # Reload to ensure AGENT_CONFIGS is up to date
