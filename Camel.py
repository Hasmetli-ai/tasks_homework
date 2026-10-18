while True:
    camel_case=input("camel_case: ")
    if camel_case[0]==camel_case[0].upper():
        print("Please type correctly in camelcase nigger")
        continue
    else:
        break
for i in camel_case:
    if i.upper() == i:
        index=camel_case.find(i)
        sneak_case=camel_case[:index]+"_"+camel_case[index:]
print(sneak_case)


