#!/usr/bin/env python3
# Author ID: [seneca_id]

def add(number1, number2):
    """Adds two numbers, returns the result, or an error message if invalid."""
    try:
        return int(number1) + int(number2)
    except ValueError:
        return "error: could not add numbers"

def read_file(filename):
    """Reads a file, returns a list of lines, or an error message if the file is not found."""
    try:
        with open(filename, 'r') as f:
            return f.readlines()
    except FileNotFoundError:
        return "error: could not read file"

if __name__ == '__main__':
    print(add(10,5))                        
    print(add('10',5))                      
    print(add('abc',5))                     
    print(read_file('seneca2.txt'))         
    print(read_file('file10000.txt'))       
