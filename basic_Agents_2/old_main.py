# main.py
from tasks import analyze_position_task, generate_content_task
from datetime import datetime
import os

def save_session(outputs):
    # Create session_output directory if it doesn't exist
    if not os.path.exists("session_output"):
        os.makedirs("session_output")
    
    current_time = datetime.now()
    filename = current_time.strftime("session_output/session_output[%d%b%y][%H:%M].md")
    
    with open(filename, "w") as file:
        file.write("# Session Outputs\n\n")
        for output in outputs:
            file.write(output + "\n\n")
    print(f"Outputs saved to '{filename}'")

def main():
    outputs = []

    while True:
        user_input = input("Enter your request (or type 'save' to save current session, or type 'exit' to quit): ").strip().lower()
        
        if user_input == "exit":
            save_session(outputs)
            print("Exiting program.")
            break
        elif user_input == "save":
            save_session(outputs)
        elif "analyze" in user_input:
            tone = input("Choose response type (quick/detailed): ").strip().lower() or "quick"
            name = input("Enter the name for the report: ")
            context = input("Enter the data or context to analyze: ")
            result = analyze_position_task(name, context, tone=tone)
            outputs.append(result)
            print(result)
        elif "generate content" in user_input:
            tone = input("Choose response type (quick/detailed): ").strip().lower() or "quick"
            topic = input("Enter the topic for content generation: ")
            result = generate_content_task(topic, tone=tone)
            outputs.append(result)
            print(result)
        else:
            print("Unrecognized command. Try 'analyze', 'generate content', 'save', or 'exit'.")

if __name__ == "__main__":
    main()
