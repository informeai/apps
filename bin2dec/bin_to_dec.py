print(""" 
########################
########################
###### 00000001 ########
######    |     ########
######    v     ########
######    1     ########
########################
########################
##### BIN -> HEX #######
""")

def convert_num(value:int):
    return int(value, 2)
def evaluate_num(value):
    for n in value:
        if n is '0' or n is '1':
            pass
        else:
            return True

num_bin = input('Input the binary sequence: Ex: 00000001 >> ').strip()


if len(num_bin) > 8:
    print('Number max of digits is 8.')
elif evaluate_num(num_bin):
    print('Number format not compost of 0 or 1')
else:
    pass