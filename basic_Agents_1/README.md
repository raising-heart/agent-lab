# Enhanced AI Agents

A flexible and powerful AI agent system that leverages OpenAI's GPT-4o for data analysis and content generation. This system features customizable roles and contexts for specialized tasks, with automatic session saving functionality.

## Features

- **Dual Agent System**
  - AgentAlpha: Specialized in data analysis
  - AgentBeta: Specialized in content generation
- **Customizable Roles**
- **Additional Context Support**
- **Automatic Session Saving**
- **Markdown-formatted Outputs**

## Setup

1. **Environment Setup**
   ```bash
   # Create a .env file and add your OpenAI API key
   OPENAI_API_KEY=your_api_key_here
   ```

2. **Dependencies**
   ```bash
   pip install openai python-dotenv
   ```

## Usage

Run the program:
```bash
python main.py
```

### Available Commands

1. `analyze` - Analyze data with custom role
2. `generate` - Generate content with custom role
3. `save` - Save current session
4. `exit` - Save and exit program

### Using Custom Roles

Custom roles allow you to specify the AI's expertise for a particular task. Examples:

#### For Analysis:
- Financial Analyst: "You are a financial analyst specializing in cryptocurrency markets"
- Medical Researcher: "You are a medical researcher analyzing clinical trial data"
- Sports Statistician: "You are a sports statistician analyzing player performance"

```bash
Enter custom role: You are a financial analyst specializing in cryptocurrency markets
```

#### For Content Generation:
- Technical Writer: "You are a technical writer creating documentation"
- Marketing Copywriter: "You are a marketing copywriter focusing on engaging product descriptions"
- Journalist: "You are a journalist writing news articles"

```bash
Enter custom role: You are a technical writer specializing in API documentation
```

### Using Additional Context

Additional context provides specific instructions or parameters for the task. Examples:

#### For Analysis:
```bash
Enter additional context: Focus on environmental impact and sustainability metrics. Include data from the last 3 months only.
```

#### For Content Generation:
```bash
Enter additional context: Target audience is beginners. Keep language simple. Include practical examples. Maximum length 500 words.
```

### Example Session

1. **Analyzing Data**
   ```bash
   Enter your request: analyze
   Enter the name for the report: Crypto Market Analysis
   Enter the data or context to analyze: BTC price movements in Q4 2023
   Enter custom role: You are a cryptocurrency market analyst
   Enter additional context: Focus on institutional adoption and regulatory impacts
   ```

2. **Generating Content**
   ```bash
   Enter your request: generate
   Enter the topic for content generation: AI Ethics
   Enter custom role: You are an AI ethics researcher
   Enter additional context: Target audience is policymakers. Include recent case studies.
   ```

### Output Files

Session outputs are automatically saved in the `session_output` directory with timestamps:
```
session_output/session_output[29Nov23][14:30].md
```

Each output includes:
- Timestamp
- Task type (Analysis/Content Generation)
- Custom role used (if any)
- Additional context (if any)
- Results

## Project Structure

- `main.py` - Main program with CLI interface
- `agents.py` - Agent definitions and OpenAI integration
- `tasks.py` - Task wrapper functions
- `config.py` - Configuration and API key management
- `session_output/` - Directory for saved session outputs

## Tips for Best Results

1. **Custom Roles**
   - Be specific about expertise areas
   - Include relevant qualifications or experience
   - Specify industry or domain focus

2. **Additional Context**
   - Set clear constraints (length, format, etc.)
   - Specify target audience
   - Include relevant time periods or data ranges
   - Mention specific aspects to focus on or ignore

## License

MIT License
