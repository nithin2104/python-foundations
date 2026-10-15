bill = float(input("Enter Bill Amount : "))
tip = int(input("Enter Tip Percentage : "))
no_of_people = int(input("Enter No of  people : "))
total_tip = ((tip / 100 ) * bill)
print(f'Tip Amount : {total_tip}')
print(f'Total Amount : {total_tip + bill}')
print(f'Each person pays {(total_tip + bill) / no_of_people :.2f}')



