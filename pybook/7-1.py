#from typing import Tuple


#flag = True
#while flag:
#    a = input()
#    if a != 'q':
#        print("plz "+a)
#    else:
#        flag = False

#i = 0
#while True:
#    i += 1
#    print(i)

sw = ['a','b','c','a','a']
nsw = []
while sw:
    a = sw.pop()
    nsw.append(a)
    print(a)
print(nsw)

while 'a' in nsw:
    nsw.remove('a')
print(nsw)