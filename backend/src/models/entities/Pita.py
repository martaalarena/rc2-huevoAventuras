class Pita():

    def __init__(self, id, name=None, description=None, status=None, picture_url=None) -> None:
        self.id = id
        self.name = name
        self.description = description
        self.status = status
        self.picture_url = picture_url

    def to_JSON(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'status': self.status,
            'picture_url' : self.picture_url
    }