''' 
Module: Wheyland Pythoni - Building Better Modules

This module provides a simple, reusable foundation for analytics projects. 
Code should be reusable.
A good byline could be used in every Python analytics project that is done.

Process:

Code is not written from top to bottom; instead, it is written from the outside, in.
Here's what a first draft of utils_case.py might look like:

1. I start with this docstring at the very beginning.
   I use it to clarify the purpose of my Python file and organize my thoughts.
   
2. I'll declare a global variable for my byline string and just set it to some simple text.

3. I'll declare a main() function for my module. When I run this script, I can use main() to test my byline.

4. I'll add the boilerplate conditional execution code so I only run the main() function when 
   this script is executed directly (but not when I import it into another file).

Testing was completed in an online interpreter (https://www.online-python.com/)
'''


''' In the fourth interation, basic statistics are introduced using Python. 
These include min(), max(), and the statistics module.
'''


####################################################
# Modules Import - included at the top of the script
####################################################

# Modules provide additional tools and functions not included in the basic installation.
# The following modules will be imported:
#  'statistics' - provides tools to calculate pieces like averages
# You can use ctrl+F to find where it is used
# Look for examples like statistics.mean() and statistics.stdev()

import statistics


####################################################
# Declare global variables (keep byline at end)
# This information will be used fo ra smarter byline
####################################################


# Boolean to indicate whether the company has international clients
has_international_clients: bool = True

# Integer variable for the number of years in operation
years_in_operation: int = 144

# List of strings representing the skills offered by the company
skills_offered: list = ["Data Analysis", "Machine Learning", "Harmonic Balancing", "Modular Consulting", "Equilibrium Evaluation"]

# List of floats representing individual client satisfaction scores
client_satisfaction_scores: list = [4.5, 4.4, 4.7, 4.2, 4.9, 5.0, 4.4, 4.4, 3.9, 4.7, 4.8]



####################################################
# Calculate Basic Statistics
# Completed BEFORE we declare the byline
# Ensures values have been calculated & are ready for byline
####################################################


# Basic Stats using built-in functions min(), max() and statistics module functions mean() and stdev()
min_score: float = min(client_satisfaction_scores)
max_score: float = max(client_satisfaction_scores)
mean_score: float = statistics.mean(client_satisfaction_scores)
stdev_score: float = statistics.stdev(client_satisfaction_scores)





####################################################
# Declare a global variable named byline
# Make it an f-string to show our information
####################################################

byline: str = f"""
----------------------------------------------------
Wheyland Pythoni: Building Better Modules
----------------------------------------------------
Has International Clients:   {has_international_clients}
Years in Operation:          {years_in_operation}
Skills Offered:              {skills_offered}
Client Satisfaction Scores:  {client_satisfaction_scores}
"""


####################################################
# Define the get_byline function
####################################################

def get_byline() -> str:
   # return a byline for Wheyland Pythoni
   return byline

####################################################
# Define a main() function for this module.
####################################################

# Create a function named main.
# A function is a block of code that performs a specific task.
# This function will simply print the byline to the console.
# Add a type hint to indicate that this function doesn't return anything when called 
# (that is, it has a Python type of None).
# It doesn't need any additional information passed in, 
# so there's nothing needed inside the parentheses.
# Everything afer the colon (:) must be indented (usually 4 spaces)

def main() -> None:
    '''Print the byline to the console when this function is called.'''
    print(get_byline())

####################################################
# Conditional Execution - Only call main() when executing this module as a script.
####################################################

if __name__ == '__main__':
    main()
