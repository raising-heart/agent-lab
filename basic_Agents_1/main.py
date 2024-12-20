# Enhanced main program with session saving and custom roles
from tasks import analyze_position_task, generate_content_task
from datetime import datetime
import os

def save_session(outputs):
    """Save session outputs to a markdown file"""
    output_dir = "session_output"
    os.makedirs(output_dir, exist_ok=True)
    
    current_time = datetime.now()
    filename = current_time.strftime("session_output[%d%b%y][%H:%M].md")
    filepath = os.path.join(output_dir, filename)
    
    with open(filepath, "w") as file:
        file.write("# Session Outputs\n\n")
        file.write("## Generated with Enhanced AI Agents\n\n")
        for output in outputs:
            file.write(output + "\n\n---\n\n")
    print(f"\nOutputs saved to '{filepath}'")

def get_optional_inputs():
    """Get custom role and additional context from user"""
    print("\nOptional inputs (press Enter to skip):")
    role = input("Enter custom role: ").strip()
    context = input("Enter additional context: ").strip()
    return role or None, context or None

def display_menu():
    """Display available commands"""
    print("\nAvailable commands:")
    print("1. analyze     - Analyze data with custom role")
    print("2. generate    - Generate content with custom role")
    print("3. save       - Save current session")
    print("4. exit       - Save and exit program")
    print("-------------------------------------------")

def main():
    outputs = []  # Store session outputs
    
    print("\nWelcome to Enhanced AI Agents!")
    print("Each session will be automatically saved with timestamps.")
    
    while True:
        display_menu()
        user_input = input("\nEnter your request: ").strip().lower()
        
        if user_input == "exit":
            save_session(outputs)
            print("Session saved. Exiting program.")
            break
            
        elif user_input == "save":
            save_session(outputs)
            
        elif "analyze" in user_input:
            name = input("Enter the name for the report: ")
            data = input("Enter the data or context to analyze: ")
            role, context = get_optional_inputs()
            
            result = analyze_position_task(name, data, role, context)
            
            # Format and store output
            output = f"## Analysis Report: {name}\n"
            if role:
                output += f"*Analyzed by: {role}*\n\n"
            output += f"### Results\n{result}"
            outputs.append(output)
            
            print("\nAnalysis Result:")
            print(result)
            
        elif "generate" in user_input:
            topic = input("Enter the topic for content generation: ")
            role, context = get_optional_inputs()
            
            result = generate_content_task(topic, role, context)
            
            # Format and store output
            output = f"## Generated Content: {topic}\n"
            if role:
                output += f"*Generated by: {role}*\n\n"
            output += f"### Content\n{result}"
            outputs.append(output)
            
            print("\nGenerated Content:")
            print(result)
            
        else:
            print("Unrecognized command. Please try again.")

if __name__ == "__main__":
    main()
