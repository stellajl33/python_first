#Rectangular

array = ["My Brain", "Hurts", "from", "this", "exercise"]
arraylength = []
arraynew= []

for i in array:
    leng = len(i)
    global leng
    arraylength.append(leng)
    maxindex = max(arraylength)
    global maxindex

maxlength = maxindex + 6
print "*" * maxlength

leng = int(leng)
maxlength = int(maxlength)

spaces = maxlength-leng


for i in array:
    rightgap = (maxindex-len(i)) + 2
    print "*" + " " * (2) + i + " " * rightgap + "*"

print "*" * maxlength
