from database.db import get_connection
from .entities.PitaRenting import PitaRenting
@classmethod
def add_pita(self, pitaRenting):
        try:
            connection=get_connection()

            with connection.cursor() as cursor:
                    cursor.execute("""INSERT INTO pitas (id, pick_up_date, return_date, id_pita)
                                                VALUES (%s, %s, %s, %s, %s,)""", (pitaRenting.id, pitaRenting.pick_up_date, pitaRenting.return_date, pitaRenting.id_pita))
                    affected_rows=cursor.rowcount
                    connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)