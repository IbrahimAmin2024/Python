# Write a file (rewrite/create new write)


#Ibrahim
#Hello
#this for testing purpose

text = "Ibrahim\nHello\nthis for testing purpose"

# 'w' = over Writing
# 'a' = append

try:
    with open('C:\\Users\\hezoo\\OneDrive\\Desktop\\test.txt','w') as file:
        file.write(text)
except FileNotFoundError:
    print("That file was not found!")