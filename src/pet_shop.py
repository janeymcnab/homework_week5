# WRITE YOUR FUNCTIONS HERE


def get_pet_shop_name(pet_shop):
    return pet_shop["name"]


def get_total_cash(pet_shop):
    cash = pet_shop["admin"]["total_cash"]
    return cash


def add_or_remove_cash(pet_shop, amount):
   pet_shop["admin"]["total_cash"] += amount
     
     
def get_pets_sold (pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, sold):
    pet_shop["admin"]["pets_sold"] += sold
    return sold

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

def get_pets_by_breed(pet_shop, breed):
    breed_list = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed:
            breed_list.append(breed)
    return breed_list

def find_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            return pet
        else:
            pet = None

def remove_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            pet_shop["pets"].remove(pet)

def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)

def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer, amount):
    customer["cash"] -= amount

def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)


# EXTENSIONS

def customer_can_afford_pet(customer, new_pet):
    can_buy_pet = False
    if customer["cash"] >= new_pet["price"]:
        can_buy_pet = True
    return can_buy_pet


# OPTIONAL

# This code passes the first optional test.

# def sell_pet_to_customer(pet_shop, pet, customer):
#     pets_sold = []
#     pet_shop["admin"]["total_cash"] += pet["price"]
#     pet_shop["pets"].remove(pet)
#     customer["pets"].append(pet)
#     pets_sold.append(pet)
#     customer["cash"] -= pet["price"]
#     pet_shop["admin"]["pets_sold"] += len(pets_sold)


# This is attempted code to work with all three optional tests.

# def sell_pet_to_customer(pet_shop, pet, customer):
#     sufficient_funds = False
#     pet_found = False
#     pets_sold = []
#     if customer["cash"] >= pet["price"]:
#         sufficient_funds = True
#     for pet in pet_shop["pets"]: 
#         if pet["name"] == pet:
#             pet_found = True
#     if pet_found and sufficient_funds == True:
#         pet_shop["admin"]["total_cash"] += pet["price"]
#         pet_shop["pets"].remove(pet)
#         customer["pets"].append(pet)
#         customer["cash"] -= pet["price"]
#         pets_sold.append(pet)
#         pet_shop["admin"]["pets_sold"] += len(pets_sold)
                    

                



    


    
    
        


