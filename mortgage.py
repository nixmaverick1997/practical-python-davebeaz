principal= 500000.0 #principal amount
ir=0.05 #interest rate
payment=2684.11
extra=1000 #If extra 1000$ per month is added during the first 12 months 
total_paid=0.0
extra_payment_start_mth=61
extra_payment_end_mth=108
i=0
while principal>0:
    if i>extra_payment_start_mth and i<extra_payment_end_mth:
        principal=principal*(1+ir/12)-payment-extra
        i=i+1
        total_paid=total_paid+payment+extra
        if principal>0:
            print(i," ",total_paid," ",principal)
    else:
        principal=principal*(1+ir/12)-payment
        i=i+1
        total_paid=total_paid+payment
        if principal>0:
            print(i," ",total_paid," ",principal)
