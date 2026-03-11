#Accessing a Global Variable

count =0
def increment ():
    global count #declare "count" as global
    count +=1
    print(f"count inside function :{count}")
 #call the function

increment()
increment()
 #access the global variable
 
print(f"count outside function :{count}")