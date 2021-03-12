def stringch(str1):
    char=str1[3]
    str1=str1.replace(char,'$')
    str1=char+str1[1:]
    return str1
print(stringch('amma'))