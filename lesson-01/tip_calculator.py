bill_amount = float(input("Enter Bill Amount : "))
tip_percent = float(input("Enter Tip Percentage : "))
no_of_people = int(input("Enter No of  people : "))
tip_amount = bill_amount * tip_percent / 100
total_amount = tip_amount + bill_amount
print(f'Tip Amount : {tip_amount : .2f}')
print(f'Total Amount : {total_amount : ,.2f}')
print(f'Each person pays {total_amount / no_of_people : ,.2f}')
