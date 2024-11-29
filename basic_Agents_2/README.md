# AI Agent System for Action Movie Analysis

A sophisticated AI agent system specialized in action movie analysis and content generation, featuring configurable agents, YAML-based configuration management, and a user-friendly interface.

## System Architecture

### Core Components and Their Relationships

1. **Configuration Management Layer**
   - `agent_configs.yaml`: Stores all agent configurations
     - Roles and goals for each agent
     - Prompt templates for different response types
     - Easily modifiable without changing code
   
   - `config_manager.py`: Manages configuration loading and updates
     - Loads configurations from YAML
     - Provides methods to update and save configurations
     - Ensures configuration consistency

   - `agent_config.py`: Bridge between YAML and agents
     - Uses ConfigManager to load configurations
     - Provides AGENT_CONFIGS to other components
     - Includes functions for runtime config updates

2. **Agent Layer**
   - `agents.py`: Core agent implementations
     - `BaseAgent`: Common functionality for all agents
       - Handles OpenAI API interactions
       - Manages prompt formatting
       - Processes configurations
     
     - `AgentAlpha`: Data Analysis Specialist
       - Analyzes movie-related data
       - Supports quick/detailed analysis modes
       - Handles additional context for analysis
     
     - `AgentBeta`: Content Generation Specialist
       - Generates movie-related content
       - Supports quick/detailed generation modes
       - Processes additional context for content

3. **Task Management Layer**
   - `tasks.py`: High-level task implementations
     - `analyze_position_task`: Manages analysis workflows
       - Creates AgentAlpha instances
       - Formats analysis results
       - Handles error cases
     
     - `generate_content_task`: Manages content generation
       - Creates AgentBeta instances
       - Formats generated content
       - Processes errors gracefully

4. **User Interface Layer**
   - `main.py`: Command-line interface
     - Provides user interaction
     - Handles command processing
     - Manages session outputs
     - Implements error handling

### Data Flow

```
User Input (main.py)
    ↓
Task Processing (tasks.py)
    ↓
Agent Execution (agents.py)
    ↓
Configuration Loading (agent_config.py → config_manager.py → agent_configs.yaml)
    ↓
OpenAI API Interaction
    ↓
Response Processing
    ↓
User Output
```

## Setup and Usage

1. **Environment Setup**
   ```bash
   # Create a .env file with your OpenAI API key
   OPENAI_API_KEY=your_api_key_here
   ```

2. **Dependencies**
   ```bash
   pip install openai python-dotenv pyyaml
   ```

3. **Running the System**
   ```bash
   python main.py
   ```

## Available Commands

1. **analyze**: Use AgentAlpha for analysis
   - Response type: quick/detailed
   - Report name
   - Data/Context to analyze
   - Additional context (optional)

2. **generate**: Use AgentBeta for content generation
   - Response type: quick/detailed
   - Topic
   - Additional context (optional)

3. **help**: Display command information

4. **save**: Save current session

5. **exit**: Save and quit

## Configuration

Modify `agent_configs.yaml` to:
- Change agent roles and goals
- Update prompt templates
- Adjust response types
- Add new configurations

## Session Management

- Sessions are automatically saved with timestamps
- Output is stored in markdown format
- Located in the `session_output` directory

## Legacy Files

The system includes some legacy files for reference:
- `old_main.py`: Previous version of the interface
- `old_agents.py`: Earlier agent implementations

These files are kept for historical reference but are not part of the active system.

## Error Handling

The system implements comprehensive error handling:
- Input validation
- API error management
- Configuration error handling
- Graceful error recovery

## Future Improvements

1. Add unit tests for configuration management
2. Implement more sophisticated prompt engineering
3. Add support for batch processing
4. Enhance session management capabilities
