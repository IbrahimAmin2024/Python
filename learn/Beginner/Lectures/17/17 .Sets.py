#Sets = collection which is unordered, unindexed, {no dublicated values},remove,common value..

utensils = {"fork","spoon","knief","knief","knief","knief"}
dishes = {"bowl","cup","plate","knief"}

# utensils_2 = ("fork","spoon","knief","knief","knief","knief")
# print(utensils)
# print(utensils_2)
# utensils.add("napkin")
# utensils.remove("fork")
# utensils.clear()
# dishes.update(utensils)
# dinner_tables = utensils.union(dishes)

#diffrience = dishes.difference(utensils)
common = utensils.intersection(dishes)
print(common)

for i in utensils:
   print(i)

