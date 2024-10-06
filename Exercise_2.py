import os
import logging

# Configure logging
logging.basicConfig(filename='file_errors_log.txt', level=logging.ERROR, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def read_file():
    try:
        file_path = input("Enter the path of the file you want to read: ")
        
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"File '{file_path}' does not exist.")
        
        with open(file_path, 'r') as file:
            content = file.read()
            print("File Content:\n", content)
    
    except FileNotFoundError as fnf_error:
        logging.error(fnf_error)
        print(f"Error: {fnf_error}")
    
    except PermissionError:
        logging.error(f"Permission denied for file: {file_path}")
        print("Error: You don't have permission to access this file.")
    
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        print(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    read_file()
