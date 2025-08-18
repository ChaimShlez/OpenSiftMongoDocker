from services.data_loader.dataLoader import ConnectionWrapper


class Queries:

    def __init__(self):
        self._connection=ConnectionWrapper()


    def getAll(self):
        res = self._connection.get_all("users")
        return res


