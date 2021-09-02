
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "        # This is the base of the encryption and the decryption

massege  = input ()

encrypt = lambda letter, shift, alph : alph [(alph.index (letter.upper ()) + shift) % len (alph)]       # annonymous fuction for encryt to a character

decrypt = lambda letter, shift, alph : alph [(alph.index (letter.upper ())) - shift]                    # annonymous fuction for decryt to a character

deMassege = []      # store encrypted chars

for i in massege:
    enChar = encrypt (i, 5, alphabet)
    deMassege.append (enChar)               # append encrypted characters in to deMassege list

deMassege = ''.join (deMassege)             # convert list to a string

print("Encrypted massege : " + deMassege)

print ("Encrypted massege : ", end="")

for i in deMassege:
    print (decrypt (i, 5, alphabet), end="")
