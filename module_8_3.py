class Car:
    def __init__(self, model, vin, numbers):
        self.model = model
        if self.__is_valid_vin(vin) and self.__is_valid_numbers(numbers):
            self.__vin = vin
            self.__numbers = numbers
            print(f'{self.model} успешно создан.')
        else:
            pass

    def __is_valid_vin(self, vin_number):
        try:
            if type(vin_number) != int:
                raise IncorrectVinNumber('Некорректный тип vin номер')
            if vin_number >= 9999999 or vin_number <= 1000000:
                raise IncorrectVinNumber('Неверный диапозон для vin номера')
        except IncorrectVinNumber:
            pass
        else:
            return True

    def __is_valid_numbers(self, numbers):
        try:
            if type(numbers) != str:
                raise IncorrectCarNumber('Некорректный тип данных для номеров')
            if len(numbers) != 6:
                raise IncorrectCarNumber('Неверная длина номера')
        except IncorrectCarNumber:
            pass
        else:
            return True

class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message
        print(self.message)

class IncorrectCarNumber(Exception):
    def __init__(self, message):
        self.message = message
        print(self.message)


f = Car('Model1', 1000000, 'f123dj')
s = Car('Model2', 1200300, 'т001тр')
t = Car('Model3', 2020202, 'к551уф')
f = Car('Model4', 4089273, 'нет номера')