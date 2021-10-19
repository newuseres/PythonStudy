'''
def makesmz(*a):
    ss=''
    for sc in a:
        ss+=str(sc)
    print(ss)

makesmz(1,2,3)

makesmz(233,0)


'''


def make_user(first,second,a):
    usr = {}
    usr["firstname"]=first
    usr["secondname"]=second
    for key,value in a.items():
        usr[key] = value
    return usr

wow = {'location' : 5,'field' : "pythics"}

nusr = make_user("luo","jhao",wow)

print(nusr)
a = [1,2]
