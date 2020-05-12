
name=input("Enter student's name:")

s1= ['Ahmad', 18, 17, 19.5, 8, 25]
s2= ['Sami', 20, 20, 19, 9, 28]
s3= ['Faris', 14.5, 16, 13, 7, 23]

s11=[18, 17, 19 , 5, 8, 25]
sum1= sum(s11)
s22=[ 20, 20, 19, 9, 28]
sum2= sum(s22)
s33=[ 14.5, 16, 13, 7, 23]
sum3= sum(s33)

if name =='Ahmad':
    print('Ahmad '+str(sum1))
elif name=='Sami':
    print('Sami '+str(sum2))
elif name =='Faris':
    print('Faris '+str(sum3))
else:
    print('Student is not recorded '+str(0))  
