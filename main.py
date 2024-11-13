 import pandas as pd
import matplotlib.pyplot as plt

# Завантаження даних
file_path = 'comptagevelo2010.csv'
df = pd.read_csv(file_path, sep=',', encoding='latin1')

# Об'єднуємо дату і час у єдиний стовпець та перетворюємо на datetime
df['DateTime'] = pd.to_datetime(df['Date'] + ' ' + df['Unnamed: 1'], dayfirst=True)
df.set_index('DateTime', inplace=True)

# Видаляємо зайві колонки та рядки з усіма пропусками
df.drop(columns=['Date', 'Unnamed: 1'], inplace=True)
df.dropna(how='all', inplace=True)

# Виведення таблиці
print("\nДані:")
print(df.head(10).to_string()) 

# Створюємо стовпець місяць-рік
df['Year-Month'] = df.index.to_period('M')

# Групуємо по місяцях і рахуємо суму для кожного місяця
monthly_counts = df.groupby('Year-Month').sum()

# Знаходимо місяць з найбільшою кількістю велосипедистів
most_popular_month = monthly_counts.sum(axis=1).idxmax()

print(f"\nМісяць з найбільшою кількістю велосипедистів: {most_popular_month}")

# Побудова графіку
plt.figure(figsize=(15, 10))
df.plot(figsize=(15, 10))

plt.title("Кількість велосипедистів за різними станціями")
plt.xlabel("Дата")
plt.ylabel("Кількість велосипедистів")
plt.legend(loc='upper left')
plt.grid(True)

# Виведення графіка
plt.show()
