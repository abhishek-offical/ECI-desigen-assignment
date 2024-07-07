# Create a program that takes user input to add multiple elements to an array, then prints the final array

def Createlist():
    # Initialize an empty array
    array = []

    while True:

        element = input("Enter an element to add to the array (or type 'done' to finish): ")

        if element.lower() == 'done':
            break

        array.append(element)

    # Print the final array
    print("The final array is:", array)

Createlist()