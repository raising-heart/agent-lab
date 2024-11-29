# Basic Agents

A Python-based project implementing specialized AI agents using OpenAI's GPT-4o for data analysis and content generation tasks.

## Features

- Two specialized AI agents:
  - **AgentAlpha**: Focused on data analysis tasks
  - **AgentBeta**: Specialized in content generation tasks
- Session saving functionality
- Command-line interface
- Automatic output saving to markdown files
- Environment-based configuration

## Prerequisites

### Environment Setup

This project uses Conda for environment management and requires the following Python packages:
- openai
- python-dotenv

### Configuration

1. Create a `.env` file in the project root
2. Add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## Project Structure

- `agents.py`: Core agent implementations
  - Initializes OpenAI client
  - Implements AgentAlpha and AgentBeta with specific system prompts
  
- `tasks.py`: High-level task functions
  - `analyze_position_task`: Report generation using AgentAlpha
  - `generate_content_task`: Content creation using AgentBeta

- `config.py`: Environment configuration
  - Manages OpenAI API key
  - Handles environment variable loading

- `main.py`: Basic CLI interface
  - Handles user input
  - Provides basic analysis and content generation functionality
  - Simple exit command

- `main_sv.py`: Enhanced CLI with session saving
  - All features from main.py
  - Automatic output saving with timestamps
  - Manual save command
  - Auto-save on exit

## Installation

1. Create a new Conda environment:
   ```bash
   conda create --name basic_Agents
   conda activate basic_Agents
   ```

2. Install required packages:
   ```bash
   pip install openai python-dotenv
   ```

3. Set up your environment variables in `.env`

## Usage

1. Activate the Conda environment:
   ```bash
   conda activate basic_Agents
   ```

2. Run the basic interface:
   ```bash
   python main.py
   ```

   Or run the version with session saving:
   ```bash
   python main_sv.py
   ```

## Features

- Data Analysis (AgentAlpha)
  - Generate analytical reports
  - Process position-related data

- Content Generation (AgentBeta)
  - Create various types of content
  - Customizable output formats

- Session Management (main_sv.py)
  - Automatic saving of outputs
  - Timestamped markdown files
  - Manual save option
