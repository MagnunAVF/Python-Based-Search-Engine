class Database:
    """
        Entity that is responsable for store the app data
    """
    def __init__(self):
        self.documents = []
        self.inverted_index = {}
