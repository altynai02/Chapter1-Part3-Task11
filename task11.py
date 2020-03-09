# 11. Напишите функцию которая подсчитает количество
# строк, слов и букв в текстовом файле.

def count():
    stroka = 0
    word = 0
    letter = 0
    space = 0
    first_step = open("file.txt", "r" )
    
    for i in first_step:
      split = i.split()  #Преобразую в строку
      stroka+=1
      word += len(split) 
      letter += len(i)
      
      for words in i:
        if words.isspace():
          space+=1
    letters = letter - space
    first_step.close()
    return stroka, word, letters
print(count())