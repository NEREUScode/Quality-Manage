import sqlite3

class Erreur:
    def __init__(self, db_path='datbase.db'):
        self.conn = sqlite3.connect(db_path)
        self.create_table()

    def create_table(self):
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS Erreur (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nSerie TEXT,
                    debitActuel REAL,
                    temperature REAL,
                    indexInitial INTEGER,
                    indexFinal INTEGER,
                    volumeIndique REAL,
                    volumeReel REAL,
                    erreur REAL,
                    emt TEXT
                )
            ''')

    def insert(self, nSerie, debitActuel, temperature, indexInitial, indexFinal, volumeIndique, volumeReel, erreur, emt):
        with self.conn:
            self.conn.execute('''
                INSERT INTO Erreur (nSerie, debitActuel, temperature, indexInitial, indexFinal, volumeIndique, volumeReel, erreur, emt)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (nSerie, debitActuel, temperature, indexInitial, indexFinal, volumeIndique, volumeReel, erreur, emt))

    def delete_by_id(self, record_id):
        with self.conn:
            self.conn.execute('DELETE FROM Erreur WHERE id = ?', (record_id,))

    def update_by_id(self, record_id, **kwargs):
        columns = ', '.join(f"{k} = ?" for k in kwargs.keys())
        values = list(kwargs.values())
        values.append(record_id)
        query = f'UPDATE Erreur SET {columns} WHERE id = ?'
        with self.conn:
            self.conn.execute(query, values)

    def get_all_records(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM Erreur')
        return cursor.fetchall()

    def find_by_id(self, record_id):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM Erreur WHERE id = ?', (record_id,))
        return cursor.fetchone()

    def __del__(self):
        self.conn.close()


