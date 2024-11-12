# Добавляем путь проекта в sys.path, чтобы Python мог находить модули fake_math и true_math
import sys
sys.path.append(r"H:\My Python Project\MODULE_4\module_4_1")

# Импортируем функцию divide из fake_math и переименовываем ее в fake_divide
from fake_math import divide as fake_divide

# Импортируем функцию divide из true_math и переименовываем ее в true_divide
from true_math import divide as true_divide

# Вызываем функцию fake_divide с произвольными значениями, где второй аргумент не равен нулю
result1 = fake_divide(69, 3)     # Ожидаемый результат: 23.0

# Вызываем функцию fake_divide с делением на ноль
result2 = fake_divide(3, 0)      # Ожидаемый результат: 'Ошибка'

# Вызываем функцию true_divide с произвольными значениями, где второй аргумент не равен нулю
result3 = true_divide(49, 7)     # Ожидаемый результат: 7.0

# Вызываем функцию true_divide с делением на ноль
result4 = true_divide(15, 0)     # Ожидаемый результат: inf

# Выводим результаты на экран
print(result1)  # Должно вывести: 23.0
print(result2)  # Должно вывести: 'Ошибка'
print(result3)  # Должно вывести: 7.0
print(result4)  # Должно вывести: inf
