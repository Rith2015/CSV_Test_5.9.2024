# Diamonds Analysis Tool
    This Python project analyzes a dataset of diamonds. It provides functionalities to extract insights on various attributes of diamonds, such as price, cut, color, and carat.

## Requirements
    Python 3.x
    pandas library
## Setup
    Install Python: Make sure Python 3.x is installed on your system.

    Install pandas: Install the pandas library using pip:

    pip install pandas
    Dataset: Ensure that the dataset file named diamonds.csv is in the same directory as the script.
## Functions
    load_data()
    Loads the diamonds dataset from diamonds.csv.

### highest_price(df)
    Finds and prints the highest price for a diamond in the dataset.
### average_price(df)
    Calculates and prints the average price of diamonds in the dataset.
### ideal_diamond(df)
    Counts and prints the number of diamonds classified as 'Ideal' in the dataset.
### color_types(df)
    Counts and prints the number of unique colors for diamonds and lists all unique colors.
### median_premium(df)
    Calculates and prints the median carat weight for diamonds classified as 'Premium' in the dataset.
### average_carat_for_cut(df)
    Calculates and prints the average carat weight for each cut type of diamonds in the dataset.
### average_price_for_color(df)
    Calculates and prints the average price of diamonds for each color type.
### Exit_app()
    Clears the terminal screen and exits the application.
## Running the Application
    To run the application, execute the app.py script:
    python app.py
    Follow the prompts to select the desired functionality. The available options are:

    1. Show the highest price for a diamond.
    2. Show the average price for a diamond.
    3. Show how many diamonds are of type 'Ideal'.
    4.Show how many different colors of diamonds there are and list them.
    5. Find the median carat weight for diamonds of type 'Premium'.
    6. Show the average carat weight for each cut type.
    7. Show the average price for diamonds of each color type.
    8. Exit the application.
 ## Notes
    Ensure that the diamonds.csv file is properly formatted and available in the same directory as the script.
    The terminal screen clearing function (Exit_app()) might not work as expected on all operating systems.
