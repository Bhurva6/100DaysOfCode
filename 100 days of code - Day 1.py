# 100 days of code - Day 2
print("Welcome to the tip calculator!")
total=float(input("What was the total bill? "))
percent=int(input("What percentage tip would you like to give? "))
people= int(input("How many people to split the bill? "))
percenttip= percent/100
totaltip= total * percenttip 
totalbill= total + totaltip 
billperperson= totalbill/people
final=round(billperperson,2)
print(f"Each person should pay: ${final}" )