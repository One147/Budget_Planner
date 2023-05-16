import pandas as pd
import MoneyLogging
from matplotlib import pyplot as plt

def date_prompt():
    
    while True:
        
        target_date = input("What date would you like to start at?: ")
        
        date_list = list(target_date)
    
        if len(date_list) != 10:
            print("Sorry, wrong date format")
    
    
        elif date_list[2] and date_list[5] != "/":
            print("Sorry, wrong date format")
    
    
        else:
            return target_date


def main():

    #getting target date
    target_date = date_prompt()
    
    #read and convert the date section of the csv file to a pandas accesible date
    moneylog = pd.read_csv("MoneyTracking.csv", dayfirst = True)

    #filtering csv from target date to current date
    filt = (moneylog["Date"] >= target_date)
    moneylog = moneylog.loc[filt]
    
    
    #find total spent
    total_spent = moneylog["Amount"].sum()
    
    #total spent on needs
    
    needs_filt = (moneylog["Category"] == "N")
    needs = moneylog.loc[needs_filt]
    total_needs = needs["Amount"].sum()
    
    
    #total spent on wants
    
    wants_filt = (moneylog["Category"] == "W")
    wants = moneylog.loc[wants_filt]
    total_wants = wants["Amount"].sum()
    
    
    #total spent on debt
    
    debt_filt = (moneylog["Category"] == "D")
    debts = moneylog.loc[debt_filt]
    total_debts = debts["Amount"].sum()
    
    
    #total spent on savings
    
    savings_filt = (moneylog["Category"] == "S")
    savings = moneylog.loc[savings_filt]
    total_savings = savings["Amount"].sum()
    
    #pie chart generation
    plt.style.use("fivethirtyeight")
    
    slices = [total_needs, total_wants, total_debts, total_savings]
    labels = ["Needs", "Wants", "Debts", "Savings"]
    
    plt.pie(slices, labels = labels, autopct="%1.1f%%",)
    
    plt.title(f"Spending Allocation Since {target_date}")
    plt.tight_layout()
    plt.show()
    