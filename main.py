lines = ["Сегодня хороший день","Компьютеры изменили мир","Вода расслабляет мысли",
"Солнце встает над горизонтом","Вдохновенье приходит внезапно","Я люблю изучать программирование"]
count = 0
for i in lines:
    if "б" in i.lower():
        count +=1
print("Количество строк сожержащих букву б:",count)