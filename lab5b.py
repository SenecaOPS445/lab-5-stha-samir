#!/usr/bin/env python3
# Author ID: [seneca_id]

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

def append_file_string(file_name, string_of_lines):
    """Appends a string to the end of a file."""
    with open(file_name, 'a') as f:
        f.write(string_of_lines)

def write_file_list(file_name, list_of_lines):
    """Writes a list of lines to a file, each on a new line."""
    with open(file_name, 'w') as f:
        for line in list_of_lines:
            f.write(line + '\n')

def copy_file_add_line_numbers(file_name_read, file_name_write):
    """Reads data from the first file, writes it to the second file with line numbers."""
    try:
        with open(file_name_read, 'r') as f_read, open(file_name_write, 'w') as f_write:
            for index, line in enumerate(f_read, 1):
                f_write.write(f"{index}:{line}")
    except FileNotFoundError:
        print(f"Error: {file_name_read} not found")

if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']

    
    append_file_string(file1, string1)
    print(read_file_string(file1))  

    
    write_file_list(file2, list1)
    print(read_file_string(file2))  

    
    copy_file_add_line_numbers(file2, file3)
    print(read_file_string(file3))  
