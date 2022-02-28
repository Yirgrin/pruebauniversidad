
print ("Ingrese dos palabras")
palabra1 = input ()
palabra2 = input ()




if palabra1 [:-4:-1] in palabra2[:-4:-1]: 
    print ("Las palabras riman")
elif palabra1[:-3:-1] in palabra2[:-3:-1]: 
    print ("Las palabras riman un poco")
else: 
    print ("Las palabras no riman")



