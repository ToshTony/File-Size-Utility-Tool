# File Size Utility Tool

This utility tool calculates the size of files given their file paths. It supports calculating file sizes in different units (bytes, KB, MB, GB) and can handle multiple file paths entered by the user.

## Features

- Calculate file size in bytes, KB, MB, or GB.
- Handle multiple file paths entered by the user.
- Informative error handling for file not found scenarios.

## Requirements

- Python 3.x
- Modules used: `os`

## How to Use

1. **Clone the repository:**

git clone https://github.com/ToshTony/File-Size-Utility-Tool.git


cd file-size-utility



2. **Run the program:**
- Open a terminal or command prompt.
- Navigate to the directory where the `file-size-utility.py` file is located.
- Run the following command:
  ```
  python file-size-utility.py
  ```

3. **Input file paths:**
- Enter file paths separated by spaces when prompted.
- Example: `/path/to/file1.txt /path/to/file2.pdf /path/to/directory`

4. **Output:**
- The program will display the size of each file in bytes, KB, MB, or GB.

5. **Error Handling:**
- If a file path is incorrect or the file is not found, the program will notify you with an error message.


## Usefulness

### How This Tool Can Be Useful:

- **Disk Space Management**: Quickly assess how much disk space individual files or directories occupy, aiding in efficient storage management.

- **File Transfer Planning**: Estimate transfer times and plan file transfers more effectively by knowing file sizes beforehand.

- **Performance Optimization**: Identify large files impacting application performance or storage usage for optimization efforts.

- **Compliance and Auditing**: Facilitate compliance reporting and auditing by tracking and reporting file sizes and storage usage.

- **Troubleshooting**: Quickly identify large or unexpected file sizes that may be causing disk space errors or performance issues.

### Educational and Practical Applications:

- **Learning Tool**: Provides a practical example for learning about file handling and basic Python programming techniques.

- **Automation**: Easily integrate into scripts or automated workflows to monitor file sizes and automate reporting tasks.


## Example

Enter file paths separated by spaces: /path/to/file1.txt /path/to/file2.pdf /path/to/directory

File size of '/path/to/file1.txt': 1024 bytes

File size of '/path/to/file2.pdf': 1.23 MB

File not found: /path/to/directory



## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

