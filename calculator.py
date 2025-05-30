list_of_add=[]
list_of_sub=[]
list_of_mul=[]
list_of_div=[]
list_of_mod=[]
list_of_reminder=[]


def add(num_1,num_2):
    
    add=num_1+num_2
    list_of_add.append(add)
    return list_of_add
 
def sub(num_1,num_2):
    
    sub=num_1-num_2
    list_of_sub.append(sub)
    return list_of_sub

def mul(num_1,num_2):

    mul=num_1*num_2
    list_of_mul.append(mul)
    return list_of_mul

def div(num_1,num_2):
    div=num_1/num_2
    list_of_div.append(div)
    return list_of_div

def mod(num_1,num_2):
    mod=num_1%num_2
    list_of_mod.append(mod)
    return list_of_mod

def reminder(num_1,num_2):
    
    reminder=num_1%num_2
    list_of_reminder.append(reminder)
    return list_of_reminder
    


 

def main_play():
    while True:
        
        player_input=input("Enter which operation would you like to perform- add/sub/mul/div/mod/reminder :")
        num_1=int(input("Enter a first number: "))
        num_2=int(input("Enter a second number: "))
        if player_input=='add':
            print("Addition: ",add(num_1,num_2))
        elif player_input=="sub":
            print("Subtraction: ",sub(num_1,num_2))
        elif player_input=="mul":
            print("Multiplication: ",mul(num_1,num_2))
        elif player_input=='div':
            print("Division: ",div(num_1,num_2))
        elif player_input=='mod':
            print("Modulus: ",mod(num_1,num_2))
        elif player_input=='reminder':
            print("Reminder: ",reminder(num_1,num_2))
        else:
            print("Invalid choice. Enter add/sub/mul/mod/div/reminder")
    
main_play()



    


    