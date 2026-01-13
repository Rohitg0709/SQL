marks = int(input("Enter your marks: "))
if marks < 0 or marks > 100 :
    print ("Invalid marks")

elif marks < 35 : 
    print ("Fail")
elif marks < 60 :
    print ("Pass")
elif marks < 75 :
    print ("Good")
else :
    print ("Excellent")