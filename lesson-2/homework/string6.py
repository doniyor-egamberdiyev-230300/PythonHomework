a = input("Enter the string: ")
b= input("Enter the string to search: ")

if b in a:
    print(f'"{b}" is found in "{a}"')

else:
      print(f' "{b}" is not found in "{a}"')