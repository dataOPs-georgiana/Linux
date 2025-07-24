# main.py

def greet(name):
    """Greets the given name."""
    return f"Hello, {name}!"

if __name__ == "__main__":
    user_name = input("Enter your name: ")
    message = greet(user_name)
    print(message)
    print("This is your first Python script with Git!")
