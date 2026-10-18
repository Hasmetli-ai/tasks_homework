letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers="0123456789"
i=0
valid=True
plate=input("Plate: ")
plate=plate.upper()
if plate!=plate.split():
    valid=False
if len(plate)<=2 and len(plate)>=6:
    valid=False
number_started=False
for char in plate:
    if char not in letters or char not in numbers:
        valid=False
for char in plate:
    if char in numbers:
        if number_started==False:
            if char=="0":
                valid=False
            number_started=True
    else:
        number_started=False
if valid==True:
    print(f"Plate {plate}")
else:
    print("Invalid plate")