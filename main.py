def main():
    calculator = input("Enter the operation you want to perform (e.g., 2 + 2): ")
    try:
        result = eval(calculator)
        print(f"The result of {calculator} is: {result}")
    except Exception as e:
        print(f"An error occurred: {e}")

main()