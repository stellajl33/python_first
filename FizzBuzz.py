#fizzbuzz

for i in range (101):
    if i%3 == 0:
        print str(i) + " Fizz"
    if i%5 == 0:
        print str(i) + " Buzz"
    if i%3 and i%5:
        print str(i) + " Fizz Buzz"
