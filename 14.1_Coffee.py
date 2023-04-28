con = "IHateRabbits"
FILENAME = "coffeehouse_supplies.csv"
try:
    File = open(FILENAME, 'r')
    file = File.readlines()
    File.close()

    data = []
    c = 0
    for i in file:
        c += 1
        i = i.strip('\n')
        i = i.split(',')
        data.append(i)
    try:
        import sqlite3
        con = sqlite3.connect('coffee.db')
        cur = con.cursor()
        table = '''CREATE TABLE IF NOT EXISTS Coffee
                (ProductID INTEGER PRIMARY KEY NOT NULL, Product TEXT, 
                Category TEXT, Supplier TEXT)'''
        cur.execute(table)
        con.commit()

        for i in data:
            cur.execute('''INSERT INTO Coffee (Product, Category, Supplier)
            VALUES (?, ?, ?)
            ''', (i[0], i[1], i[2]))
        con.commit()
        print(f"{c} records added")
    except sqlite3.Error:
        print("SQL error encountered")
except IOError:
    print(f"Unable to add data from {FILENAME}")
finally:
    if con != "IHateRabbits":
        con.close()
