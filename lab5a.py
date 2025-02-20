#!/usr/bin/env python3

def read_file_string(file_name):
    """Takes a file name as a string, returns its entire contents as a single string."""
    try:
        with open(file_name, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return "Error: File not found"

def read_file_list(file_name):
    """Takes a file name as a string, returns its contents as a list of lines without new-line characters."""
    try:
        with open(file_name, 'r') as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        return "Error: File not found"

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))
