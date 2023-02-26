from module import *

print("переводчик")

f=open('rus.txt','r',encoding="utf-8-sig")
rus_words=[]
for rida in f:
    rus_words.append(rida.strip())
f.close()

f=open('eng.txt','r')
eng_words=[]
for rida in f:
    eng_words.append(rida.strip())
f.close()

print(rus_words, eng_words)


while True:
    print("введите слово и получите перевод")
    wor=input("> ")
    alphabet_ru = ["а","б","в","г","д","е","ё","ж","з","и","й","к","л","м","н","о",
                "п","р","с","т","у","ф","х","ц","ч","ш","щ","ъ","ы","ь","э","ю","я"]
    ka=bool(set(alphabet_ru).intersection(set(wor.lower())))
    if ka == True:
        for i in range(len(rus_words)):
            if rus_words[i].lower() == wor.lower():
                print(">", eng_words[i])
                break
            elif rus_words[i].lower() != wor.lower():
                isnot=int(input("this word is not yet in yhe dictionary\nwould you like to add it (1/0)> "))
                if isnot==1:
                    rus_words.append(wor)
                    rus_trans=input("how does it translate> ")
                    eng_words.append(rus_trans)

                    f = open('rus.txt','a',encoding="utf-8-sig") 
                    f.write(wor)
                    f.close()

                    f = open('eng.txt','a') 
                    f.write(rus_trans)
                    f.close()

                    break
                elif isnot==0:
                    break
    elif ka == False:
        for i in range(len(eng_words)):
            if eng_words[i].lower() == wor.lower():
                print(">", rus_words[i])
                break
            elif eng_words[i].lower() != wor.lower():
                isnot=int(input("this word is not yet in yhe dictionary\nwould you like to add it (1/0)> "))
                if isnot==1:
                    eng_words.append(wor)
                    eng_trans=input("how does it translate> ")
                    rus_words.append(eng_trans)

                    f = open('eng.txt','a') 
                    f.write(wor)
                    f.close()

                    f = open('rus.txt','a',encoding="utf-8-sig") 
                    f.write(eng_trans)
                    f.close()

                    break
                elif isnot==0:
                    break
