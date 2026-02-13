"""
This is a basic crash course on working with Python as a coding language
underneath this section I have commented out some basic functionality, and we will go about removing the comment tag to
add various functions to this program. The first step will be to remove the comment line indicator # at the beginning of
lines 7 through 10, while keeping the comments after the parentheses as they are explanatory in nature!
"""
#print("Hello World") #This is generally the first thing all coders will express with a new language
#print("-----") #I've added this for visual clarity of the output in the terminal below
#print("Harper College Cybersecurity Club Python Crash Course!") #This is us!
#print("-----") #again visual clarity
"""
Next up we are going to discuss variables. If you're familiar with the concept from mathematics, it largely is the same
concept here. We have a value such as X that will represent another value such as 42. An important thing with variables 
when coding is that there are several types of variables to be considered.

float - A number that can also have fractional values ie: 3.5, but can also be a whole number ie: 2
int - A number that has to be a whole value ie: 2
str - A string value represents a sequence of characters, which can be alphanumeric
user input - You can have user defined variables, and typically the coder should expect a certain type of data ie: str
or int
bool - true or false value. This also gets into conditional values where things can get a bit more complex code wise.
we will briefly cover this concept in the next section, but just be aware that typically a boolean data type tends to be
comparative in nature. Now lets interact with the following section by uncommenting lines 25 to 33
"""
#X = float(3.1415) #In this example X would be roughly equal to PI
#Y = int(42) #The ultimate answer to life, the universe, and everthing
#Z = str("Cybersecurity Club Python Project") #Us again!
#print(Z) 
#A = int(input("Enter a whole number: ")) #This line will ask you to enter a value into the terminel at the bottom of the IDE
#if A == Y:
#    print("A is equal to Y")
#else:
#    print("A is not equal to Y")
"""
Since we briefly touched on it in the previous section lets go ahead and mention conditions here. The previous section
I demonstrated a boolean true false value with the user input section and an if/else statement in the code. This is one
example of a conditional response for your code to output, if we provided the number 42 to the request for a whole number
the code would tell us that it the values are equal, however the code does not need to indicate the variables by name,
and often does not. Lets take a look at another example. In order to make our lives easier lets recomment up the previous
sections so they don't need to be run again and again moving forward, and uncomment lines 42 to 49.
"""
#C = 50 #Here we haven't assigned C a variable type, but thats okay because python will recognize that C is 50 with just this
#D = int(input("Enter a whole number: ")) #pretend you don't know that C is 50, and enter a random value!
#if C == D:
#    print("You have entered the correct value!")
#elif C > D:
#    print("You have entered a value smaller than the correct value.")
#elif C < D:
#    print("You have entered a value larger than the correct value.")
"""
In this example there are three possible outcomes, and our code has accounted for each of them. Either the input is
correct, or the input is incorrect in one of two ways. Additionally, we made use of relational operators here via the
equals to ( == ) greater than ( > ) and less than ( < ) choices for our example. Relational operators are yet another
intrusion from mathematics, but coding at the end of the day is a bunch of 1's and 0's. In python you can take advantage
of the following types of relational operators
<   - less than
>   - greater than
<=  - less than or equal to
>=  - greater than or equal to
==  - equal to
!=  - not equal to

In addition to relational operators, you can use logical operators in your python code, which are as follows:
and
or
not

using logical operators in your code functions similarly to how one might use these words in a sentence.
lets examine these by uncommenting lines 72 to 74 which covers our basic foundation here. to examine an instance of "or"
in operation lets uncomment lines 75 to 78. to examine and, uncomment 79 to 82, to examine not uncomment 83 to 86.
"""
#E = int(input("Enter a whole number: "))
#F = int(input("Enter either the same number or a different number: "))
#G = E + F
#if G == (E + E) or G == (F + F):
#    print("You entered the same number")
#else:
#    print("You entered different numbers")
#if G == E and G != F:
#    print("You entered zero for the second number")
#else:
#    print("You did not enter zero for the second number")
#if G == F and not G == E:
#    print("You entered a zero first")
#else:
#    print("You entered a positive number first")
