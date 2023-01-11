#import files 
import os
import csv

budgetdata_csv= os.path.join("", "Resources", "budget_data.csv")


with open(budgetdata_csv,newline="") as csvfile:
    csvreader =csv.reader(csvfile,delimiter=",")

    csv_header=next(csvfile)
    


    Total=0
    Greatest_profit=0
    max_loss=0
    month_count=0
    average=0


    for row in csvreader:
        Total= Total + int(row[1])
        month_count += 1

        if int(row[1])> Greatest_profit:
            Greatest_profit=int(row[1])
            month_profit= str(row[0])

        if int(row[1]) < max_loss:
            max_loss= int(row[1])
            month_loss= str(row[0])


    outfile = open("Results.txt","w")
    outfile.write("financial analysis \n")
    outfile.write("Total profit is: $ " + str(Total) + "\n")
    outfile.write("Total Months is:" + str(month_count) + "\n")
    outfile.write("Greatest increase in profit: $" + str(Greatest_profit) + str (month_profit) + "\n")
    outfile.write("Greatest decrease in profit: $" + str(max_loss) + str (month_loss) + "\n")
    outfile.close()
    
#print for verification
print("financial analysis \n")
print("Total profit is: $ " + str(Total) + "\n")
print("Total Months is:" + str(month_count) + "\n")
print("Greatest increase in profit: $" + str(Greatest_profit) + str(month_profit)+ "\n")
print("Greatest decrease in profit: $" + str(max_loss) + str(month_loss)+ "\n")
print("Average change ")
    



 


