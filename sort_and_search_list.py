'''
Program: basic_list.py
Author: Joshua M McGinley
Last Date Modified: 10/12/2022

You can make a new file sort_and_search_list.py. For this assignment, you can hard-code a list you pass to the
sort_list() and search_list() in your main. For extra credit, you and use the previous assignment get_list()
Write sort_list() to sort the list

    What is the return statement?
        Write a comment explaining why you included return OR
        Write a comment explaining why your code has no return statement.

Write search_list()

    What is the return statement?
        Write a comment explaining why you included return OR
        Write a comment explaining why your code has no return statement.

Write main

    call sort_list()
    call search_list()
'''

list = [1, 75, 3, 4, 5, 54, 7, 8, 9, 10, 48, 8, 27, 36, 21, 15, 11, 7, 3, 5, 0, ]

def sort_list(list):
    list.sort()
    return list  #This return statement returns the sorted list so that it is printed.

def search_list(list):
    find = int(input('What are you looking for: '))
    return list.index(find)  #This returns the index of 'find' concerning where it is located in the list

if __name__ == '__main__':
    print(sort_list(list))
    print(search_list(list))
