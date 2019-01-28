#name:Gaikwad jaydeep laxman
#div:p         #batch;1
''' a programme to convert  second into hours,minuits,seconds'''

x=int(input('enter time in seconds'))
q1=x//86400
r1=x%86400
q2=r1//3600
r2=r1%3600
q3=r2//60
r3=r2%60
q4=r3//1
r4=r3%1
print(q1,q2,q3,q4)
print('the number of days',q1,'number of hours',q2,'number of minuits',q3,'number of second',q4,)
