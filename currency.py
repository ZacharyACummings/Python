yuan = (int(input("What do you have left in yuan?: ")))
yen = (int(input("What do you have left in yen?: ")))
won = (int(input("What do you have left in won?: ")))
total = (yuan*0.15) + (yen*0.0075) + (won*0.00078)
print("Your total in USD is:")
print(total)