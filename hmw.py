import sqlite3


try:
    connection = sqlite3.connect("ma'lumotlar.db")
    cursor = connection.cursor()
    print("Ma'lumotlar bazasiga muvaffaqiyatli ulandik!")
except sqlite3.Error as error:
    print("Xatolik: Ma'lumotlar bazasiga ulanishda xatolik yuz berdi:", error)


def create_table():
    try:
        cursor.execute('''CREATE TABLE IF NOT EXISTS nom (
                            id INTEGER PRIMARY KEY,
                            nom TEXT,
                            narx REAL
                        )''')
        connection.commit()
        print("Jadval muvaffaqiyatli yaratildi!")
    except sqlite3.Error as error:
        print("Xatolik: Jadval yaratishda xatolik yuz berdi:", error)

# Ma'lumot qo'shish
def insert_data(nom, narx):
    try:
        cursor.execute("INSERT INTO nom (nom, narx) VALUES (?, ?)", (nom, narx))
        connection.commit()
        print("Ma'lumotlar bazasiga ma'lumot muvaffaqiyatli qo'shildi!")
    except sqlite3.Error as error:
        print("Xatolik: Ma'lumot qo'shishda xatolik yuz berdi:", error)

# Ma'lumot o'chirish
def delete_data(id):
    try:
        cursor.execute("DELETE FROM nom WHERE id=?", (id,))
        connection.commit()
        print("Ma'lumotlar bazasidan ma'lumot muvaffaqiyatli o'chirildi!")
    except sqlite3.Error as error:
        print("Xatolik: Ma'lumot o'chirishda xatolik yuz berdi:", error)

# Ma'lumotni yangilash
def update_data(id, nom, narx):
    try:
        cursor.execute("UPDATE nom SET nom=?, narx=? WHERE id=?", (nom, narx, id))
        connection.commit()
        print("Ma'lumotlar bazasidagi ma'lumot muvaffaqiyatli yangilandi!")
    except sqlite3.Error as error:
        print("Xatolik: Ma'lumot yangilashda xatolik yuz berdi:", error)

# Barcha ma'lumotlarni tanlash
def select_all_data():
    try:
        cursor.execute("SELECT * FROM nom")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as error:
        print("Xatolik: Ma'lumotlarni tanlashda xatolik yuz berdi:", error)

# Biror ma'lumotni tanlash
def select_one_data(id):
    try:
        cursor.execute("SELECT * FROM nom WHERE id=?", (id,))
        row = cursor.fetchone()
        print(row)
    except sqlite3.Error as error:
        print("Xatolik: Ma'lumotni tanlashda xatolik yuz berdi:", error)

# Jadvalni yopish
def close_connection():
    try:
        cursor.close()
        connection.close()
        print("Ulanish yopildi!")
    except sqlite3.Error as error:
        print("Xatolik: Ulanish yopilishda xatolik yuz berdi:", error)

# Test qismi
create_table()
insert_data("Olma", 2.5)
insert_data("Banana", 3.0)
select_all_data()
select_one_data(1)
update_data(1, "Anor", 4.0)
select_all_data()
delete_data(2)
select_all_data()

# Ulanishni yopish
close_connection()
