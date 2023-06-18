import csv 
import time
import os.path



#slow typing effect

def slowtype(string):
    
    broken_string = list(string)
    
    for i in range(len(broken_string)):
        print(broken_string[i], end = "")
        time.sleep(0.01)
    

def get_date():
        
        while True:
            date_input = input("Date (DD/MM/YYY): \n")

            date_list = list(date_input)
    
            if len(date_list) != 10:
                print("Sorry, wrong date format\n")
    
            elif date_list[2] and date_list[5] != "/":
                print("Sorry, wrong date format\n")
    
            else:
                break
        
        
        return date_input


def get_amount():
    amount_input = input("Amount (+ for expenses) \n")
    return amount_input
        
def get_category():
    categ = input("What category (N,W,D,S) ")
    return categ
    
def get_desc():
    desc = input("Description? ")
    return desc

def done_response():
    done_response = input("Thank you, would you like to input more data? (Y/N)\n")
    return done_response

def get_info():
    
    done = "Y"
    
    while done == "Y":
        
        date = get_date()
        amount = get_amount()
        category = get_category()
        description = get_desc()


        file_exists = os.path.isfile("MoneyTracking.csv")

    #append to the csv file this information in a new row
        with open ("MoneyTracking.csv" , "a" , newline = "") as csvfile:
        
            fieldnames = ["Date" , "Amount" , "Category" , "Desc"]
            
            thewriter = csv.DictWriter(csvfile, fieldnames = fieldnames)
            
            if not file_exists:
                thewriter.writeheader()
                
            thewriter.writerow({
                
                "Date" : date,
                "Amount" : amount,
                "Category" : category,
                "Desc" : description,
                
                
            })
        
        done = done_response()
            
        
    
        


def main():

    slowtype("Welcome to your money logger, please input the following information\n------------------------------\n")
    slowtype(f"Date (DD/MM/YYYY), Amout (only expenses as + no deposits), Category (Needs, Wants, Debt/Saving), Desc (One Word/Phrase)\n------------------------------\n")

    #get inputs on "date" , "amount" , "category" , "desc"

    while True:
        get_info()
        
        
        
