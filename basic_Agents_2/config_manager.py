import yaml
import os
from typing import Dict, Any

class ConfigManager:
    def __init__(self, config_file: str = 'agent_configs.yaml'):
        self.config_file = config_file
        self.configs = self.load_configs()

    def load_configs(self) -> Dict[str, Any]:
        """Load configurations from YAML file."""
        if not os.path.exists(self.config_file):
            raise FileNotFoundError(f"Configuration file {self.config_file} not found!")
        with open(self.config_file, 'r') as file:
            return yaml.safe_load(file)

    def save_configs(self) -> None:
        """Save current configurations to YAML file."""
        with open(self.config_file, 'w') as file:
            yaml.dump(self.configs, file, default_flow_style=False)

    def get_agent_config(self, agent_type: str) -> Dict[str, Any]:
        """Get configuration for a specific agent."""
        return self.configs.get(agent_type, {})

    def update_agent_config(self, agent_type: str, new_config: Dict[str, Any]) -> None:
        """Update configuration for a specific agent."""
        if agent_type in self.configs:
            self.configs[agent_type].update(new_config)
            self.save_configs()

if __name__ == "__main__":
    # Example usage
    config_manager = ConfigManager()
    
    # Get alpha agent config
    alpha_config = config_manager.get_agent_config('alpha')
    print("Alpha Agent Configuration:")
    print(yaml.dump(alpha_config))
