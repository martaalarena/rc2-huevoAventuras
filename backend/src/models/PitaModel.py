from database.db import get_connection
from .entities.Pita import Pita

class PitaModel():
    @classmethod
    def get_pitas(self):
        try:
            connection=get_connection()
            pitas=[]

            with connection.cursor() as cursor:
                    cursor.execute("SELECT id, name, description, status, picture_url FROM pitas")
                    resultset=cursor.fetchall()

                    for row in resultset:
                        pita=Pita(row [0], row[1], row[2], row[3], row[4])
                        pitas.append(pita.to_JSON())

            connection.close()
            return pitas
        except Exception as ex:
            raise Exception(ex)