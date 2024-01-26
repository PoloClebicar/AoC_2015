import hashlib

numKey = 1

while True:
    key = "bgvyzdsv" + str(numKey)

    mdKey = hashlib.md5(key.encode())
    mdKey = mdKey.hexdigest()

    if mdKey[0] == "0" and mdKey[1] == "0" and mdKey[2] == "0"and mdKey[3] == "0"and mdKey[4] == "0" and mdKey[5] == "0":
        print(mdKey, key)
        break

    numKey += 1 


