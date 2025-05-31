list_of_add=[]
list_of_sub=[]
list_of_mul=[]
list_of_div=[]
list_of_mod=[]
def add_function(num_1,num_2):
    add=num_1+num_2
    list_of_add.append(add)
    return list_of_add
 
def sub_function(num_1,num_2):
    sub=num_1-num_2
    list_of_sub.append(sub)
    return list_of_sub

def mul_function(num_1,num_2):
    mul=num_1*num_2
    list_of_mul.append(mul)
    return list_of_mul

def div_function(num_1,num_2):
    try:
        div=num_1/num_2
        list_of_div.append(div)
        return list_of_div
    except ZeroDivisionError:
        print("Number is not divisible by 0")

def mod_function(num_1,num_2):
    try:
        mod=num_1%num_2
        list_of_mod.append(mod)
        return list_of_mod
    except ZeroDivisionError:
        print("Number is not divisible by 0")



def main_play():
    
    while True:
        player_choice=input("Do you want to exit or continue ? : ")
        if player_choice=='exit':
            print('Try again!!')
            break
        
        player_input=input("Enter which operation would you like to perform- add/sub/mul/div/mod :")
        if player_input not in ['add','sub','mul','div','mod']:
            print("Invalid choice, please input add,sub,mul,div,mod")
            break
            
        num_1=int(input("Enter a first number: "))
        num_2=int(input("Enter a second number: "))
        if player_input=='add':
            print("Addition: ",add_function(num_1,num_2))
        elif player_input=="sub":
            print("Subtraction: ",sub_function(num_1,num_2))
        elif player_input=="mul":
            print("Multiplication: ",mul_function(num_1,num_2))
        elif player_input=='div':
            print("Division: ",div_function(num_1,num_2))
        elif player_input=='mod':
            print("Modulus: ",mod_function(num_1,num_2))
 
if __name__ == "__main__":
    main_play()



    


    