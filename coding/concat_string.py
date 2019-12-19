def concat_string(my_str,n):
    if n<=len(my_str):
        my_str=my_str[n:len(my_str)]
    return my_str
user_string=input("enter a string: ")
n=int(input("enter a number till you want concat"))
new_str=concat_string(user_string,n)
print("original string:",user_string)
print("concatenated string:",new_str)