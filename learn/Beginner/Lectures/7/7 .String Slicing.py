# slicing = Creating a substring by extracting element from another string
# Indexing[] / slice()
#indexing[start_pos:stop_pos:steps]
Name = "Ibrahim Amen" #0:7 8[Space] 9:12
#First
# part_of_my_name = Name[6] #I
# print(part_of_my_name)
#
# Full_First_name = Name[0:7]
# print(Full_First_name)
#
# Full_Last_name = Name[8:12]
# print(Full_Last_name)
#
# full_name = Name[:]
# print(full_name)

#Slice [Steps] [2] show only character

# Funke_name = Name[::2] #IrhmAe
# Funke_name = Name[0:12:2] #IrhmAe
# print(Funke_name)

# Reversed_name = Name[::-1]
# print(Reversed_name)
####
# slice()

my_website_1 = "https://www.google.com"
my_website_2 = "https://www.facebook.com"
my_website_3 = "https://udemy.com"

Extracted_word = slice(12,-4)

print(my_website_1[Extracted_word])
print(my_website_2[Extracted_word])
print(my_website_3[slice(8,-4)])