"""
Functions necessary for running a virtual cookie shop.
See README.md for instructions.
Do not run this file directly.  Rather, run main.py instead.
"""

def bake_cookies(filepath):
  """
  Opens up the CSV data file from the path specified as an argument.
  - Each line in the file, except the first, is assumed to contain comma-separated information about one cookie.
  - Creates a dictionary with the data from each line. 
  - Adds each dictionary to a list of all cookies that is returned.

  :param filepath: The path to the data file.
  :returns: A list of all cookie data, where each cookie is represented as a dictionary.
  """
  # write your code for this function below here.
  

def welcome():
  """
  Prints a welcome message to the customer in the format:

    Welcome to the Python Cookie Shop!
    We feed each according to their need.  

  """
  # write your code for this function below this line


def display_cookies(cookies):
  """
  Prints a list of all cookies in the shop to the user.
  - If doing the extra credit version, ask the user for their dietary restrictions first, and only print those cookies that are suitable for the customer.

  :param cookies: a list of all cookies in the shop, where each cookie is represented as a dictionary.
  """
  # write your code for this function below this line


def get_cookie_from_dict(id, cookies):
  """
  Finds the cookie that matches the given id from the full list of cookies.

  :param id: the id of the cookie to look for
  :param cookies: a list of all cookies in the shop, where each cookie is represented as a dictionary.
  :returns: the matching cookie, as a dictionary
  """
  # write your code for this function below this line


def solicit_quantity(id, cookies):
  """
  Asks the user how many of the given cookie they would like to order.
  - Validates the response.
  - Uses the get_cookie_from_dict function to get the full information about the cookie whose id is passed as an argument, including its title and price.
  - Displays the subtotal for the given quantity of this cookie, formatted to two decimal places.
  - Follows the format (with sample responses from the user):

      My favorite! How many Animal Cupcakes would you like? 5 
      Your subtotal for 5 Animal Cupcake is $4.95.

  :param id: the id of the cookie to ask about
  :param cookies: a list of all cookies in the shop, where each cookie is represented as a dictionary.
  :returns: The quantity the user entered, as an integer.
  """
  # write your code for this function below this line


def solicit_order(cookies):
  """
  Takes the complete order from the customer.
  - Asks over-and-over again for the user to enter the id of a cookie they want to order until they enter 'finished', 'done', 'quit', or 'exit'.
  - Validates the id the user enters.
  - For every id the user enters, determines the quantity they want by calling the solicit_quantity function.
  - Places the id and quantity of each cookie the user wants into a dictionary with the format 
      {'id': 5, 'quantity': 10}
  - Returns a list of all sub-orders, in the format:
      [ 
        {'id': 5, 'quantity': 10}, 
        {'id': 1, 'quantity': 3} 
      ]

  :returns: A list of the ids and quantities of each cookies the user wants to order.
  """
  # write your code for this function below this line



def display_order_total(order, cookies):
  """
  Prints a summary of the user's complete order.
  - Includes a breakdown of the title and quantity of each cookie the user ordereed.
  - Includes the total cost of the complete order, formatted to two decimal places.
  - Follows the format:

      Thank you for your order. You have ordered:

      -8 Animal Cupcake
      -1 Basboosa Semolina Cake

      Your total is $11.91.
      Please pay with Bitcoin before picking-up.

      Thank you!
      -The Python Cookie Shop Robot.
  
  """
  # write your code for this function below this line


def run_shop(cookies):
  """
  Executes the cookie shop program, following requirements in the README.md file.
  - This function definition is given to you.
  - Do not modify it!

  :param cookies: A list of all cookies in the shop, where each cookie is represented as a dictionary.
  """
  # write your code for this function below here.
  welcome()
  display_cookies(cookies)
  order = solicit_order(cookies)
  display_order_total(order, cookies)