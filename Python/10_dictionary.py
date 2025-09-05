dics = {
    "name" : "Rohan",
    "roll" : 234,
    "canDrive" : False,
    "openToWork" : True
}

print(dics["name"])

print(dics.get("name"))

print(dics)

print(dics.get("nicName" , "chintu"))
print(dics)


# -----------key

print(dics.keys())
dicsKeys = dics.keys()
print(dicsKeys)


# ------------values


print(dics.values())
dicsValues = dics.values()
print(dicsValues)



# ----------update

dics.update({"name" : "Mohan", "age" : 25})
print(dics)

pics = {
    "name":"Pintu",
    "canDrive": False
}

print(pics)
dics.update(pics)
print(dics)

# ----------pop 

print(dics.pop("age"))
print(dics)

# popitempair - Removes and returns the last inserted (key, value) pair.

print(dics.popitem())
print(dics)


# ---------------set default

dics.setdefault("roll", 00)
print(dics)

dics.setdefault("openToWork", False)
print(dics)

# -----------cop

dics_2 = dics.copy()
print(dics_2)