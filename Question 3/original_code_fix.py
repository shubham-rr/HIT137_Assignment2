# Corrected code with comments

global_variable = 100
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

def process_numbers():
    global global_variable
    local_variable = 5
    numbers = [1, 2, 3, 4, 5]

    while local_variable > 0:
        if local_variable % 2 == 0:
            numbers.remove(local_variable)
        local_variable -= 1

    return numbers

# Sets do not allow duplicate values, so this will automatically be {1, 2, 3, 4, 5}
my_set = {1, 2, 3, 4, 5}
# The function process_numbers does not take any arguments, so we call it without arguments
result = process_numbers()

def modify_dict():
    local_variable = 10
    my_dict['key4'] = local_variable

# The function modify_dict does not take any arguments, so we call it without arguments
modify_dict()

def update_global():
    global global_variable
    global_variable += 10

# update_global() is defined but never called

# i += 1 in the for loop does not affect the loop's iteration
# and won't change the value of i 
for i in range(5):
    print(i)
    # removed i += 1

# my_dict['key4'] will return an error if the key does not exist
# replacing it with my_dict.get('key4') will return None if the key doesn't exist
if my_set is not None and my_dict.get('key4') == 10:
    print("Condition met!")

if 5 not in my_dict:
    print("5 not found in the dictionary!")

print(global_variable)
print(my_dict)
print(my_set)
