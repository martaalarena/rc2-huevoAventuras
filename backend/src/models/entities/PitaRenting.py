class PitaRenting():

    def __init__(self, id, pick_up_date=None, return_date=None, id_pita=None) -> None:
        self.id = id
        self.pick_up_date = pick_up_date
        self.return_date = return_date
        self.id_pita = id_pita

    def to_JSON(self):
        return {
            'id': self.id,
            'pick_up_date': self.pick_up_date,
            'return_date': self.return_date,
            'id_pita': self.id_pita,
    }