from database.db import get_connection

from datetime import datetime

class PitaRentingModel():
    @classmethod
    def add_pitaRenting(cls, pitaRenting):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO pitarentings (pick_up_date, return_date, id_pita)
                                        VALUES (%s, %s, %s)""", (pitaRenting.pick_up_date, pitaRenting.return_date, pitaRenting.id_pita))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)