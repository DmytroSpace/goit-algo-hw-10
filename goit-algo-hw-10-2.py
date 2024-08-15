import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt


a, b = -2.5, 3                                                   # Встановлюємо межі інтегрування
num_samples = 100000

def f(x):                                                        # Визначаємо функцію для інтегрування
    return (x ** 2) / 5 + np.sqrt(3)

def visualize_results(x_random, y_random):                       # Створюємо діапазон значень для x
    x = np.linspace(a - 1, b + 1, 400)
    y = f(x)

    _, ax = plt.subplots()

    ax.plot(x, y, "r", linewidth=2)
    ax.scatter(x_random, y_random, color="red", s=0.5)

    ix = np.linspace(a, b)                                       # Заповнюємо область під графіком у наших межах сірим кольором
    iy = f(ix)
    ax.fill_between(ix, iy, color="gray", alpha=0.3)

    ax.set_xlim([x[0], x[-1]])
    ax.set_ylim([0, max(y) + 0.1])
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")

    ax.axvline(x=a, color="gray", linestyle="--")                # Додаємо межі інтегрування та назву графіка
    ax.axvline(x=b, color="gray", linestyle="--")
    ax.set_title(f"Графік інтегрування f(x) від {a} до {b}")
    
    plt.grid()
    plt.show()

def monte_carlo(a, b, num_samples):                              # Обчислюємо інтеграл методом Монте-Карло

    x_random = np.random.uniform(a, b, num_samples)
    y_random = np.random.uniform(0, f(b), num_samples)

    under_curve = np.sum(y_random < f(x_random))                 # Кількість точок під кривою

    area_under_curve = (b - a) * f(b) * under_curve / num_samples      # Площа під кривою

    result = spi.quad(f, a, b)[0]                                      # Обчислюємо інтеграл за допомогою функції quad

    print(f'Площа обчислена методом Монте-Карло: {area_under_curve}')
    print(f'Площа обчислена функцією quad: {result}\n')
    visualize_results(x_random, y_random)

if __name__ == "__main__":
    for density in [100, 1000, 10000, 100000]:
        print(f"\n\tResults for points amount: {density}")
        monte_carlo(a, b, density)
