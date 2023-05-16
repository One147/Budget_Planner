
import MoneyLogging
import os.path
import pandas as pd
from matplotlib import pyplot as plt
import csv

file_exists = os.path.isfile("Static_Transactions.csv")

def get_response():
    MoneyLogging.slowtype("Hello, would you like to\n1-Add/Remove Expected Transactions\n2-View expected spending/free money?\n")
    response = input()
    return response

def add_tran():
    while True:
        MoneyLogging.slowtype("What category is this expected transaction ((N)eeds (W)ants (S)avings (D)ebt (I)ncome)?\n")
        category = input()
        
        MoneyLogging.slowtype("What type of transaction is this (Savings/Debt, Food, Shelter, Transportaion, Giving, Health, Personal)?\n")
        Type = input()
        
        MoneyLogging.slowtype("Whats the description of the transaction?\n")
        desc = input()
        
        MoneyLogging.slowtype("Whats the amount ($/week)\n")
        amount = input()
        
        MoneyLogging.slowtype("Thank you\n")
        
        
        with open ("Static_Transactions.csv" , "a" , newline = "") as csvfile:
            fieldnames = ["Category" , "Type" , "Desc" , "Amount"]
            
            thewriter = csv.DictWriter(csvfile, fieldnames = fieldnames)
            
            if not file_exists:
                thewriter.writeheader()
            
            thewriter.writerow({
                "Category" : category,
                "Type" : Type,
                "Desc" : desc,
                "Amount" : amount,
            })
        
        MoneyLogging.slowtype("Thank you, would like to\n1- input another\n2- Finished\n")
        response = input()
        if int(response) == 1:
            pass
        if int(response) == 2:
            break
        else:
            MoneyLogging.slowtype("Sorry, incorrect response\n")

def remove_tran():
    MoneyLogging.slowtype("What transaction would you like to remove (index)\n")
    
    df = pd.read_csv("Static_Transactions.csv")
    
    pd.set_option("display.max_rows", None)
    pd.set_option("display.max_columns,", None)
    pd.set_option("display.width", None)
    pd.set_option("display.max_colwidth", None)
    
    print(df)
    while True:
        target_index = input()
        try:
            df.drop(df.index[target_index], axis = 0)
        except:
            print("Sorry, invalid index\n")
        else:
            MoneyLogging.slowtype("Thank you, sucessfully removed. Would you like to\n1- remove another\n2- finished\n")
            response = input()
            if int(response) == 1:
                pass
            if int(response) == 2:
                break
            else:
                print("Sorry, invalid response\n")
      
def add_remove():
    #would you like to add or remove an expected transaction
    
    MoneyLogging.slowtype("Would you like to\n1- Add transaction\n2- Remove transaction\n")
    add_rem_response = input()
        
        #if add, append to csv "amount" "category, "type", "desc"
    if int(add_rem_response) == 1:
        add_tran()
       
    if int(add_rem_response) == 2:
        remove_tran()

def project_category(total_income):
    income = total_income
    
    df = pd.read_csv("Static_Transactions.csv")
    
    #get value for $ on N
    
    needs_filt = (df["Category"] == "N")
    needs = df.loc[needs_filt]
    total_needs = needs["Amount"].sum()
    
    #get value for $ on W
    
    wants_filt = (df["Category"] == "W")
    wants = df.loc[wants_filt]
    total_wants = wants["Amount"].sum()
    
    #get value for $ on D
    
    debt_filt = (df["Category"] == "D")
    debt = df.loc[debt_filt]
    total_debt = debt["Amount"].sum()
    
    #get value for $ on S
    
    savings_filt = (df["Category"] == "S")
    savings = df.loc[savings_filt]
    total_savings = savings["Amount"].sum()
    
    #get value for $ on taxes
    taxes = income*0.4
    
    #get free money value
    
    expected_free_money = income - total_needs - total_wants - total_debt - total_savings - taxes
    
    #display pie chart with these values based on percentages 
    
    plt.style.use("fivethrityeight")
    
    slices = [total_needs, total_wants, total_debt, total_savings, taxes, expected_free_money]
    labels = ["Needs" , "Wants" , "Debt" , "Savings" , "Taxes" , "Expected Free Money"]
    
    plt.pie(slices, labels=labels, autopct="%1.1f%%",)
    
    plt.title(f"Projected Spending Based on Cateogry of Static/Confirmed Expenses/Income")
    plt.tight_layout()
    plt.show()

def project_type(total_income):
    income = total_income
    
    df = pd.read_csv("Static_Transactions.csv")
    
    #get value for $ on Savings/Debt
    
    savings_debt_filt = (df["Type"] == "Savings/Debt")
    savings_debt = df.loc[savings_debt_filt]
    total_savings_debt = savings_debt["Amount"].sum()
    
    #get value for $ Food
    
    food_filt = (df["Type"] == "Food")
    food = df.loc[food_filt]
    total_food = food["Amount"].sum()
    
    #get value for $ on Shelter
    
    shelter_filt = (df["Type"] == "Shelter")
    shelter = df.loc[shelter_filt]
    total_shelter = shelter["Amount"].sum()
    
    #get value for $ on Transportation
    
    transpo_filt = (df["Type"] == "Transportation")
    transpo = df.loc[transpo_filt]
    total_transpo = transpo["Amount"].sum()
    
    #get value for $ on Giving
    
    giving_filt = (df["Type"] == "Giving")
    giving = df.loc[giving_filt]
    total_giving = giving["Amount"].sum()
    
    #get value for $ on Health
    
    health_filt = (df["Type"] == "Health")
    health = df.loc[health_filt]
    total_health = health["Amount"].sum()
    
    #get value for $ on Personal
    
    personal_filt = (df["Type"] == "Personal")
    personal = df.loc[personal_filt]
    total_personal = personal["Amount"].sum()
    
    
    #taxes
    tax = income*0.4
    
    #get free money value
    
    expected_free_money = income - total_savings_debt - total_food - total_shelter - total_transpo - total_giving - total_health - total_personal - tax
    
    #display pie chart with these values based on percentages 
    
    plt.style.use("fivethrityeight")
    
    slices = [total_savings_debt, total_food, total_shelter, total_transpo, total_giving, total_health, total_personal, tax, expected_free_money]
    labels = ["Savings/Debt", "Food" , "Shelther", "Transportation" , "Giving" , "Health" , "Personal" , "Tax" , "Expected Free Money"]
    
    plt.pie(slices, labels=labels, autopct="%1.1f%%",)
    
    plt.title(f"Projected Spending Based on Types of Static/Confirmed Expenses")
    plt.tight_layout()
    plt.show()
    

def view_projections():
    
    df = pd.read_csv("Static_Transactions.csv")
    
    income_filt = df["Category" == "I"]
    income = df.loc[income_filt]
    total_income = income["Amount"].sum()
    
    #would you rather display via category and free money or type and free money
    
    MoneyLogging.slowtype("Would you like to view projected spending/free money based on\n1- Category\n2- Type\n")
    while True:
        response = input()
        if int(response) == 1:
            project_category(total_income)
            break
        if int(response) == 2:
            project_type(total_income)
            break
        else:
            print("Sorry, invalid response\n")    
        
def main():
    #Would you like to append a static transaction or view expected spending?
    while True:
        response = get_response()
        
        if int(response) == 1:
            add_remove()
            break
            
        if int(response) == 2:
            #View expected spending/free money
            view_projections()
            break
        
        else:
            MoneyLogging.slowtype("Sorry, incorrect response\n")
            response = get_response()
            
