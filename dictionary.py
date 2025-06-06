def keyword(**kwargs):
    print(kwargs)
    for key,value in kwargs.items():
        print(key,":",value)


keyword(name="pradeep",age=23,place="tirur",eng=45)
keyword(name="shibili",age=22,place="pmna",malayalam=45)

capitals={"india":"new delhi","russia":"moscow"}
for k,v in capitals.items():
    print(k,":",v)

car={"brand":"ford","model":"mustang","year":1964}   
for k,v in car.items():
    print(k,":",v)

def key(**abcd):
    print(abcd) 
    for k,v in abcd.items():
        print(k,":",v)

key(nam="adil",age=21,mark=82)
key(name="shaheel",age=22,mark=71)



def square(list):
    ss=[]
    for i in list:
        ss.append(i **2) 
    return ss    
square(2,3,4)