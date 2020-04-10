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

num_bin = input('Input the binary sequence: Ex: 00000001 >> ').strip()


if len(num_bin) > 8:
    print('Number max of digits is 8.')
elif not isinstance(num_bin, int):
    print('Not number valid.')
