''' default argument function'''
# def info(name="hii",age=23):
#     print("Name :" ,name)
#     print("Age :", age)
# info()
# info(60)
# info('sha')
# info(name='mohd')
# info(age=44)


''' addition to two numbers '''

# def g(x,y):
#     e = x+y
#     f = x-y
#     print("the sum of x+y is : ",e)
#     print("the diff of x-y is : ",f)
# g(10,15)
# g(23.0,25.3)


''' adding number by return'''

# def j(t,s):
#     v = t+s
#     return v
# z = j(10,20)
# print("the sum is ",z)
# r = j(20,50)
# print("the sum is ",r)


''' even and odd numbers'''

# def dum(n):
#     if n%2==0:
#         print(n,"it is even number")
#     else:
#         print(n,'it is odd number')
# dum(120)                                        # 120 it is even number
# dum(7)                                          # 7 it is odd number
# n=int(input())
# dum(n)                                          # 13 it is odd number



''' filter func'''

# def zec(m):
#     if m%2==0:
#         return True 
#     else:
#         return False
# x =[int(m) for m in input().split()]
# r = list(filter(zec,x))
# print("the values from x is :",r)


''' lambda function '''

# e = lambda a,b,c: a/b/c
# d = lambda p,q,s : p-q-s
# g = e(11,45,12.3)
# r = d(45,78,102)
# print('div =',g)                                # div = 0.01987353206865402
# print('sub=',r)                                 # sub = sub= -135


''' lambda function printing bigger numbers'''
# k = lambda d, e :d if d>e else e #write lambda function
# d,e= [int(n) for n in input("enter two numbers: ").split()]
# print(k(d,e))                                       # Doubt


# r = [int(w) for w in input().split()]                   # 10 20 30
# print("the bigger value is ",max(r))                    # the bigger value is  30                        
# print("the smaller value is ",min(r))                   # the smaller value is  10


# f= [25,3.6,120,25.366562]
# print(max(f))                           # 120
# print(min(f))                           # 3.6


# l = [int(q) for q in input().split()]               # [12 56 23 859 632 547 895 63 25] 
# h = list(filter(lambda q: q%2==0,l))
# j = list(filter(lambda q: q%2!=0,l))
# print("The even number from l is :",h)          # The even number from l is : [12, 56, 632]
# print("The odd numbers from l is :",j)          # The odd numbers from l is : [23, 859, 547, 895, 63, 25]


''' squaring the values'''

# g = lambda c : c**c
# teh = g(5)
# print("the square of 5 is :",teh)             # the square of 5 is : 3125

# ''' map function '''
# o  =[int(d) for d in input().split()]
# f = list(map(lambda d : d**3,o))
# print("the square of d is : ",f)


# from functools import *
# f = [1,2,3,4,5,6]
# r = reduce (lambda x , y:x,f)
# p = reduce (lambda x , y:y,f)
# t = reduce(lambda x,y:x+y,f)
# w = reduce(lambda x,y:x-y,f)
# print(t)
# print(r)                                                    # Doubt
# print(p)
# print(w)
# print(sum(f))


''' def func calling each func at the end'''
# def UG(ug='b.tech'):
#     print(f"My college is {ug}")                # My college is b.tech
#     dip()
# def dip(cg='diploma'):
#     print(f"My diploma clg is {cg}")            # My diploma clg is diploma          
# def scl(sc='stj'):
#     print(f"My school is {sc}")                 #  # My school is stj
#     UG()
# scl()


    