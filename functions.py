import pandas as pd
import os
filename="diamonds.csv"
df=pd.read_csv
# load data from diamonds.csv file
def load_data():
    try:
        return df(filename)
    except FileNotFoundError:
        return[]

# finds the biggest price for a diamond
def highest_price(df):
    try:
        if 'price' in df.columns:
            high_price = df['price'].max()
            print(f"Biggest price for a diamond is {high_price}")
            return high_price
    except:
        return []
# return the average price of a diamond
def average_price(df):
    try:
        if 'price' in df.columns:
            average= df['price'].mean()
            print(f"The average price of a diamond: {average:.2f}")
            return average
    except:
        return []
#check how many rows has ideal in them and returns the number of how many rows has it
def ideal_diamond(df):
    try:
        if 'cut' in df.columns:
            ideal_count = df[df['cut'] == 'Ideal'].shape[0]
            print(f"Number of ideal diamonds is : {ideal_count}")
            return ideal_count
    except:
        return []
#count in color colums how many unique color rows there are
def color_types(df):
    try:
        if  'color' in df.columns:
            unique_colors = df['color'].unique()
            num_colors = len(unique_colors)
            print(f'There are {num_colors} different colors for diamonds and they are: ')
            for color in unique_colors:
                print(color)
    except:
        return []

#prints the median of carat of diamonds in the premium rows
def median_premium(df):
    try:
       if 'cut' in df.columns:
            premium_count = df[df['cut'] == 'Premium']
            median=premium_count['carat'].median()
            print(f"The median of carat premium diamonds is : {median}")
            return median
    except:
        return []
#print what is the average number of carat is for each cut type
def average_carat_for_cut(df):
    try:
           if 'cut' in df.columns:
            average_carat = df.groupby('cut')['carat'].mean() 
            print("Average carat for each cut type is:")
            for cut, carat in average_carat.items():
                print(f"{cut}: {carat:.2f}")
    except:
        return []
##print what is the average price for a diamonds for each color type
def average_price_for_color(df):
    try:
        if 'color' in df.columns:
            average_price_for_color = df.groupby('color')['price'].mean() 
            print("Average price for each color type is:")
            for color, price in average_price_for_color.items():
                print(f"{color}: {price:.2f}")
    except:
        return []
#exit the currnt app and cleans terminal screen
def Exit_app():
    os.system('cls' if os.name == 'nt'else 'clear')
    exit()