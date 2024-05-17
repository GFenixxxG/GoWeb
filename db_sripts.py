import sqlite3

db_name = "quiz.db"

conn = None
cursor = None


def open():
    global conn, cursor
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

def close():
    cursor.close()
    conn.close()

def do(query):
    cursor.execute(query)
    conn.commit()

def create():
    open()
    do("""CREATE TABLE quiz(
            id INTEGER PRIMARY KEY,
            name VARCHAR)""")

    do("""CREATE TABLE questions(
            id INTEGER PRIMARY KEY,
            question VARCHAR,
            answer VARCHAR,
            wrong1 VARCHAR,
            wrong2 VARCHAR,
            wrong3 VARCHAR)""")
    
    do("""CREATE TABLE quiz_content(
            id INTEGER PRIMARY KEY,
            quiz_id INTENGER,
            question_id INTENGER,
            FOREIGN KEY (quiz_id) REFERENCES quiz (id),
            FOREIGN KEY (question_id) REFERENCES questions (id))""")

    close()

def clear_db():
    ''' видаляє всі таблиці '''
    open()
    query = '''DROP TABLE IF EXISTS questions'''
    do(query)
    query = '''DROP TABLE IF EXISTS quiz'''
    do(query)
    query = '''DROP TABLE IF EXISTS quiz_content'''
    do(query)
    close()

def add_quizes():
    open()
    quizes = [
        ("Тест по астрономії",),
        ("Тест на логіку",),
        ("Тест на знання географії",),
        ("Тест на знання Книг",),
    ]
    cursor.executemany("""INSERT INTO quiz (name) VALUES (?)""", quizes)
    conn.commit()
    close()
    
def add_question():
    questions = [
        ('Скільки місяців на рік мають 28 днів?', 'Всі', 'Один', 'Жодного', 'Два'),
        ('Яким стане зелена скеля, якщо впаде в Червоне море?', 'Мокрим', 'Червоним', 'Не зміниться', 'Фіолетовим'),
        ('Якою рукою краще розмішувати чай?', 'Ложкою', 'Правою', 'Лівою', 'Любою'),
        ('Що не має довжини, глибини, ширини, висоти, а можна виміряти?', 'Час', 'Дурність', 'Море', 'Повітря'),
        ('Коли сіткою можна витягнути воду?', 'Коли вода замерзла', 'Коли немає риби', 'Коли спливла золота рибка', 'Коли сітка порвалася'),
        ('Що більше слона і нічого не важить?', 'Тінь слона', 'Повітряна куля', 'Парашут', 'Хмара'),
        ("Яка найбільша планета в Сонячній системі?", "Юпітер", "Марс", "Земля", "Венера"),
        ("Яка книга написана Вільямом Шекспіром?", "Гамлет", "Війна і мир", "Преступлення і кара", "Гаррі Поттер і філософський камінь"),
        ("Яка ріка є найдовшою у світі?", "Амазонка", "Ніл", "Міссісіпі", "Дунай"),
        ("Яка столиця Японії?", "Токіо", "Пекін", "Сеул", "Бангкок"),
        ("Як зветься найбільший океан на Землі?", "Тихий", "Індійський", "Атлантичний", "Північний"),
        ("Яка планета відома як 'вечірня зірка'?", "Венера", "Меркурій", "Марс", "Юпітер"),
        ("Хто написав 'Майстра та Маргариту'?", "Михайло Булгаков", "Лев Толстой", "Федор Достоєвський", "Антуан де Сент-Екзюпері"),
        ("Яка країна має найбільшу кількість населення?", "Китай", "Індія", "Сполучені Штати Америки", "Бразилія"),
        ("Який океан знаходиться між Європою та Північною Америкою?", "Атлантичний", "Тихий", "Індійський", "Північний"),
        ("Яка приблизна кількість зірок у Всесвіті?", "Понад 200 млрд триліонів", "100 мільйонів", "Бескінечность", "Ні жодної"),]

    open()
    cursor.executemany("INSERT INTO questions (question, answer, wrong1, wrong2, wrong3) VALUES (?, ?, ?, ?, ?)", questions)
    conn.commit()
    close()

def add_links():
    open()
    cursor.execute("PRAGMA foreign_keys = on")
    answer = input("Connect Link? (y/n): ")
    while answer != "n":
        quiz_id = int(input("Input number victorian: "))
        question_id = int(input("Input number question: "))
        cursor.execute("INSERT INTO quiz_content (quiz_id, question_id) VALUES (?, ?)", [quiz_id, question_id])
        conn.commit()
        answer = input("Connect Link? (y/n): ")
    close()

def main():
    #clear_db()
    #create()
    #add_quizes()
    #add_question()
    add_links()
    pass


main()