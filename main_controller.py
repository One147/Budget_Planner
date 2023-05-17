import MoneyLogging
import PieChart
import Expected_Transactions
import pandas

         
def get_response():
    MoneyLogging.slowtype("What would you like to do today?\n1- Money Logging\n2- Previous Spending Pie Chart\n3- View/Analyze Static/Confirmed Expenses and Income\n")
    response = input()
    return int(response)
def main():
    MoneyLogging.slowtype("Good afternoon, welcome to your budget tracker!\n")
    
    #getting response and running money log, pie chart, or future log depending on input
    
    while True:
        response = get_response()
        
        if int(response) == 1:
            MoneyLogging.main()
            
            MoneyLogging.slowtype("Is that all you would like to do today?\n1-Yes\n2-No\n")
            continue_response = input()
        
            if int(continue_response) == 1:
                MoneyLogging.slowtype("Thank you, exiting now\n")
                break
            if int(continue_response) == 2:
                pass
        
        if int(response) == 2:
            PieChart.main()
            
            MoneyLogging.slowtype("Is that all you would like to do today?\n1-Yes\n2-No\n")
            continue_response = input()
        
            if int(continue_response) == 1:
                MoneyLogging.slowtype("Thank you, exiting now\n")
                break
            if int(continue_response) == 2:
                pass
        
        if int(response) == 3:
            Expected_Transactions.main()
            
            MoneyLogging.slowtype("Is that all you would like to do today?\n1-Yes\n2-No\n")
            continue_response = input()
        
            if int(continue_response) == 1:
                MoneyLogging.slowtype("Thank you, exiting now\n")
                break
            if int(continue_response) == 2:
                pass
        
        else:
            MoneyLogging.slowtype("Sorry, wrong format \n")
        
main()