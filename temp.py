import sqlite3

class Database:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS module (
                date TEXT PRIMARY KEY,
                fabriant TEXT,
                dateFab TEXT,
                typeCompteur TEXT,
                diametreNominal TEXT,
                classe TEXT,
                Pression TEXT,
                debitPermanent TEXT,
                rpDebit1 TEXT,
                rpDebit2 TEXT,
                rp TEXT
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Erreur (
                id INTEGER PRIMARY KEY,
                date TEXT,
                nSerie TEXT,
                debitActuel TEXT,
                temperature TEXT,
                indexInitial TEXT,
                indexFinal TEXT,
                volumeIndique TEXT,
                volumeReel TEXT,
                erreur TEXT,
                emt TEXT,
                FOREIGN KEY(date) REFERENCES module(date)
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Essai (
                date TEXT PRIMARY KEY,
                methode TEXT,
                banc TEXT,
                TempAmbiante TEXT,
                HumiditeRelative TEXT,
                TempEau1 TEXT,
                TempEau2 TEXT,
                preEau1 TEXT,
                preEau2 TEXT,
                echelon TEXT,
                FOREIGN KEY(date) REFERENCES module(date)
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Quantité (
                id INTEGER PRIMARY KEY,
                date TEXT,
                m1 TEXT,
                m2 TEXT,
                m3 TEXT,
                v1 TEXT,
                v2 TEXT,
                v3 TEXT,
                FOREIGN KEY(date) REFERENCES Erreur(date)
            )
        ''')

        self.connection.commit()

    def __del__(self):
        self.connection.close()


class Module:
    def __init__(self, date, fabriant, dateFab, typeCompteur, diametreNominal, classe, Pression, debitPermanent, rpDebit1, rpDebit2, rp):
        self.date = date
        self.fabriant = fabriant
        self.dateFab = dateFab
        self.typeCompteur = typeCompteur
        self.diametreNominal = diametreNominal
        self.classe = classe
        self.Pression = Pression
        self.debitPermanent = debitPermanent
        self.rpDebit1 = rpDebit1
        self.rpDebit2 = rpDebit2
        self.rp = rp


class Erreur:
    def __init__(self, id, date, nSerie, debitActuel, temperature, indexInitial, indexFinal, volumeIndique, volumeReel, erreur, emt):
        self.id = id
        self.date = date
        self.nSerie = nSerie
        self.debitActuel = debitActuel
        self.temperature = temperature
        self.indexInitial = indexInitial
        self.indexFinal = indexFinal
        self.volumeIndique = volumeIndique
        self.volumeReel = volumeReel
        self.erreur = erreur
        self.emt = emt


class Essai:
    def __init__(self, date, methode, banc, TempAmbiante, HumiditeRelative, TempEau1, TempEau2, preEau1, preEau2, echelon):
        self.date = date
        self.methode = methode
        self.banc = banc
        self.TempAmbiante = TempAmbiante
        self.HumiditeRelative = HumiditeRelative
        self.TempEau1 = TempEau1
        self.TempEau2 = TempEau2
        self.preEau1 = preEau1
        self.preEau2 = preEau2
        self.echelon = echelon


class Quantité:
    def __init__(self, id, date, m1, m2, m3, v1, v2, v3):
        self.id = id
        self.date = date
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3


class ModuleView:
    def __init__(self, db_connection):
        self.connection = db_connection
        self.cursor = self.connection.cursor()

    def create_module(self, module):
        self.cursor.execute('''
            INSERT INTO module (date, fabriant, dateFab, typeCompteur, diametreNominal, classe, Pression, debitPermanent, rpDebit1, rpDebit2, rp)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (module.date, module.fabriant, module.dateFab, module.typeCompteur, module.diametreNominal, module.classe,
              module.Pression, module.debitPermanent, module.rpDebit1, module.rpDebit2, module.rp))
        self.connection.commit()

    def get_module_by_date(self, date):
        self.cursor.execute('SELECT * FROM module WHERE date = ?', (date,))
        return self.cursor.fetchone()

    def update_module(self, module):
        self.cursor.execute('''
            UPDATE module
            SET fabriant=?, dateFab=?, typeCompteur=?, diametreNominal=?, classe=?, Pression=?, debitPermanent=?, rpDebit1=?, rpDebit2=?, rp=?
            WHERE date=?
        ''', (module.fabriant, module.dateFab, module.typeCompteur, module.diametreNominal, module.classe,
              module.Pression, module.debitPermanent, module.rpDebit1, module.rpDebit2, module.rp, module.date))
        self.connection.commit()

    def delete_module(self, date):
        self.cursor.execute('DELETE FROM module WHERE date = ?', (date,))
        self.connection.commit()


class ErreurView:
    def __init__(self, db_connection):
        self.connection = db_connection
        self.cursor = self.connection.cursor()

    def create_erreur(self, erreur):
        self.cursor.execute('''
            INSERT INTO Erreur (date, nSerie, debitActuel, temperature, indexInitial, indexFinal, volumeIndique, volumeReel, erreur, emt)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (erreur.date, erreur.nSerie, erreur.debitActuel, erreur.temperature, erreur.indexInitial,
              erreur.indexFinal, erreur.volumeIndique, erreur.volumeReel, erreur.erreur, erreur.emt))
        self.connection.commit()

    def get_erreur_by_id(self, id):
        self.cursor.execute('SELECT * FROM Erreur WHERE id = ?', (id,))
        return self.cursor.fetchone()

    def update_erreur(self, erreur):
        self.cursor.execute('''
            UPDATE Erreur
            SET date=?, nSerie=?, debitActuel=?, temperature=?, indexInitial=?, indexFinal=?, volumeIndique=?, volumeReel=?, erreur=?, emt=?
            WHERE id=?
        ''', (erreur.date, erreur.nSerie, erreur.debitActuel, erreur.temperature, erreur.indexInitial,
              erreur.indexFinal, erreur.volumeIndique, erreur.volumeReel, erreur.erreur, erreur.emt, erreur.id))
        self.connection.commit()

    def delete_erreur(self, id):
        self.cursor.execute('DELETE FROM Erreur WHERE id = ?', (id,))
        self.connection.commit()


class EssaiView:
    def __init__(self, db_connection):
        self.connection = db_connection
        self.cursor = self.connection.cursor()

    def create_essai(self, essai):
        self.cursor.execute('''
            INSERT INTO Essai (date, methode, banc, TempAmbiante, HumiditeRelative, TempEau1, TempEau2, preEau1, preEau2, echelon)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (essai.date, essai.methode, essai.banc, essai.TempAmbiante, essai.HumiditeRelative,
              essai.TempEau1, essai.TempEau2, essai.preEau1, essai.preEau2, essai.echelon))
        self.connection.commit()

    def get_essai_by_date(self, date):
        self.cursor.execute('SELECT * FROM Essai WHERE date = ?', (date,))
        return self.cursor.fetchone()

    def update_essai(self, essai):
        self.cursor.execute('''
            UPDATE Essai
            SET methode=?, banc=?, TempAmbiante=?, HumiditeRelative=?, TempEau1=?, TempEau2=?, preEau1=?, preEau2=?, echelon=?
            WHERE date=?
        ''', (essai.methode, essai.banc, essai.TempAmbiante, essai.HumiditeRelative,
              essai.TempEau1, essai.TempEau2, essai.preEau1, essai.preEau2, essai.echelon, essai.date))
        self.connection.commit()

    def delete_essai(self, date):
        self.cursor.execute('DELETE FROM Essai WHERE date = ?', (date,))
        self.connection.commit()


class QuantitéView:
    def __init__(self, db_connection):
        self.connection = db_connection
        self.cursor = self.connection.cursor()

    def create_quantite(self, quantite):
        self.cursor.execute('''
            INSERT INTO Quantité (date, m1, m2, m3, v1, v2, v3)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (quantite.date, quantite.m1, quantite.m2, quantite.m3, quantite.v1, quantite.v2, quantite.v3))
        self.connection.commit()

    def get_quantite_by_id(self, id):
        self.cursor.execute('SELECT * FROM Quantité WHERE id = ?', (id,))
        return self.cursor.fetchone()

    def update_quantite(self, quantite):
        self.cursor.execute('''
            UPDATE Quantité
            SET date=?, m1=?, m2=?, m3=?, v1=?, v2=?, v3=?
            WHERE id=?
        ''', (quantite.date, quantite.m1, quantite.m2, quantite.m3, quantite.v1, quantite.v2, quantite.v3, quantite.id))
        self.connection.commit()

    def delete_quantite(self, id):
        self.cursor.execute('DELETE FROM Quantité WHERE id = ?', (id,))
        self.connection.commit()


# Usage example
if __name__ == "__main__":
    db = Database('my_database.db')

    # Example usage of ModuleView
    module_view = ModuleView(db.connection)

    # Create a new module entry
    new_module = Module('2024-07-02', 'Company A', '2024-06-30', 'Type A', 'DN50', 'Class B', '1 bar', '10 m3/h', '5 m3/h', '8 m3/h', '7 m3/h')
    module_view.create_module(new_module)

    # Get a module by date
    fetched_module = module_view.get_module_by_date('2024-07-02')
    print("Fetched Module:", fetched_module)

    # Update a module
    fetched_module.fabriant = 'Company B'
    module_view.update_module(fetched_module)

    # Delete a module
    module_view.delete_module('2024-07-02')

    # Example usage of ErreurView
    erreur_view = ErreurView(db.connection)

    # Similarly, you can perform CRUD operations for Erreur, Essai, and Quantité tables using their respective view classes.
