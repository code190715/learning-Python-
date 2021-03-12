name = "usman"; print(name);

sum = 1+1;
print(sum);

#this is a comment

name = "Roger";
print(type(name) == str);
#check the type of a variable by using the type() function, passing the variable as an argument, and then comparing the result to str

print()

age = 1;
print("This is a int:");print(type(age) == int);

fraction = 0.4;
print("This is a float:");print(type(fraction) == float);

print()

#You can also create a variable of a specific type by using the class constructor, passing a value literal or a variable name:
name = str("Hope");
anotherName = str(name);


age = 23;
anotherVariable = age;


print()

firstName = "Usman";
lastName = 'Sajid';
#Stringgs can be defined single or double quotes

print("My full name is " + firstName + " " + lastName);


str(23);
#Converting a num to a string using constructor 
print(firstName + " is " + str(23) + " years old");


#strings can be multiline with three quotes:
print( """ Usman is 


23 


years old """);


name = 'Usman';
print(name.upper());
print(name);

name = "usman";
print ("man" in name);



name = "Hope";
print(name[0]);
print(name[1]);
print(name[2]);
print(name[3]);
print(name[-1]); #neg num starts counting from the end 
print()
print(name[0:2]);
print(name[2:]);

