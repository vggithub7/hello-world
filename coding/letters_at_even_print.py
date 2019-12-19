def letters_at_even_print(str):
    for i in range(len(str)):
        if i%2==0:
            print("index[i]:",str[i])
            
str=input("enter string")
print("original string is:" ,str)
letters_at_even_print(str)