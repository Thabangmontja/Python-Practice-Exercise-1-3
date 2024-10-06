import logging

# Custom Exception
class ValueTooHighError(Exception):
    def __init__(self, message="Value is too high! Must be less than or equal to 100."):
        self.message = message
        super().__init__(self.message)

# Configure logging
logging.basicConfig(filename='custom_exception_log.txt', level=logging.ERROR, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def check_value():
    try:
        num = float(input("Enter a number: "))
        
        if num > 100:
            raise ValueTooHighError(f"Input value {num} exceeds the limit of 100.")
        
        print(f"Your number {num} is valid!")
    
    except ValueTooHighError as e:
        logging.error(e)
        print(e)
    
    except ValueError:
        logging.error("Invalid input. Non-numeric value entered.")
        print("Error: Please enter a valid numeric value.")
    
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        print(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    check_value()
