bill_amount = float(input("Enter Bill Amount : "))
tip_percent = float(input("Enter Tip Percentage : "))
num_people = int(input("Enter No of  people : "))
if num_people < 1 :
    print("Number of people must be greater than or equal 1")
else:
    tip_amount = bill_amount * tip_percent / 100
    total_amount = tip_amount + bill_amount
    print(f'Tip Amount : {tip_amount:.2f}')
    print(f'Total Amount : {total_amount:,.2f}')
    print(f'Each person pays {total_amount / num_people:,.2f}')
