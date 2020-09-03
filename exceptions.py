class QueryNotFound(Exception):
    def __init__(self):
        self.message = "The requested query was not found"
        super().__init__(self.message) 
