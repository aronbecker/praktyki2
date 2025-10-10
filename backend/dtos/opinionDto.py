class OpinionDto:
    def __init__(self, id: int, rating: int, comment: str, creation_date: str, username: str):
        self.id = id
        self.rating = rating
        self.comment = comment
        self.creation_date = creation_date
        self.username = username