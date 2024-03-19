import sqlite3
import tkinter as tk
from tkinter import messagebox

connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

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
    category_name = category_entry.get()
    if category_name.strip() != "":
        cursor.execute('''INSERT INTO Kategooriad(kategooria_nimi) VALUES(?)''', (category_name,))
        connection.commit()
        messagebox.showinfo("Категория добавлена!")
    else:
        messagebox.showerror("Ошибка", "Введите название категории.")

def add_brand():
    brand_name = brand_entry.get()
    if brand_name.strip() != "":
        cursor.execute('''INSERT INTO Brandid(brandi_nimi) VALUES(?)''', (brand_name,))
        connection.commit()
        messagebox.showinfo("Бренд добавлен!")
    else:
        messagebox.showerror("Ошибка", "Введите название бренда.")

def add_product():
    product_name = product_entry.get()
    category_id = category_id_entry.get()
    brand_id = brand_id_entry.get()
    if product_name.strip() != "" and category_id.strip() != "" and brand_id.strip() != "":
        cursor.execute('''INSERT INTO Tooted(toote_nimi, kategooria_id, brandi_id) VALUES(?, ?, ?)''', (product_name, category_id, brand_id))
        connection.commit()
        messagebox.showinfo("Товар добавлен!")
    else:
        messagebox.showerror("Заполните все поля.")

def delete_product():
    product_id = delete_product_id_entry.get()
    if product_id.strip() != "":
        cursor.execute('''DELETE FROM Tooted WHERE toote_id = ?''', (product_id,))
        connection.commit()
        messagebox.showinfo("Товар удален!")
    else:
        messagebox.showerror("Введите ID товара для удаления.")

def view_data():
    cursor.execute('''SELECT * FROM Tooted''')
    products = cursor.fetchall()
    product_list.delete(0, tk.END)
    for product in products:
        product_list.insert(tk.END, product)

root = tk.Tk()
root.title("Database")
root.configure(bg="#333") 

button_frame = tk.Frame(root, bg="#333")
button_frame.pack(side=tk.TOP, padx=10, pady=10)

add_category_button = tk.Button(button_frame, text="Добавить категорию", command=add_category, bg="white")
add_category_button.pack(side=tk.LEFT, padx=5)

add_brand_button = tk.Button(button_frame, text="Добавить бренд", command=add_brand, bg="white")
add_brand_button.pack(side=tk.LEFT, padx=5)

add_product_button = tk.Button(button_frame, text="Добавить товар", command=add_product, bg="white")
add_product_button.pack(side=tk.LEFT, padx=5)

delete_product_button = tk.Button(button_frame, text="Удалить товар", command=delete_product, bg="white")
delete_product_button.pack(side=tk.LEFT, padx=5)

view_data_button = tk.Button(button_frame, text="Просмотреть данные", command=view_data, bg="white")
view_data_button.pack(side=tk.LEFT, padx=5)

category_label = tk.Label(root, text="Название категории:", bg="#333", fg="white")  
category_label.pack(pady=(20,0))

category_entry = tk.Entry(root)
category_entry.pack(pady=(0,10))

brand_label = tk.Label(root, text="Название бренда:", bg="#333", fg="white")
brand_label.pack()

brand_entry = tk.Entry(root)
brand_entry.pack()

product_label = tk.Label(root, text="Название товара:", bg="#333", fg="white")
product_label.pack()

product_entry = tk.Entry(root)
product_entry.pack()

category_id_label = tk.Label(root, text="ID категории:", bg="#333", fg="white")
category_id_label.pack()

category_id_entry = tk.Entry(root)
category_id_entry.pack()

brand_id_label = tk.Label(root, text="ID бренда:", bg="#333", fg="white")
brand_id_label.pack()

brand_id_entry = tk.Entry(root)
brand_id_entry.pack()

delete_product_id_label = tk.Label(root, text="ID товара для удаления:", bg="#333", fg="white")
delete_product_id_label.pack()

delete_product_id_entry = tk.Entry(root)
delete_product_id_entry.pack()

product_list = tk.Listbox(root, height=10, width=50, bg="white", fg="black")  
product_list.pack(padx=10, pady=10)

root.mainloop()

connection.close()
