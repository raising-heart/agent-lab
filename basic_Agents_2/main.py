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

def display_help():
    """Display detailed help information about available commands."""
    print("\nAvailable Commands:")
    print("1. analyze")
    print("   - Analyze data with customizable response type")
    print("   - Options:")
    print("     * response type: quick/detailed")
    print("     * name: name for the report")
    print("     * context: data or context to analyze")
    print("\n2. generate")
    print("   - Generate content with customizable response type")
    print("   - Options:")
    print("     * response type: quick/detailed")
    print("     * topic: topic for content generation")
    print("     * context: additional context (optional)")
    print("\n3. save")
    print("   - Save current session to a file")
    print("\n4. help")
    print("   - Display this help message")
    print("\n5. exit")
    print("   - Save and exit program")
    print("\nExample commands:")
    print("- analyze")
    print("- generate")
    print("- save")
    print("- help")
    print("- exit")

def main():
    outputs = []
    print("\nWelcome to the Agent System!")
    print("Type 'help' to see available commands")

    while True:
        print("\n" + "="*50)
        user_input = input("Enter command (analyze/generate/save/help/exit): ").strip().lower()
        
        if user_input == "exit":
            save_session(outputs)
            print("Saving session and exiting program.")
            break
            
        elif user_input == "save":
            save_session(outputs)
            
        elif user_input == "help":
            display_help()
            
        elif user_input == "analyze":
            print("\nAnalysis Options:")
            try:
                tone = input("Response type (quick/detailed) [default: quick]: ").strip().lower() or "quick"
                if tone not in ["quick", "detailed"]:
                    print("Error: Response type must be either 'quick' or 'detailed'. Using default: quick")
                    tone = "quick"
                
                name = input("Report name: ").strip()
                if not name:
                    print("Error: Report name is required for analysis.")
                    continue
                
                if name.lower() in ["exit", "quit"]:
                    print("Use 'exit' command at the main prompt to exit the program.")
                    continue
                
                context = input("Data/Context to analyze: ").strip()
                if not context:
                    print("Error: Context is required for analysis.")
                    continue
                
                if context.lower() in ["exit", "quit"]:
                    print("Use 'exit' command at the main prompt to exit the program.")
                    continue
                
                additional_context = input("Additional context (optional): ").strip()
                if additional_context.lower() in ["exit", "quit"]:
                    print("Use 'exit' command at the main prompt to exit the program.")
                    continue
                
                result = analyze_position_task(name, context, tone=tone, additional_context=additional_context if additional_context else None)
                outputs.append(result)
                print("\nAnalysis Result:")
                print(result)
            except Exception as e:
                print(f"Error during analysis: {str(e)}")
                
        elif user_input == "generate":
            print("\nGeneration Options:")
            try:
                tone = input("Response type (quick/detailed) [default: quick]: ").strip().lower() or "quick"
                if tone not in ["quick", "detailed"]:
                    print("Error: Response type must be either 'quick' or 'detailed'. Using default: quick")
                    tone = "quick"
                
                topic = input("Topic: ").strip()
                if not topic:
                    print("Error: Topic is required for content generation.")
                    continue
                
                if topic.lower() in ["exit", "quit"]:
                    print("Use 'exit' command at the main prompt to exit the program.")
                    continue
                
                context = input("Additional context (optional): ").strip()
                if context.lower() in ["exit", "quit"]:
                    print("Use 'exit' command at the main prompt to exit the program.")
                    continue
                
                result = generate_content_task(topic, tone=tone, context=context if context else None)
                outputs.append(result)
                print("\nGenerated Content:")
                print(result)
            except Exception as e:
                print(f"Error during content generation: {str(e)}")
                
        else:
            print("Unrecognized command. Type 'help' to see available commands.")

if __name__ == "__main__":
    main()
