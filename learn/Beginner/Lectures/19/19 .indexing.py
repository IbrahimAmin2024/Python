#dictionary = a changeable, unordered collection of unique key:value pairs
#             fast because they use hashing, allow us to access a value quickly

#[
# key:value,
# key:value
# ] braces

capitals = {
    "USA" : "Washington DC",
    "India" : "New Delhi",
    "China" : "Beijing",
    "Russia" : "Moscow",
    "Egypt": "Cairo"
}

# capitals.update({"Germany" : "Berlin"}) # adding new item
# capitals.update({"Egypt" : "Alex"}) # edit currently item
# capitals.pop("Russia")# will remove ur specific item
# capitals.clear()

print(capitals.values())
print(capitals["China"])
print(capitals.get("China"))
print(capitals.items())


# for key,value in capitals.items():
#    print(key, value, end=" |") # USA India











