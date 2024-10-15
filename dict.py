# dict
1) The program takes a dictionary and checks if a given key exists in a dictionary or not. 
Problem Solution:
1. Declare and initialize a dictionary to have some key-value pairs.{'A':1,'B':2,'C':3}
2. Take a key from the user and store it in a variable.
3. Using an if statement and the in operator, check if the key is present in the dictionary using the dictionary.keys() method.
4. If it is present, print the value of the key.
5. If it isn’t present, display that the key isn’t present in the dictionary.
6. Exit.
Sample Input :
Enter key to check : A
Sample Output :
Key is present and value of the key is: 1

d={"A":1,"B":2,"C":3}
print("Enter key to check:")
key=input()
if key in d.keys():
    print("Key is present and value of the key is:",d[key])
else:
    print("Key isn't present!")

    2)
The program takes two dictionaries and concatenates them into one dictionary. 
Problem Solution:
1. Declare and initialize two dictionaries with some key-value pairs d1={'A':1,'B':2} d2={'C':3}
2. Use the update() function to add the key-value pair from the second dictionary to the first dictionary.
3. Print the final dictionary.
4. Exit.
Sample Output:
Concatenated dictionary is: {'A': 1, 'B': 2, 'C': 3}

a={"A":1,"B":2}
b={"C":3}
a.update(b)
print("Concatenated dictionary is:",a)

3) 
The program takes a number from the user and generates a dictionary that contains numbers (between 1 and n) in the form (x,x*x). 
Problem Solution:
1. Take a number from the user and store it in a separate variable.
2. Declare a dictionary and using dictionary comprehension initialize it to values keeping the number between 1 to n as the key and the square of the number as their values.
3. Print the final dictionary.
4. Exit.
Sample I/O:
5
Sample O/P:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

def generate_square_dictionary():
    n = int(input("Enter a number: "))
    square_dict = {x: x * x for x in range(1, n + 1)}
    print(square_dict)
generate_square_dictionary()

4) The program takes a key-value pair and adds it to the dictionary. 
Problem Solution:
1. Take a key-value pair from the user and store it in separate variables.
2. Declare a dictionary and initialize it to an empty dictionary.
3. Use the update() function to add the key-value pair to the dictionary.
4. Print the final dictionary.
5. Exit.
Sample I/O:
12
34
Sample o/p:
{12: 34}

def add_key_value_to_dictionary():
    key = input("Enter the key: ")
    value = input("Enter the value: ")
    my_dict = {}
    my_dict.update({key: value})
    print(my_dict)
add_key_value_to_dictionary()

5) The program takes a dictionary and prints the sum of all the items in the dictionary.
Problem Solution:
1. Declare and initialize the n number of dictionary values from the user.
2. Find the sum of all the values in the dictionary.
3. Print the total sum.
4. Exit.
Sample Input:
3
100
540
239
Sample Output :
879


def sum_of_dictionary_values():
    n = int(input("Enter the number of items: "))
    my_dict = {}
    for i in range(n):
        value = int(input(f"Enter value {i + 1}: "))
        my_dict[i + 1] = value  # Use index as the key
    total_sum = sum(my_dict.values())
    print(total_sum)
sum_of_dictionary_values()




