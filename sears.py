bill_dim=0.11*0.001 #bill dimensions in meters
sears_h=442 #sears tower height
num_bill=1  #bills counter
day=1   #days counter
while bill_dim*num_bill<sears_h:
    print(day, num_bill, bill_dim*num_bill)
    num_bill=2*num_bill
    day=day+1
print('No. of days: ', day)
print('No. of bills used: ', num_bill)
print('Height of stack of bills: ', bill_dim*num_bill)    