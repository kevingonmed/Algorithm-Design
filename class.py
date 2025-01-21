"""print ("Hello world")
print (f"i was born in {2001}")
#name = input("your name: ")
#print (f"your name is {name}.")

birth_year = input("Your birthday: ")
print (f"Your birthday is {birth_year}.")
age = 2025 - int(birth_year)
print (f"your age is {age}.")"""

#Print your name in txt file
"""try:
    name = input("your name: ")
    file = open("name.txt", "w")
    file.write(name)
    file.close
except OSError:
    print("error")

with open("name.txt", "r") as file:
    print(file.read())
import json
with open ("Lab02.json", "r") as file:
        data = file.read()
        data2 = json.loads(data)
        #print(data2)

        ussername = data2["username"]
        #print(ussername)

        password = data2["password"]
        #print(password)

        password  =password[3]
        print("\nthe forth paswword is: " + password)
        ussername = ussername[3]   
        print("\nthe forth ussername is: " + ussername)"""

#number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#print(number)
#print(number[0:3],number[7:10],number[3:6])

#tuple_one = 1, 1.1
#print(tuple_one[0])
#print(tuple_one[1])

#for i in range(5+1):
#    print(i)



#for i in range(10,35+5,5):
#    print(i)

"""name = ["Kevin", "Juan", "Maria", "Pedro"]
for i, name in enumerate(name):
    print(i+1, " ", name)"""


text ="""No se que escribir pero es lo que me eaata pidienso el camarada, entonces vamos a ver que se arma, tengo
hambre y """
print(text[0])
print(len(text))
print(text[:20])"""










