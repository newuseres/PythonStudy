#li = ['admin','a','b','c','d']
#for usr in li:
#    if usr == 'admin':
#        print("wow,admin!!!")
#    else:
#        print("hello,"+usr+" long time no see.")

#while li:
#    li.pop()

#if (not li):
#    print("wtf")

#current = ['a','b','c','d','e']
#newu = ['a','h','e','g','f']

#current_n = [cr.lower() for cr in current ]
#newu_n = [ nm.lower() for nm in newu ]

#for us in newu_n:
#    if us in current_n:
#        print("o"+us)
#    else :
#        print("nou")

lis = [i for i in range(1,10,1)]
for i in lis:
    if i == 1 :
        print(str(i)+'st')
    elif i == 2 :
        print(str(i)+"nd")
    elif i == 3 :
        print(str(i)+'rd')
    else:
        print(str(i)+'th')