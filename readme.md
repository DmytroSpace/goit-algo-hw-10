#        Результати для 100 вибірок:
# Площа обчислена методом Монте-Карло: 12.627081637058737
# Площа обчислена функцією quad: 12.367946108295492      


#        Результати для 1 000 вибірок:
# Площа обчислена методом Монте-Карло: 12.277408607109416
# Площа обчислена функцією quad: 12.367946108295492


#        Результати для 10 000 вибірок:
# Площа обчислена методом Монте-Карло: 12.617368497337921
# Площа обчислена функцією quad: 12.367946108295492


#        Результати для 100 000 вибірок:
# Площа обчислена методом Монте-Карло: 12.413004037611987
# Площа обчислена функцією quad: 12.367946108295492

# Досліджуючи отримані результати простежується тенденція збільшення точності методу Монте-Карло зі збільшенням тестовий вибірок:
# найбільша розбіжність між аналітичним методом та Монте-Карло з'являється у найменшій кількості тестових вибірок, що можна
# пояснити занадто малою вводною інформацією для точного прогнозування.
# Максимальне наближення до аналітичного розв'язання маємо для тестової вибірки у 100 000, що підтверджує цю тенденцію.

# Практична користь використання методу Монте-Карло стане в нагоді у випадках, коли аналітичне рішення складне або ж взагалі відсутнє
# В той же час треба звернути увагу, що збільшення кількості тестових вибірок напряму збільшує і кількість часу обчислень.

# Тож основним у використанні цього методу є пошук балансу між точністю результатів та ефективністю його роботи, як завжди:
# життя - це пошук компромісів та балансу :)