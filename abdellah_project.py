"""
File: abdellah_project.py
Author: Abdellah Boudlal

Purpose:
    A minimal Python script to demonstrate:
    - Importing modules
    - Defining a main() function
    - Using logging
    - Conditional execution
"""

#####################################
# Imports
#####################################

from utils_logger import logger

#####################################
# Main Function
#####################################

def main() -> None:
    """
    Main entry point of the script.
    Logs a success message to confirm the setup works.
    """
    logger.info("Running main function successfully!")

#####################################
# Conditional Execution
#####################################

if __name__ == "__main__":
    main()
