from database.db import get_connection
from .entities.PitaWalk import PitaWalk

class PitaWalkModel():
    @classmethod
    def add_pitaWalk(self, pitaWalk):
        try:
            connection=get_connection()

            with connection.cursor() as cursor:
                    cursor.execute("""INSERT INTO pitaWalks (id, pick_up_time, pick_up_date, id_pita
                                                VALUES (%s, %s, %s, %s, %s,)""", (pitaWalk.id, pitaWalk.pick_up_time, pitaWalk.pick_up_date, pitaWalk.id_pita ))
                    affected_rows=cursor.rowcount
                    connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
