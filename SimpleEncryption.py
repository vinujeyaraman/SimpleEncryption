num = int(input("Enter the key: "))
cypher = str(input("Enter the original string or cypher: "))
option = int(input("Enter if you want to encode or decode the cypher (1 to encode and 0 to deocde): "))

l = len(cypher)
n = 0

if option == 0: 
    while n < l: 
        if 90 >= ord(cypher[n]) >= 65: 
            b = ord(cypher[n]) - 65 + num
            print(chr((b%26)+65), end="")
            n += 1
        
        elif 122 >= ord(cypher[n]) >= 97: 
            c = ord(cypher[n]) - 97 + num
            print(chr((c%26)+97), end="")
            n += 1
        else:
            print(cypher[n], end= "")
            n += 1
elif option == 1: 
    while n < l:
        if 90 >= ord(cypher[n]) >= 65: 
            b = ord(cypher[n]) + 65 - num
            print(chr((b%26)+65), end="")
            n += 1
            
        elif 122 >= ord(cypher[n]) >= 97: 
            c = ord(cypher[n]) - 97 - num
            print(chr((c%26)+97), end="")
            n += 1
        else:
            print(cypher[n], end= "")
            n += 1
