#Question 1
def multi_seven():
    '''finds all numbers that are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included) and prints them in a comma-separated sequence on a single line.'''
    div_seven=[]
    
    # Finds all numbers between 2000 and 3200 both included
    # Filters all multiples of seven that aren't multiples of 5
    #converts the value from int to string and adds it to a list
    for i in range(2000,3201):
        if i%7==0 and i%5==1:
            div_seven.append(str(i))
            
    #converts the list obtained from the loop into a string
    #prints in a comma-separated sequence on a single line.
    stringzy=", ".join(div_seven)
    print(stringzy)
    
    
#Question 2
def fact():
    
    #prompts the user to enter a number and converts the input into an integer
    user_input=int(input("Enter a number to find it's factorial: "))
    
    #Initialize a function to calculate the factorial of the entered number
    #returns 1 if the number is zero or once since their factorial is equal to one
    #else calaulates the factorial of the number if the number is greater then one
    def facto(num):
        if num == 0 or num == 1:
            return 1
        else:
            return num*facto(num-1)
        
    #stores the factorial in result variable
    result = facto(user_input)
    print(result)
    

# Question 3
def integral_dict(): #Initialize the function
    
    #Prompt the user to enter a number and converts the input into an integer
    user_input = int(input("Please enter a number")) 
    
    #Instantiate a dictionary
    int_dict=dict() 
    
    #iterate over the numbers between 1 and the given input, both included
    #creates a dictionary with the number as the key and the square of the number as the value
    for i in range(1, user_input+1):
        int_dict[i]=i*i
    
    #prints the dictionary
    print(int_dict) 
    
    
# Question 4
def list_tuple():
    #Prompt the user to enter a sequence of comma separated numbers and converts the input into a ist
    user_input=input("Enter a sequence of comma separated numbers").split(",")
    
    #converts the list into a tuple
    tups=tuple(user_input)
    
    #prints the user input both as a list and tuple
    print(user_input,tups)
    

# Question 5
#creates a class Q5
class Q5:
    def __init__(self):
        self.user_input="A statement is needed"
        
    #initializes a method getString that prompts the user to enter a statement of their choice
    def getString(self):
        self.user_input=input('Enter a statement of your choice')
    
    #initializes a method printString that converts the user_input into uppercase
    def printString(self):
        print(self.user_input.upper())
        
#Initializes a function in which a class object is instantiated
#the two methods in the object created are called
def funky():
    gig=Q5()
    gig.getString()
    gig.printString()
    
    
    
#Question 6
def Q6():
    H=30
    C=50
    
    #prompts the user to enter a sequence of comma separated numbers and converts the input into a list
    user_input=input("Please enter a sequence of comma separated numbers").split(",")
    
    #iterates over the user_input list
    #for each iteration, it converts the element into a integer and saves it to the variable D
    #performs the arithmetic operation
    #and prints the result obtained in each iteration
    for i in user_input:
        D=int(i)
        Q=round(((2 * C * D)/H)**0.5)
        print(Q,end=", ")
        
        
        
#Question 8
#initialize a function
def sortQ8():
    
    # Prompt the user to enter a sequence of comma separated words and converts the input into a list
    user_input=input("Please enter a sequence of comma separated words").split(",")
    
    # sorts the list in reverse order
    user_input.sort(reverse=True)
    
    # prints the user i put sorted in reverse order
    print(user_input)
    
    
    
#Question 9
def upperQ9():
    
    # propts the user to enter a sequence of lines 3 times and saves the input in a variable user_input
    # prints each statement stored in the variable
    user_input=[input("Please enter a sequence of lines.").upper() for i in range(1,4)]
    for i in user_input:
        print(i)
        
        
        
# Question 10
def Q10():
    
    # prompts the user to enter a sequence of words separated by white spaces and converts the input into a list
    # sorts the user_input list
    #and prints out the list
    user_input=list(set(input("Please a sequence of word separated by witespaces").split(" ")))
    user_input.sort()
    print(user_input)
    
    
#Question 41
def tupQ41():
    
    # instantiate an empty list
    # squares every number between 1 and 20 both included and appends them to the list
    squared=list()
    for i in range(1,21):
        squared.append(i**2)
    
    # converts the list into a tuple
    squared=tuple(squared)
    print(squared)
    
    
    
#Question 42
# imports the math module
import math

# creates a tupQ42 function that has a default argument tups
def tupQ42(tups=(1,2,3,4,5,6,7,8,9,10)):
    
    # gets the length of the tuple and divides it by two
    #rounds it off with the ceil() method from the math module and saves it to a variable midpoint
    midpoint=math.ceil(len(tups)/2)
    
    #splices the tuple in half and two halves separated by a new line
    print(tups[:midpoint],tups[midpoint:], sep="\n")
    
tupQ42((1,2,3,4,5,6,7,8,9,10,11,12))



#43
#creates a tupQ43 function
def tupQ43():
    
    #initializes a tuple
    #instantiate a list
    tups=(1,2,3,4,5,6,7,8,9,10)
    tuplist=[]
    
    #iterates over the tuple appending each iterated element to the tuplist if the element is an even number
    for i in tups:
        if i%2==0:
            tuplist.append(i**2)
            
    #converts the tuplist list into a tuple using the tuple method and prints it
    print(tuple(tuplist))
    
    
    
#44

#creates a function Q44
def Q44():
    
    # Prompts the user to enter either yes YES or Yes
    user_input=input("yes or YES or Yes")
    
    #checks whether the user has passed in the expected input
    #prints Yes if the input is the Expected one otherwise it prints Np
    if user_input=='yes' or user_input=='YES' or user_input=='Yes':
        print("Yes")
    else:
        print("No")
        
        
#45
def Q45():
    
    #initialize a numlst list
    numlst=[1,2,3,4,5,6,7,8,9,10]
    
    #filter numlst using lambda function to select the even numbers
    #initialize an evens list from the filter function using the list() function and print it
    evens=list(filter(lambda i : i%2==0,numlst))
    print(evens)
    
    
    
#46
def Q46():
    
    #initialize a munlst
    numlst=[1,2,3,4,5,6,7,8,9,10]
    
    # iterating over each numlst using the map function
    # ieach element of numlst is squared using the anonymous lambda function
    # initialize a list squared from the map object using the list() function
    squared=list(map(lambda i : i*i, numlst))
    print(squared)
    
    
    
#47
def Q47():
    
    # initialize a numlst list
    numlst=[1,2,3,4,5,6,7,8,9,10]
    
    #filter numlst using the lambda function
    # the result is then iterated over using the map function and each of its elements is squared using the lambda function
    #initialize a squared_evens list from the map object using a list() function
    squared_evens=list(map(lambda i : i*i, filter(lambda i : i%2==0,numlst)))
    print(squared_evens)
    
    
    
#48
def Q48():
    
    #filters the numbers in the range of 1 and 20 both included using the lambda function to select the even numbers
    #initialize a list called even from the filter object using the list() funtion
    even=list(filter(lambda i: i%2==0, range(1,21)))
    print(even)
    
    
#49
def Q49():
    
    #squares all the numbers between 1 and 20 both included using the lambda and map functions
    #initialize a squares list using the list() function
    squares=list(map(lambda i: i*i, range(1,21)))
    print(squares)
    
    
    
#50
class  American():
    def __init__(self):
        self.nationality="American"
    #initialize a static method printNationality that expects an arg and prints it
    @staticmethod
    def printNationality(nationality):
        print(nationality)
Trump=American()
American.printNationality("Kenyan")



#51
class  American():
    def __init__(self):
        self.nationality="American"
    
    #initialize a static method printNationality that expects an arg and prints it
    @staticmethod
    def printNationality(nationality):
        print(nationality)

# creating a subclass of American called NewYorker
class NewYorker(American):
    def __init__(self,city):
        self.city=city
        
    def hood(self):
        return self.city
        
        
Curtis_Jackson=NewYorker("New York City")
Curtis_Jackson.hood()



#52
class circle():
    def __init__(self,r):
        self.r=r
        self.perimeter=3.142*r*2
     
    #initialize a class method radius
    @classmethod
    def radius(self,r):
        self.area=3.142*r*r
        return self(r)
    
    #def calc_area(self,r):
        
#initialize class objects using the class method       
mycircle=circle.radius(7)
Hiscircle=circle.radius(8)

print("My circle radius is ", mycircle.r,"cm while perimetr is ",mycircle.perimeter, "cm and area is ",mycircle.area," square cm", sep="")
print("His circle radius is ",Hiscircle.r,"cm while perimeter is ",Hiscircle.perimeter,"cm", sep="")




#53
class Rectangle():
    def __init__(self,l,w):
        self.perim=(l+w)*2
        self.l=l
        self.w=w
        
    #initialize a class method that claculates the area and instantiates a class object ones it's called
    @classmethod   
    def from_l_w(self,l,w):
        self.area=l*w
        return self(l,w)

#instantiate a class object using the from_l_w class method
fst=Rectangle.from_l_w(7,6)
print(fst.area)



#54
class Shape():
    def __init__(self):
        self.area=0           
    
    #initialize a function areas that prints the ares
    def areas(self):
        print(self.area)
        
# creates a subclass of Shape called Square
class Square(Shape):
    def __init__(self,l):
        self.l=l
        self.w=l
    
    # initialize a method that calculates the area of the square and prints it
    def areas(self):
        print(self.l*self.w)
        
#instantiate a Square object with a length of 5
myshape=Square(5)
myshape.areas()



#55
def cstm_err(x):
    
    #raises an exception if the args passed are not numeric
    #otherwise prints the args
    if not str(x).isnumeric():
        raise Exception("Only numbers are allowed")
    else:
        print(x)
        
cstm_err(5)




#06.ipynb Exercise

#function to calculate %GC content after verifying a sequence is a valid dna sequence
def percentageGC():
    
    #prompt for the user to enter a DNA sequence
    user_seq=input("Enter a DNA sequence to calculate its %GC content").upper()
    
    # Function that verifies the given sequence is a DNA
    def verifier(seq):
        for i in seq:
            if i =="A" or i =="T" or i =="G" or i =="C":
                continue
            else:
                return False
        return True
    
    #calculates %GC content on conditoin that the DNA sequence is valid
    if verifier(user_seq):
        return (user_seq.count("G")+user_seq.count("C"))/len(user_seq)*100
    
    else:
        print("The Sequence you entered is not a DNA sequence")
        


#07.ipynb Exercise 1
import urllib.request
import time
from pathlib import Path

def read_write(filein,fileout):
    path = Path(filein)
    if not path.is_file():
        flag=False
        url = "https://www.uniprot.org/docs/humchrx.txt"
        destination_filename = filein
        urllib.request.urlretrieve(url, destination_filename)
        time.sleep(5)
        if not path.is_file():
            time.sleep(5)
        else:
            flag=True
    if flag:
        gene_list=[]
        with open(filein, "r") as filein:
            flag=False
            for line in filein:
                if line.startswith("name"):
                    flag=True
                    pass
                if flag:
                    line=line.split()

                    if len(line) > 0:
                        gene_list.append(line[0])

        gene_list=gene_list[1:-7]
        with open(fileout, 'w') as outputfile:
            for i in gene_list:
                outputfile.write(i+"\n")
    else:
        print("Input File not Found!")
                

                
                
                
#07.ipynb Exercise 2 (a)
import myscript
#myscript.read_write("huchrx.txt","gen_names.txt")
