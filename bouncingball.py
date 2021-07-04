h_ini=100   #Initial height of ball drap
n=10    #Max no. of bounces
for i in range(n):
    h_ini=3*h_ini/5 #Bounce bank height after each bounce
    print(i+1, round(h_ini,4)) #Print nth bounce and its corresponding bounce height