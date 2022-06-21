# create a public function, generate a dictionary with 10 random keys, values.
#keys: random letter (bet kokia nesikartojanti raide)
#Values: (bet koks skaicius nuo 0 iki 30, skaicius  negali kartotis)
#Grazinti kokiam Key prilauso dizdiausias value.

import random, string

def dict_generator() -> str:
    my_dict = {}
   
    while True:
        random_letter = random.choice(string.ascii_letters)
        random_number = random.randint(1, 30)
        
        if random_number not in my_dict.values():
            my_dict [random_letter] = random_number
            
        if len(my_dict) >= 10:
            break
    print(my_dict)
    return max(my_dict, key=my_dict.get)
   
print(dict_generator())

