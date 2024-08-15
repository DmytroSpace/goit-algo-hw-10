import pulp as pl

model = pl.LpProblem("Maximize Production", pl.LpMaximize)                       # Ініціалізаємо моделі         

water_available = 100                                                            # Встановлюємо константи
sugar_available = 50  
lemon_juice_available = 30  
fruit_puree_available = 40   

water_per_lemonade = 2                                                           # Вказуємо потрібні ресурси для виробництва одиниці напою
sugar_per_lemonade = 1
lemon_juice_per_lemonade = 1
fruit_puree_per_juice = 2
water_per_juice = 1

lemonade = pl.LpVariable('Lemonade', lowBound=0, cat='Integer')                  # Вводимо невідомі змінні
fruit_juice = pl.LpVariable('Fruit_Juice', lowBound=0, cat='Integer')

                                                                                 # Вказуємо обмеження ресурсів
model += water_per_lemonade * lemonade + water_per_juice * fruit_juice <= water_available, "Water"
model += sugar_per_lemonade * lemonade <= sugar_available, "Sugar"
model += lemon_juice_per_lemonade * lemonade <= lemon_juice_available, "Lemon_Juice"
model += fruit_puree_per_juice * fruit_juice <= fruit_puree_available, "Fruit_Puree"


total_production = lemonade + fruit_juice                                        # Визначаємо цільову функцію: 
model += total_production, "Total_Production"                                    # максимальна загальна кількість вироблених напоїв

model.solve()                                                                    # Наше розв'язання проблеми

# Результати
print("Кількість виробленого лимонаду:", lemonade.varValue)
print("Кількість виробленого фруктового соку:", fruit_juice.varValue)
print("Загальна кількість вироблених напоїв:", lemonade.varValue + fruit_juice.varValue)
