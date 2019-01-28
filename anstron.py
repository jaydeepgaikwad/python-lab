#name:gaikwad jaydeep 
#div:p          #batch:1

'Python programme to cheak whether number is anstron number' 

x1=input('Enter a number')
x=int(x1)
q1=int(x1[0]**3)
q2=int(x1[1]**3)
q3=int(x1[2]**3)
z=q1+q2+q3
if x==z:
   print("amstron")
else:
   print("not amstron")
