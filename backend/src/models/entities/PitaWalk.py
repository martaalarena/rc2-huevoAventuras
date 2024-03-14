class PitaWalk():

    def __init__(self, id, pick_up_time=None, return_time=None, id_pita=None) -> None:
        self.id = id
        self.pick_up_time = pick_up_time
        self.return_time = return_time
        self.id_pita = id_pita

    def to_JSON(self):
        return {
            'id': self.id,
            'pick_up_time': self.pick_up_time,
            'return_time': self.return_time,
            'id_pita': self.id_pita,
    }