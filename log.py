import logging

# Configure logging to output messages to the terminal
logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(message)s')

def log_function_call(func):
    def decorated(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        return result
    return decorated

@log_function_call
def my_function(a, b):
    return a + b
my_function(1, 2)