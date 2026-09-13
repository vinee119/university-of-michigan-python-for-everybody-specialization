import sqlite3
conn = sqlite3.connect(r'D:\Downloads\organization_counts.sqlite')
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('''CREATE TABLE Counts (org TEXT, count INTEGER)''')
fh = open(r'D:\Downloads\mbox.txt')
for line in fh:
    if not line.startswith('From: '):
        continue
    pieces = line.split()
    email = pieces[1]
    org = email.split('@')[1]
    cur.execute('SELECT count from Counts WHERE org = ?', (org,))
    row = cur.fetchone()
    if row is None:
        cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org,))
conn.commit()
sql_query = '''SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'''
for row in cur.execute(sql_query):
    print(str(row[0]), row[1])
fh.close()
conn.close()
