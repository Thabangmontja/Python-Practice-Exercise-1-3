import logging

# Configure logging
logging.basicConfig(filename='error_log.txt', level=logging.ERROR, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def divide_numbers():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        # Perform division
        result = num1 / num2
        print(f"The result of {num1} / {num2} is: {result}")
    
    except ZeroDivisionError:
        logging.error("Attempted to divide by zero.")
        print("Error: Division by zero is not allowed. Please try again.")
    
    except ValueError:
        logging.error("Invalid input. Non-numeric value entered.")
        print("Error: Please enter valid numeric values.")
        
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        print(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    divide_numbers()
