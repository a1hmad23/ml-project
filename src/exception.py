import traceback  # Provides utilities to extract, format, and print stack traces
from logger import logging

def format_error(error: Exception) -> str:
    """
    Return a concise, human-readable error message with filename, line, and message.
    Parameters:
    error : Exception
        The actual exception object (e.g., from 'except Exception as e').

    Returns:
    str
        A short error message containing:
        - The type of error (e.g. ZeroDivisionError)
        - The file name where it occurred
        - The line number
        - The actual error message
    """
    # error.__traceback__ → gets the traceback object stored inside the exception.
    # traceback.extract_tb(...) → converts that traceback into a list of readable frames (each frame = one step in the call stack).
    # [-1] → picks the last frame, which is where the error actually happened.
    # The result (tb) contains info like:
        # tb.filename → file name
        # tb.lineno → line number
        # tb.name → function name
        # tb.line → the line of code that failed
    tb = traceback.extract_tb(error.__traceback__)[-1]

    # Format and return a readable message that includes:
    # - Exception type name (e.g. 'ZeroDivisionError')
    # - File name (tb.filename)
    # - Line number (tb.lineno)
    # - Actual error message text (error)
    return f"{type(error).__name__} in {tb.filename} (line {tb.lineno}): {error}"

# Instead of raising generic Exception instances, we will raise instances of our CustomException class 
# for cleaner, more descriptive error handling.
class CustomException(Exception):
    def __init__(self, error: Exception):
        # Initialize the parent Exception class with the string form of the original error.
        # This ensures the built-in Exception behavior (like .args, traceback support)
        # still works if needed later.
        super().__init__(str(error))

        # Generate and store a detailed, formatted error message
        self.error_message = format_error(error)

    #overriding the parent __str__
    def __str__(self):
        return self.error_message

if __name__ == '__main__':
    try:
        a = 1/0
    except Exception as e:
        logging.info('Divide by Zero')
        raise CustomException(e)