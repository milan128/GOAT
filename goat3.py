__author__ = 'root'
# x = 10
# ans = 0
# itersleft = x
#
# while (itersleft != 0):
#     ans = ans + x
#     itersleft = itersleft -1
#
# print (str(x) + 'x'+ str(x) + '=' + str(ans))



# x =  int(raw_input("Enter the number you want to multiplication table for:    "))
# ans = 0
# iterleft = 0
# iterright = str(x)
#
# while (iterleft < 100):
#
#     iterleft = iterleft + 1
#
#     ans = iterleft * x
#     print (str(iterright) + ' x '+  str(iterleft) + ' = ' + str(ans))


chesscount = 0
ans = 0

while (chesscount < 64):
    ans = chesscount ** chesscount
    chesscount = chesscount + 1

    print str(ans)

