s1=int(input("enter marks of telugu:"))
s2=int(input("enter marks of hindi:"))
s3=int(input("enter marks of english:"))
s4=int(input("enter marks of maths:"))
s5=int(input("enter marks of science:"))
s6=int(input("enter marks of social:"))
a=s1+s2+s3+s4+s5+s6
print("your score is {} out of 600".format(a))
b=(a/600)*100
print("your percent is {}".format(b))
if b>=90:
  print("grade A")
elif b>=80 and b<=89:
  print("grade B")
elif b>=70 and b<=79:
  print("grade c")
elif b>=60 and b<=69:
  print("grade d")
elif b>=50 and b<=59:
  print("grade e")
else:
  print("fail")
