def add_numbers(a, b):
    return a + b

def validate_message(message):
    return len(message.strip()) > 0

def greeting(name):
    return f"Salut, {name}!"

if __name__ == "__main__":
    print(greeting("GitHub"))