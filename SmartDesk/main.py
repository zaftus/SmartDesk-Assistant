from .chatbot import Chatbot
from .skill_manager import SkillManager

def main():
    bot = Chatbot()
    skills = SkillManager()

    print("Welcome to SmartDesk Assistant! Type 'exit' to quit.")

    while True:
        user_input = input("> ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        # Run skills if applicable
        if "organize" in user_input or "reminder" in user_input:
            if "organize" in user_input:
                path = input("Enter folder path to organize: ")
                print(skills.run_skill("organize", {"path": path}))
            if "reminder" in user_input:
                msg = input("Enter reminder message: ")
                time = input("Enter reminder time: ")
                print(skills.run_skill("reminder", {"message": msg, "time": time}))
        else:
            print("Bot:", bot.get_response(user_input))

if __name__ == "__main__":
    main()
