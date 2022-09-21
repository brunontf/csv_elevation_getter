def validate_file(file,extension,type):
    if file == '':
        file= type + '.'+ extension
    elif file.endswith('.'+extension) == False:
        file+= '.'+ extension
    return file

def validate_int(number,name):
    if type(number) != int:
        print(name, 'its not an integer')
        return False
    else:
        return True

# print(validate_int(10,'lat'))

# x= ''

# print(validate_file(x,'json','output'))