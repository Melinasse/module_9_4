from random import choice
# Функциональное разнообразие

first = 'Мама мыла раму'
second = 'Рамена мало было'
result_one = map(lambda i,y: i == y,first, second)
print(list(result_one))

# Замыкание
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'w', encoding='utf-8') as file:
            for i in data_set:
                file.write(f"{i}\n")
            # return file
        with open(file_name, 'r', encoding='utf-8') as file:  # Добавил блок для чтения фала поле записи
            box = file.read()
            print(box)
            return box
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


# Метод __call__:

class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)

first_ball = MysticBall('Это строчка', 'А', 'это', 'уже', 'число', 5, 'в', 'списке')
print(first_ball())
print(first_ball())
print(first_ball())
print(first_ball())
print(first_ball())
print(first_ball())
print(first_ball())
print(first_ball())
