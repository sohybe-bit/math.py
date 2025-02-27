import random

def generate_equation():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    num3 = random.randint(1, 100)
    return f"{num1} - {num2} + {num3} = "

def main():
    print("Math Worksheet Generator (Press Ctrl+C to stop)")
    try:
        while True:
            print(generate_equation())
    except KeyboardInterrupt:
        print("\nProgram exited.")

if __name__ == "__main__":
    main()