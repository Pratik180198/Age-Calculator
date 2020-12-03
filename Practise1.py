while True:
    age=input("Enter your current age or year of birth: ")
    try:
        input_age=int(age)
        current_year=2020
        convert_str = str(input_age)
        length_of_input_age = len(convert_str)
        if length_of_input_age > 4:
            print("Please enter proper year")
        elif input_age>current_year:
            print("You are not yet born.")
        elif input_age == 0 or input_age < 0:
            print("Please enter proper age")
        else:
            if length_of_input_age == 4:
                hundred_years=input_age+100
                actual_born_year = input_age
                if actual_born_year < 1900:
                    print("Your are seem to be the oldest person to alive.")
                    continue
                print("Your Born year is: ",actual_born_year)
                print(f"The year when you turned 100 years old will be {hundred_years}")
                particular_year = int(input("If you want to know your age at that particular year then enter the year: "))
                print(f"Your age at {particular_year} year will be", particular_year - actual_born_year)
            else:
                remaining_age=100-input_age
                hundred_years_old_age=current_year+remaining_age
                actual_born_year = current_year - input_age
                if actual_born_year < 1900:
                    print("Your are seem to be the oldest person to alive.")
                    continue
                print("Your Born year is: ", actual_born_year)
                print(f"The year when you turned 100 years old will be {hundred_years_old_age}")
                particular_year = int(input("If you want to know your age at that particular year then enter the year: "))
                print(f"Your age at {particular_year} year will be", particular_year - actual_born_year)
    except ValueError:
        print("Please enter only integer values!!!")

