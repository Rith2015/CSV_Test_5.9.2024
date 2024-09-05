from enum import Enum
from functions import *
class SELECTION(Enum):
    HIGHEST_PRICE=1 #Select this to show the highest price for a diamond
    AVERAGE_PRICE=2 #Select this to show the avarege price for a diamond
    HOW_MANY_IDEAL_DIAMONDS=3 #Select this to show how many diamnods from type ideal there are
    HOW_MANY_COLORS=4 #Select this to show how many diffrent color for diamonds there are and what are they
    MEDIAN_CRET=5 #Select this to finding the median of diamonds from type premium
    AVERAGE_CARAT_FOR_CUT=6 #Select this to show the average carat for every cut type 
    AVERAGE_PRICE_FOR_EVERY_COLOR=7 #Select this to show the average price for a diamond in every color group
    EXIT=8
def menu():
    for item in SELECTION:print(f"{item.name}-{item.value}")
    return SELECTION(int(input("Your Selection: ")))
def main():
    data=load_data()
    while True:
        userselection=menu()
        if userselection==SELECTION.HIGHEST_PRICE:
            highest_price(data)
        if userselection==SELECTION.AVERAGE_PRICE:
            average_price(data)
        if userselection==SELECTION.HOW_MANY_IDEAL_DIAMONDS:
            ideal_diamond(data)
        if userselection==SELECTION.HOW_MANY_COLORS:
            color_types(data)
        if userselection==SELECTION.MEDIAN_CRET:
            median_premium(data)
        if userselection==SELECTION.AVERAGE_CARAT_FOR_CUT:
            average_carat_for_cut(data)
        if userselection==SELECTION.AVERAGE_PRICE_FOR_EVERY_COLOR:
            average_price_for_color(data)
        elif userselection==SELECTION.EXIT:
            Exit_app()
if __name__=="__main__":
    main()