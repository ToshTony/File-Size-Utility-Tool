# Enhanced file size utility tool in Python


import os

def calculate_file_size(file_path):
    """ Function to calculate the file size of a given file path """
    try:
        size_bytes = os.path.getsize(file_path)
        return size_bytes
    except FileNotFoundError:
        return None

def convert_bytes_to_human_readable(size_bytes):
    """ Function to convert bytes to human-readable format (KB, MB, GB) """
    if size_bytes < 1024:
        return f"{size_bytes} bytes"
    elif size_bytes < 1024 * 1024:
        return f"{size_bytes / 1024:.2f} KB"
    elif size_bytes < 1024 * 1024 * 1024:
        return f"{size_bytes / (1024 * 1024):.2f} MB"
    else:
        return f"{size_bytes / (1024 * 1024 * 1024):.2f} GB"

def main():
    file_paths = input("Enter file paths separated by spaces: ").split()
    
    for file_path in file_paths:
        file_size = calculate_file_size(file_path)
        if file_size is None:
            print(f"File not found: {file_path}")
        else:
            human_readable_size = convert_bytes_to_human_readable(file_size)
            print(f"File size of '{file_path}': {human_readable_size}")

if __name__ == "__main__":
    main()
