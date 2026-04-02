# expenses=[10.50, 8, 5, 15, 20, 5, 3]
expenses =[]
# sum=0
# for x in expenses:
#     sum=sum+x
number_of_expenses=int(input("Enter number of expenses:"))
for x in range(number_of_expenses):
    expenses.append(float(input("Enter an expense:")))
total=sum(expenses)
# print("You spent: $",sum, sep="")
print("You spent: $",total, sep="")
range(1,7,1) # start, stop, step
