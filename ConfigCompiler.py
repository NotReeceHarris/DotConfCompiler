#         __  __                                       __
#        / / / /___ __________  ____  ______________ _/ /____
#       / /_/ / __ `/ ___/ __ \/ __ \/ ___/ ___/ __ `/ __/ _ \
#      / __  / /_/ / /  / /_/ / /_/ / /__/ /  / /_/ / /_/  __/
#     /_/ /_/\__,_/_/  / .___/\____/\___/_/   \__,_/\__/\___/
#                     /_/
#     Github: https://github.com/NotReeceHarris/Harpocrate
#     Dev   : https://github.com/NotReeceHarris

def ConfRead(FilePath):

    # Creates a dict of all lines in conf file.
    # Excluding:
    #       lines starting with '#'
    #       lines containing nothing
    # Including:
    #       lines containing data

    conf = [x for x in open(FilePath).read().splitlines() if not x.startswith('#')]
    VarNames = []
    Data = []

    while '' in conf: conf.remove('')

    # Removes variable name from dict and adds the
    # data back to the list minus the variable name

    for idx, x in enumerate(conf):
        index = x.find('=')
        VarNames.append(x[:index])
        Data.append(x[index:][1:])
    
    ConfForm = '{'

    # Converts string values into boolens and nil value if 
    # data equal to 'True', 'False', 'None'

    for x in range(len(VarNames)):
        if Data[x].lower() == 'true' or Data[x] == True:
            ConfForm += f'"{VarNames[x]}":true'
        elif Data[x].lower() == 'false' or Data[x] == False:
            ConfForm += f'"{VarNames[x]}":false'
        elif Data[x].lower() == 'none' or Data[x] == None:
            ConfForm += f'"{VarNames[x]}":null'
        else:
            ConfForm += f'"{VarNames[x]}":"{Data[x]}"'

        try:
            VarNames[x+1]
            ConfForm += ','
        except:
            ConfForm += '}'

    # Method to convert homebrew dict into a dict type.
    # Method:
    #   Temporarily create a 'temp.json' file and writing 
    #   the homebrew dict into the file, use the json
    #   package to compile the json into a dict type.

    import json
    import os

    w = open('./temp.json', 'w')
    w.write(ConfForm)
    w.close()
    x = json.load(open('./temp.json'))
    os.remove('./temp.json')

    return x

def ConfWrite(FilePath, VarName, Data):

    # Creates a dict of all lines in conf file.

    conf = [x for x in open(FilePath).read().splitlines()]

    # Open and read the config file

    r = open(FilePath, 'r')
    fc = ''

    # iterate through all lines in the file and search for an '='
    # within the line, if the data before the '=' is equal to the
    # variable name then update that line with the new data.

    for x in r.readlines():
        index = x.find('=')
        if x[:index] == VarName:
            fc += f'{VarName}={Data}\n'
        else:
            fc += x

    # Open and write the 'fc' data

    w = open(FilePath, 'w')
    w.write(fc)

    # Close r and w

    r.close()
    w.close()