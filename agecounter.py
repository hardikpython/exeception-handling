while True:
    age_input = input("Enter your age: ")

    if age_input.isdigit():
        age = int(age_input)
        if 0 < age < 120:  # optional range check
            print(f"Thank you! Your age is {age}.")
            break
        else:
            print("Please enter a realistic age between 1 and 119.")
    else:
        print("Invalid input! Please enter a whole number (no letters, decimals, or symbols).")
