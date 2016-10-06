#Morse Code

morse = {
'a': '.-',
'b': '-...',
'c': '-.-.',
'd': '-..',
'e': '.',
'f': '..-.',
'g': '--.',
'h': '....',
'i': '..',
'j': '.---',
'k': '-.-',
'l': '.-..',
'm': '--',
'n': '-.',
'o': '---',
'p': '.--.',
'q': '--.-',
'r': '.-.',
's': '...',
't': '-',
'u': '..-',
'v': '...-',
'w': '.--',
'x': '-..-',
'y': '-.--',
'z': '--..'
}

morserev = {
'.-': 'a',
'-...': 'b',
'-.-.': 'c',
'-..': 'd',
'.': 'e',
'..-.': 'f',
'--.': 'g',
'....': 'h',
'..': 'i',
'.---': 'j',
'-.-': 'k',
'.-..': 'l',
'--': 'm',
'-.': 'n',
'---': 'o',
'.--.': 'p',
'--.-': 'q',
'.-.': 'r',
'...': 's',
'-': 't',
'..-': 'u',
'...-': 'v',
'.--': 'w',
'-..-': 'x',
'-.--': 'y',
'--..': 'z'
}




choice = raw_input("1. Word-->Morse  2. Morse-->Word: ")

if choice == "1":
    word = raw_input("Enter your word: ")
    array = list(word)
    newarray =[]
    for i in array:
         newarray.append(morse[i])
    print ' '.join(newarray)

if choice == "2":
    num = raw_input("Number of codes: ")
    array = []
    newarray = []
    num = int(num)
    for i in range(0,num,1):
        code = raw_input("Input code here: ")
        array.append(code)
    for i in array:
        newarray.append(morserev[i])
    print ' '.join(newarray)
