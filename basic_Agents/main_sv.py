# main_sv.py - Enhanced version with session saving functionality
from tasks import analyze_position_task, generate_content_task
from datetime import datetime

def save_session(outputs):
    """Save session outputs to a markdown file with timestamp"""
    # Generate filename with date and time
    current_time = datetime.now()
    filename = current_time.strftime("session_output[%d%b%y][%H:%M].md")
    
    # Write outputs to markdown file
    with open(filename, "w") as file:
        file.write("# Session Outputs\n\n")
        for output in outputs:
            file.write(output + "\n\n")
    print(f"Outputs saved to '{filename}'")

def main():
    # Initialize list to store session outputs
    outputs = []

    # Main program loop
    while True:
        # Get user command
        user_input = input("Enter your request (or type 'save' to save current session, or type 'exit' to quit): ").strip().lower()
        
        # Handle different commands
        if user_input == "exit":
            save_session(outputs)  # Save before exit
            print("Exiting program.")
            break
        elif user_input == "save":
            save_session(outputs)  # Save without exiting
        elif "analyze" in user_input:
            # Handle analysis request
            name = input("Enter the name for the report: ")
            context = input("Enter the data or context to analyze: ")
            result = analyze_position_task(name, context)
            outputs.append(f"**Report for {name}:**\n\n{result}")
            print(result)
        elif "generate content" in user_input:
            # Handle content generation request
            topic = input("Enter the topic for content generation: ")
            result = generate_content_task(topic)
            outputs.append(f"**Generated Content for Topic '{topic}':**\n\n{result}")
            print(result)
        else:
            print("Unrecognized command. Try 'analyze', 'generate content', 'save', or 'exit'.")

if __name__ == "__main__":
    main()
