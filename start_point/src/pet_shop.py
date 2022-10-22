# WRITE YOUR FUNCTIONS HERE

#check
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]


def get_total_cash(pet_shop):
    return pet_shop ["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, cash):
    
    pet_shop ["admin"]["total_cash"]+=cash

    

def get_pets_sold(pet_shop):
    return pet_shop ["admin"]["pets_sold"]


def increase_pets_sold (pet_shop, amount_sold):
        pet_shop ["admin"]["pets_sold"]+= amount_sold

def get_stock_count(pet_shop):
    stock_count=0
    for pet in pet_shop["pets"]:
        stock_count+=1
    return(stock_count)




def get_pets_by_breed(pet_shop, breed):
    pets_by_breed=[]
    for pet in pet_shop["pets"]:
        if pet ["breed"]==breed:
            pets_by_breed.append(breed)
    return pets_by_breed

def find_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if pet["name"]== name:
          return pet
        

    #index = animals.index('dog')    fruits.pop(1)   index=pet_shop["pets"].index 
# thislist = ["apple", "banana", "cherry"]
# thislist.remove("banana")
# print(thislist)

def remove_pet_by_name(pet_shop, name):
    
    for pet in pet_shop["pets"]:
     if pet["name"]== name:
        pet_shop["pets"].remove(pet)

def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)

def get_customer_cash(customers):
     return customers["cash"]

     #print(myList[0]['bar'])
     # for index in range(len(a_list)):

# /
def remove_customer_cash(customers, cash):
    customers["cash"]-=cash

# why would I want to remoce from all customers the same amount of cash at the same time?
    
def get_customer_pet_count(customers):
    return len(customers["pets"])

def add_pet_to_customer(customers, new_pet):
    customers["pets"].append(new_pet)

def customer_can_afford_pet():
    pass
    


