#DAO (Data access object) pro práci s databází

import sqlite3

class ZaznamDAO:

    def __init__(self):
        self.db_file = 'nakupni_seznam.db'
        with sqlite3.connect('nakupni_seznam.db') as self.con:
            self.cur = self.con.cursor()
            self.cur.execute('''
                CREATE TABLE IF NOT EXISTS polozky 
                (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nazev VARCHAR(64) NOT NULL,
                mnozstvi VARCHAR(16) NOT NULL,
                splneno BOOL NOT NULL,
                datum_pridani DATE DEFAULT CURRENT_DATE
                )
            ''')

    def pridej_zaznam(self,zaznam_dto):
        nazev, mnozstvi = zaznam_dto
        try:
            self.cur.execute(f"""
            INSERT INTO polozky(nazev, mnozstvi, splneno)
            VALUES ({nazev}, {mnozstvi}, {False})
            """)
            self.con.commit()
        except sqlite3.Error as e:
            print(f"Chyba při vkládání záznamu {e}")

        

