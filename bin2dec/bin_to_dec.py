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


num_bin = input('Digite uma sequencia binária: Ex: 00000001 >> ').strip()


if len(num_bin) <= 8:
    result = int(num_bin,2)

    print(f'O Resultado é -> {result}')
else:
    print(f'O número maximo de digitos é 8.')
