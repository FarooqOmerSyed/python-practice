def main():
    user_data = {}  # Initialize an empty dictionary to store user data
    count = 0  # Initialize a counter for displaying data

    while True:
        command = input("Enter 'start' to input data, 'stop' to stop, or 'show' to display stored data: ")

        if command == "start":
            name = input("Enter your name: ")
            age = input("Enter your age: ")
            email = input("Enter your email: ")

            # Store user data in the dictionary
            user_data[name] = {"age": age, "email": email}
            print(f"Data for {name} stored successfully!")

        elif command == "stop":
            print("Stopping data input. You can start again later.")
            break

        elif command == "show":
            print("Stored user data:")
            for name, data in user_data.items():
                print(f"{count}. {name}, {data['age']}, {data['email']}")
                count += 1

        else:
            print("Invalid command. Please enter 'start', 'stop', or 'show'.")

if __name__ == "__main__":
    main()
