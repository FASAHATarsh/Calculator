def e_devide(x,list):
    a="0"
    b="0"
    n=0
    m=int(x)+1
    while n<x:
        a = a + list[n]
        #print(a,",",n)
        n +=1
        
    while m<int(len(list)):
        b = b + list[m]
        #print(b,",",m)
        m +=1
    c = int(a)/int(b)
    print(c)
def e_multiply(x,list):
    a="0"
    b="0"
    n=0
    m=int(x)+1
    while n<x:
        a = a + list[n]
        #print(a,",",n)
        n +=1
        
    while m<int(len(list)):
        b = b + list[m]
        #print(b,",",m)
        m +=1
    c = int(a)*int(b)
    print(c) 
def e_add(x,list):
    a="0"
    b="0"
    n=0
    m=int(x)+1
    while n<x:
        a = a + list[n]
        #print(a,",",n)
        n +=1
        
    while m<int(len(list)):
        b = b + list[m]
        #print(b,",",m)
        m +=1
    c = int(a)+int(b)
    print(c) 
def e_subtract(x,list):
    a="0"
    b="0"
    n=0
    m=int(x)+1
    while n<x:
        a = a + list[n]
        #print(a,",",n)
        n +=1
        
    while m<int(len(list)):
        b = b + list[m]
        #print(b,",",m)
        m +=1
    c = int(a)-int(b)
    print(c) 
print("""Welcome to calculator by Fasahat.
Write 2 number expression to get the result.
Use -->
+ for addition
- for subtraction
* for multiplication
/ for division
^ for exponent""")
while 1>0:
    e= input("Enter expression : ") 
    l = list(e)
    #print(l)
    t_no = len(l)
    no = 0
    while no < t_no:
        i = id(str(l[no]))
        d=id("/")
        m=id("*")
        a=id("+")
        s=id("-")
        if(i==d):
            e_devide(no,l)
        elif(i==m):
            e_multiply(no,l)
        elif(i==a):
            e_add(no,l)
        elif(i==s):
            e_subtract(no,l)
        no +=1
