def abc():
    print "abc :)"
    def x():
        print "x :D"
    def y():
        print "y :>"
    print x, y


print dir(abc)
print dir(abc.func_code)
abc()