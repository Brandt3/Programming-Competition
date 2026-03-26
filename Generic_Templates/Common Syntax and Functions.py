
# ================== DICTIONARY =============== 

# ADD VALUES
my_dict = {'apple': 1, 'banana': 2}
my_dict['orange'] = 3

print(my_dict)
# Output: {'apple': 1, 'banana': 2, 'orange': 3}

# LOOP 
for k, v in my_dict.items():
    print(f"Name is {k}, their words are {v}")



# ================== LOOP and Keep index ==========

my_list = ['apple', 'banana', 'cherry']

for index, value in enumerate(my_list):
    print(f"Index: {index}, Value: {value}")