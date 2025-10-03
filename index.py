import string

print("Welcome to Mad Libs!")

def get_user_input(prompt):
    while True:
        user_input = input(prompt).strip()
        punctuation = string.punctuation 

        try:
            # Check for alphabetic input
            if user_input.isalpha():
                return user_input

            # Check for numbers
            elif user_input.isdigit():
                print("Input cannot be a number. Please try again.")

            # Check for special characters
            elif any(char in punctuation for char in user_input):
                print("Input cannot contain special characters. Please try again.")

            # Check for empty input
            else:
                print("Input cannot be empty. Please try again.")

        except ValueError:
            print("Invalid input. Please try again.")
        

def mad_lib():
    #Inputs
    adj1 = get_user_input("Enter an adjective: ")
    noun1 = get_user_input("Enter a noun: ")
    noun2 = get_user_input("Enter another noun: ")
    adj2 = get_user_input("Enter an adjective: ")
    noun2 = get_user_input("Enter a noun: ")

    plural_noun = get_user_input("Enter a plural noun: ")
    adjective3 = get_user_input("Enter an adjective: ")
    person = get_user_input("Enter a person's name: ")
    vehicle = get_user_input("Enter a type of vehicle: ")
    verb1 = get_user_input("Enter a verb: ")

    place2 = get_user_input("Enter a place: ")
    verb2 = get_user_input("Enter another verb: ")
    food = get_user_input("Enter a type of food: ")
    adjective4 = get_user_input("Enter an adjective: ")

    story = (f"Last summer, my {adj1} {noun1} and I decided to go on a trip to {noun2}."
             f"\nWe packed a {adj2} {noun2} and brought lots of {plural_noun} for the journey."
             f"\nOn the way, we met a {adjective3} {person} who offered us a ride on their {vehicle}."
             f"\nIt was going fine until the vehicle started to {verb1} uncontrollably! Finally, we arrived at {place2}," 
             f"\nwhere everyone was busy {verb2} and eating {food}. It was the most {adjective4} trip of my life!"
            )
    return story

print(mad_lib())