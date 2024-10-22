#Cтрока открывает файл с именем text.txt в режиме чтения
with open('text.txt', 'r') as file:
    #Читаем и сохраняем содержимое файла в переменной sentences
    sentences = file.read() 
    #Cтрока разбивает строку sentences на отдельные слова
    words = sentences.split() 
#Вывод результата
print("Количество слов в файле: " + str(len(words)))
