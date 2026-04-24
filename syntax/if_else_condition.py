
maths = int (input("Enter your maths marks : "))
Science = int (input("Enter your science marks : "))
sst = int (input("Enter your sst marks : "))
Hindi = int (input("Enter your hindi marks : "))
Punjabi = int (input("Enter your punjabi marks : "))
English = int(input("Enter your english marks : "))
sum=maths+Science+sst+Hindi+Punjabi+English
average = sum/(80*6)
percentage = average*100
print(percentage)

if percentage >= 80:
    print("YOU DID GOOD")

elif percentage >= 70:
    print("Good but Scope of improvement")

elif percentage >= 60:
    print("Average")

elif percentage >= 50:
    print("Work hard")
    
elif percentage >= 33:
    print("Just Pass")

else :
    print("Fail")


