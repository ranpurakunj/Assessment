'''
Write a function that takes input string as a parameter and it converts 
those strings in desired format as given below :-
       2[a]2[b] = aabb
       2[a2[b]] = abbabb
       2[a2[b2[c]]] = abccbccabccbcc
'''

def conversion(Str):
    stck=[]
    for i in range(len(Str)):
        if Str[i]==']':
            temp=""
            while len(stck)>0 and stck[-1] != '[':
                temp = stck[-1] + temp
                stck.pop()
            num = ""
            stck.pop()
            while len(stck)>0 and ord(stck[-1]) >=48 and ord(stck[-1]) <=57:
                num = stck[-1] + num
                stck.pop()
            number=int(num)
            rep=""
            for j in range(number):
                rep+=temp
            for a in range(len(rep)):
                if len(stck)>0:
                    if rep == stck[-1]:
                        break
                stck.append(rep)
        else:
            stck.append(Str[i])
    return stck[0]


st="2[a2[b2[c]]]"
print(conversion(st))

