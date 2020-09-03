import eel, sqlite3

def connect():
    a = {}
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    for row in c.execute('SELECT identificationcode, phonenumber, name, dateofapplicationcompletion, dateandtimeofreceipt, department, product FROM data'):
        a[str(row[0])] = row
    return a
    conn.close()

def createTable(mess):
    line = []
    for k, v in mess.items():
        line.append('</td><td>'.join(map(str, v)))
    print('<tr><td>' + str(line[0]) + '</td></tr><tr><td>' + str(line[1]) + '</td></tr>')
    eel.addTable('<td>' + str(line[0]) + '</td>')

@eel.expose
def load():
    a = connect()
    print(a)
    createTable(a)
    
eel.init("web")
eel.start("main.html", size=(900, 700))




