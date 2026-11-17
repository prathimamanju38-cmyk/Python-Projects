def ac_controller():
    ac_on = False
    current_temp = 28
    target_temp = 22

    while True:
        print("------AC Controller------")
        print("1. Check state of AC")
        print("2. AC (On/Off)")
        print("3. Set temperature")
        print("4. Exit")

        choice = input("Select option from 1-4: ").strip()

        if choice == '1':
            status = "ON" if ac_on else "OFF"
            print(f"AC is {status} | Room Temp: {current_temp}°C | Target: {target_temp}°C")

            if ac_on and current_temp > target_temp:
                current_temp -= 1
                print("AC is cooling the room.")
            elif ac_on and current_temp <= target_temp:
                print("Target temperature reached.")

        elif choice == '2':
            ac_on = not ac_on
            new_status = "ON" if ac_on else "OFF"
            print(f"AC turned {new_status}.")

        elif choice == '3':
            try:
                new_target = int(input("Enter new target temperature (°C): "))
                if 16 <= new_target <= 40:
                    target_temp = new_target
                    print(f"Target temperature set to {target_temp}°C.")
                else:
                    print("Error: Valid range is between 16°C and 40°C.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        elif choice == '4':
            print("Shutting down the control system. Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")


ac_controller()
    