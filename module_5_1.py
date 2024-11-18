class House:
    def __init__(self, name, number_of_floors):
        self.name = name            # атрибут имени дома
        self.number_of_floors = number_of_floors  # атрибут  количества этажей
        self.say_info()

    def go_to(self, new_floor):
        if self.number_of_floors < new_floor or new_floor < 1:
            print("Такого этажа не существует")
        else:
            for floor in range(1, new_floor + 1):
                print(floor)
    def say_info(self):
        print(f'Название дома:', self.name, '- количество этажей:',  self.number_of_floors)


# Примеры использования
h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h3 = House('Городской совет', 4)

h1.go_to(5)
h2.go_to(10)
h3.go_to(6)
