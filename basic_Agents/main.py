# main.py - Basic command-line interface for the agent system
from tasks import analyze_position_task, generate_content_task

def main():
    # Main program loop
    while True:
        # Get user command
        user_input = input("Enter your request (or type 'exit' to quit): ").strip().lower()
        
        # Handle different commands
        if user_input == "exit":
            print("Exiting program.")
            break
        elif "analyze" in user_input:
            # Handle analysis request
            name = input("Enter the name for the report: ")
            context = input("Enter the data or context to analyze: ")
            result = analyze_position_task(name, context)
            print(result)
        elif "generate content" in user_input:
            # Handle content generation request
            topic = input("Enter the topic for content generation: ")
            result = generate_content_task(topic)
            print(result)
        else:
            print("Unrecognized command. Try 'analyze' or 'generate content'.")

if __name__ == "__main__":
    main()
