#Multiplication Table


for i in range(0,13,1):
    global i
    for j in range(0,13,1):
        global j
        print "%s x %s = %s" % (i, j, (i*j))
