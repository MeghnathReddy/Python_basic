#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Gottfried Leibniz mathematical formula
def Gottfried_Leibeinz(x):
    count=1 #initialize the count
    #consider 3 variables 
    p=1
    q=1
    r=0
    input_Number=x #number of iterations
    
    while count<=input_Number:
        if(count%2) == 0:
            r=r-(p/q) #if the count is even we need to obtain a negative sign
            q+=2
        else:
            r=r+(p/q) #if count is odd we need to obtain a positive sign
            q+=2
        count+=1
    print("%.2f"%r)
    
# number of iterations to be calculated
print("Please enter the input Number: ")
entered_Value = input()
input_Number = int(entered_Value)

# Pass the parameters to our defined function
Gottfried_Leibeinz(x=input_Number)


# In[2]:


#Lexington School Ditsrict

#Basic salary which is an input taken from user
basic_Salary= float(input("Enter the basic salary of the teacher: "))

#Number of years of experience which is an input taken from user
experience=int(input("Enter the number of years of experience: "))

#% increase in salary each year
percentage_Increase=float(input("Enter the increase in percentage: "))

print("YearNo.\tSalary")

for i in range(1, experience+1):  
    print("%d\t%.2f" %(i, basic_Salary))
    basic_Salary = basic_Salary + (basic_Salary*percentage_Increase)/100


# In[3]:


#Lucky Sevens
import random

# To calculate the sum of the numbers on the 2 dice
def Sum(x,y):
    return x+y

# To check each time if money is greater than 1
def validate_Amount(amount):
    if amount < 1:
        return 0
    
def lucky_Pot():
  
    # If the user wants to continue the game
    while True:
        total_Amount = int(input("Enter the total amount you want to play with: "))      
        # call the function to validate_Amount for the initial check
        criteria = validate_Amount(total_Amount)
        if criteria==0:
            print("No amount to continue the game")
            break
        
        i=1 #To iterate to the loop initiate with a variable
        maximum_Profit=0 #To keep track of highest amount earned 
        
        iterate = str(i)
        final_Amount = str("${}".format(total_Amount)) #conversion to string
        print("Number of rolls"+"\t"+"  Win or loss"+"\t"+"Amount of money in the pot")
        print(  "\t"+iterate+"\t"+"     Put"+"\t""\t"+final_Amount)
      
       
        while total_Amount > 0:
            i+= 1
            iterate= str(i)
            x=random.randint(1,6) # 1st die
            y=random.randint(1,6) # 2nd die
            z = Sum(x,y)
            
            if z==7: # if the sum of two die is 7
                total_Amount+=4
                final_Amount=str("${}".format(total_Amount))
                print(  "\t"+iterate+"\t"+"     Win"+"\t""\t"+final_Amount)
            else:
                total_Amount -= 1
                final_Amount = str("${}".format(total_Amount))
                print(  "\t"+iterate+"\t"+"     Loss"+"\t""\t"+final_Amount)
          
            if maximum_Profit<total_Amount:
                maximum_Profit=total_Amount

        print("Money is lost after {} rolls of play".format(i))
        print("Maximum profit during the game is ${}".format(maximum_Profit))

        #If user wishes to continue the game
        game =(input("Do you wish to play again (y/n): "))
        if (game=='n')or(game=='N'):
            break;

lucky_Pot()


# In[5]:


#Payroll department
def main():
    
    name = input("Enter the file name: ") #Takes the input from the user
    open_Name = open(name) #Open the created file
    print("\n")
    print("lastname","\t","department","hoursworked","netPay") #To print the header names

    for line in open_Name:
        content = line.split() #Removes the spaces and stores the values in a list
        lastname = content[0] #To fetch the names of the Employee
        department=content[1] #To fetch the department of the Employee
        hoursworked = int(content[2]) #To fetch the hours worked by the Employee
        hourlywage = float(content[3]) #To fetch the hourly rate of the Employee     

        net_Pay = hourlywage*hoursworked  #Gives the net pay of each employee
        print(lastname,"\t",department,"\t",hoursworked,"\t",net_Pay)

    open_Name.close()
    
main()

