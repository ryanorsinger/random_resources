def get_number_from_user():
    """
        Returns a number of the user's choosing. This implementation only handles letter and number input. Special characters throw an error.
    """

    # Obtain the user's input
    user_input = input("Please input a number.")

    # If the input ain't numeric, then prompt them again (and again and again, if necessary)
    while user_input.isalpha():
        print(f"The value inputted of: {user_input} is not a number. Please input a number.")

        # Obtain the user's input (again)
        user_input = input("Please input a number.")


        # At the end of the indentation, the flow of control goes back to check the condition.
        # If the user inputted a number, then the loop stops running

    # Converts the string version of the number in a string to a float.
    user_input = float(user_input)
    return user_input