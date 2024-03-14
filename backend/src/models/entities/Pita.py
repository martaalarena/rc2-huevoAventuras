class Pita():

    def __init__(self, id, name=None, category=None, description=None, status=None, picture_url=None) -> None:
        self.id = id
        self.name = name
        self.category = category
        self.description = description
        self.status = status
        self.pictur_url = picture_url