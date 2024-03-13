#a=7,8
#print(a)
#print(type(a))

'''
a,b=c=7,8
print(a)
print(b)
print(c)
'''
#a=b,c=4,2
#print(a,b,c)
                     #------->swapping of variables
#a=7
#b=5
                 #c=a
                 #a=b
                 #b=c
                 #print(a,b)

#eg:2
'''
a=a+b
b=a-b
a=a-b
print(a,b)
'''
#a,b=b,a
#print(a,b)       #only in python#

#----->id().....>used to find the memory adress of the variable
'''
print(id(a))
print(id(b))
'''
#......>keywords
#keywords are reserved words which is provides special meaning to compiler or interpretor
'''
import keyword
print(keyword.kwlist)
print(type(keyword.kwlist))
print(len(keyword.kwlist))
'''
#to check of the string is keyword or not
#print(keyword.iskw("if"))
'''
----->literals
literal is the constant value assigned to a variable
a variable is consider to be constant when it is defines in caps
 a=78    #a is variable
 A=78   #A is constant
'''
'''
# hash()....>it creats a hash value for constant datatypes and provides error for non constant datatypes
n1=89+7j
print(hash(n1))

f1=[7,8,9]
print(hash(f1))
#error ...>list is non -constant or mutable datatype
'''
"""
a=3
b=3
print(id(a))
print(id(b))
"""

#-----> operators
# ? operators are symboles which is used to perform various operations between 2or more operands
'''
arithmatic operator
logical operator
relational or comparison operator
bitwise operator
identity operator
membership operator
'''
# * --->arithmatic operation  ===>+ , - , * , / , % , // , **
#eg:1
a=8
b=5
c=9
print(a+b+c)


 #input()---->used to get the runtime input
#eval()--->used to get the runtime values of all data type
'''
n1=int(input("enter the value:"))
print(n1)


n1=eval(input("enter the value:"))
print(n1)
'''

a=4
b=2
print(a/b)          #is used to get the quotient value
print(a%b)       #is used to get the remainder value

#   // ----> floor division

a=20
b=10
print(a//b)  #----->the output will be inn integer & the output will be based on floor value

#   **   ----->used for power of a number
print(2**4)  #...>16

#assignme      ----->   +-=  ,   -=  ,  /=  ,  *=  ,  //=  ,  **=  ,  &=  ,  |=

a=3
a+=2
print(a)

# comparison  ----->==,  >  ,  <  ,  !=  , <= , >=

a=8
b=7
print(a>b)

a=9
b=5
print(a==b)

#bitwise operator ---->& ,  |  ,^  ,  ~  ,  << ,  >>
a=7
b=4
print(a&b)

#AND
# A    B     A&B
#0    0       0
# 0    1       0
#1    0       0
#1    1       1


# ~ --->
#a=9876
#print(~a)



#a=9

# 128   64   32   16   8   4   2    1
#    0       0     0      0   0   0   0    1     # ---->     9


#Logical --->
# and, or , not
a=6
#print(a>3 and a<10)
#print(a>7 or a<30)
#print(not(a>8 and a<10))


# Identity operator  --> it is used to compare the memoryu location that the values are stored

# is, is not
a=8
b=8
# print( a is b)
#print(a==b)

a=[1,2,3]
b=[1,2,3]
print(a is not b)


#!---> membership operators  (in, not in)
'''
l1=[5,8,20,556,5]
num1=20
num2=8
print(num1 in l1)----> true
print(num2 not in l1)----> false
'''


# !---> conditional statement (if,elif,else)
'''
#python syntax:---> if condition
                        statement
                        statement
                       
'''

#eg:
'''
a=10
if a>56:
     print("yes")
else:
    print("no")--------(NO)
'''


'''a=0
if a:
    print("yes")
else:
        print("no")-------> (no)

'''

n=int(input("enter a number"))
if  (n/2==0):

    print("it is even")
else:
     print("it is odd")

