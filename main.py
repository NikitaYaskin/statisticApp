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
    for k, v in mess.items():
        row = '<tr><td>' + str('</td><td>'.join(map(str, v))) + '</td><input type="checkbox"></tr>'
        eel.addTable(row)
    

@eel.expose
def load():
    a = connect()
    createTable(a)
    
eel.init("web")
eel.start("main.html", size=(900, 700))




