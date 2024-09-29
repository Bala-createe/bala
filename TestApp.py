#Need to add serial number in the before entering inputs
#If name age address are exact same then say duplicate entry print existing serial number

#Need to store the dict output means all the added values to txt file before closing
#If data already exist in the text file then that also to be considred for next run
#Add a function to print existing data as table

print("Welcome to data entry App")
mydict={}
keyval=1
while True:
    print(f'SL No: {keyval}')
    name=input("Enter Name: ")
    age=input("Enter Age: ")
    address=input("Enter Address: ")
    #Add this values to diction
    temp={"Name":name,"Age":age,"Address":address}
    if str(temp) in str(mydict):
        dupind=str(mydict)[str(mydict).index(str(temp))-6:str(mydict).index(str(temp))].split("'")[1]
        print(f"This User Name: {name}, Age{age}, Address:{address} already found in SL No: {dupind}")
        continue
    mydict[str(keyval)]={"Name":name,"Age":age,"Address":address}
    x=input("Do you want to enter another person: to Stop Enter 'n' ")
    keyval=keyval+1
    if x=='n':
        break
print(mydict)

x=input("Enter to exit")