contact ={}
def display_contact():
    print("name\t\tcontact info")
    for key in contact:
        print("{}\t\t{}".format(key,contact.get(key)))

while True :
    choice =int(input(" 1.add new contact\n 2.search contact\n 3.display contact\n 4.edit contact\n 5.delete contact\n 6.exit\n enter your choice"))
    if choice== 1:
        name=input("enter the contact name")
        phone=input("enter contact's phone number")
        email=input ("enter contact's email")
        contact [name]=[phone,email]
    elif choice==2:
        search_name=input("enter the contact name")
        if search_name in contact:
            print(search_name,"'s contact number and email",contact[search_name])
        else :
            print("name is not found ")
    elif choice==3:
        if not contact:
            print("empty contact book")        
        else :
            display_contact()
    elif choice == 4:
        edit_contact=input("enter the contact to be edited ") 
        if edit_contact in contact :
              phone=input("enter contact's phone number")
              email=input ("enter contact's email")  
              contact [edit_contact]=[phone,email]
              print("contact updated ")   
              display_contact()
        else :
            print("number is not found ")

    elif choice==5:
        del_contact=input("enter the contact to be deleted ")
        if del_contact in contact :
            confirm=input("do you want to delete this contact y/n?")  
            if confirm=='y' or confirm=='Y' :
                 contact.pop(del_contact)  
            display_contact()
        else:
            print("name is not found ")
    else :
        break