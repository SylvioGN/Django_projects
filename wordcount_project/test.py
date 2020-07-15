x = "olá tudo bem meu nome é sylvio , como vc está, sylvio sylvio sylvio"

words = x.split()

dicword = {}


for x in words:
    if x not in list(dicword.keys()): 
        dicword[x] = 1 
    else:
        dicword[x] +=  1

print(dicword)