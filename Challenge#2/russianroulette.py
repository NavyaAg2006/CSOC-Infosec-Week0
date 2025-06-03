import random
import sys
import time

def russian_roulette():
    bullet_position = random.randint(1, 6)
    print("The revolver has been loaded.")
    time.sleep(0.5)
    print("Spinning the chamber...")
    time.sleep(1.5)
    chamber = random.randint(1, 6)
    print(f"Chamber stopped at position {chamber}.")
    time.sleep(0.5)
    print("Pulling the trigger...")
    time.sleep(2)

    if chamber == bullet_position:
        print("\U0001F4A5 Bang! You're dead.")
        print("Game over!")
        sys.exit(0)
    else:
        print("😅 Click. You survived.")

while True:
    print("Welcome to Russian Roulette. Are you willing to risk your life for a win?")
    choice = input("Type 'play' to pull the trigger or 'quit' to exit: ").strip().lower()
    if choice == 'play':
        russian_roulette()
    elif choice == 'quit':
        print("Didn't have the courage huh...Goodbye!")
        break
    else:
        print("Invalid input. Please type 'play' or 'quit'.")
