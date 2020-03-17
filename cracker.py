import hashlib

#Variables for control
flag = 0
counter = 0

passwin = input("Please enter the MD5 hashed password:")
pwfile = input("Please enter the name or path of your password dictionary file:")

#Error Handling for the file
try:
    pwfile = open(pwfile, "r")

except:
    print("\nFile not Found.")
    quit()

#The loop that converts the passwords in the dictionary and compares it with your input hash
for word in pwfile:
    enc_word = word.encode('utf-8')
    md5pass = hashlib.md5(enc_word.strip()).hexdigest()
    counter += 1

    #printing it out to give finesse
    print(word)
    print(md5pass)
    print(passwin)
    print(counter)

    #Catches a match and end the loop
    if md5pass == passwin:
        print("Password Found")
        print("\npassword is" + word)
        print(counter)
        flag = 1
        break

    #When there's no match
    if flag == 0:
        print("Password not Found")
