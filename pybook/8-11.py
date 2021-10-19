
def makegreat(magicians,unm):
    while magicians:
        unm.append("great"+magicians.pop())

def show(magicians):
    for magician in magicians:
        print(magician)

magicians = ['a','b','c']
unm = []
show(magicians)
makegreat(magicians,unm)
show(unm)