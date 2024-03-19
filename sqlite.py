import sqlite3
import tkinter

connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

# Создание таблиц
cursor.execute('''
CREATE TABLE IF NOT EXISTS Tooted (
toote_id INTEGER PRIMARY KEY,
toote_nimi TEXT NOT NULL,
kategooria_id INTEGER,
brandi_id INTEGER,
FOREIGN KEY(kategooria_id) REFERENCES Kategooriad(kategooria_id),
FOREIGN KEY(brandi_id) REFERENCES Brandid(brandi_id)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Kategooriad (
kategooria_id INTEGER PRIMARY KEY,
kategooria_nimi TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Brandid (
brandi_id INTEGER PRIMARY KEY,
brandi_nimi TEXT NOT NULL
)
''')

def add_category():
    category_name = input("Введите название категории: ")
    cursor.execute('''INSERT INTO Kategooriad(kategooria_nimi) VALUES(?)''', (category_name,))
    connection.commit()
    print("Категория успешно добавлена!")

def add_brand():
    brand_name = input("Введите название бренда: ")
    cursor.execute('''INSERT INTO Brandid(brandi_nimi) VALUES(?)''', (brand_name,))
    connection.commit()
    print("Бренд успешно добавлен!")

def add_product():
    product_name = input("Введите название товара: ")
    category_id = input("Введите ID категории товара: ")
    brand_id = input("Введите ID бренда товара: ")
    cursor.execute('''INSERT INTO Tooted(toote_nimi, kategooria_id, brandi_id) VALUES(?, ?, ?)''', (product_name, category_id, brand_id))
    connection.commit()
    print("Товар успешно добавлен!")
    
def delete_product():
    product_id = input("Введите ID товара, который хотите удалить: ")
    cursor.execute('''DELETE FROM Tooted WHERE toote_id = ?''', (product_id,))
    connection.commit()
    print("Товар успешно удален!")

def view_data():
    cursor.execute('''SELECT * FROM Tooted''')
    products = cursor.fetchall()
    print("Список товаров:")
    for product in products:
        print(product)

while True:
    print("\nМеню:")
    print("1. Добавить новую категорию")
    print("2. Добавить новый бренд")
    print("3. Добавить новый товар")
    print("4. Удалить товар")
    print("5. Просмотреть данные")
    print("6. Выход")
    
    choice = input("Выберите действие: ")

    if choice == '1':
        add_category()
    elif choice == '2':
        add_brand()
    elif choice == '3':
        add_product()
    elif choice == '4':
        delete_product()
    elif choice == '5':
        view_data()
    elif choice == '6':
        break
    else:
        print("Неверный ввод. Пожалуйста, выберите номер действия из меню.")

connection.close()



