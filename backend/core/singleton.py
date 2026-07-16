class MongoConnection:

    _instance = None

    @staticmethod
    def get_instance():

        if MongoConnection._instance is None:
            MongoConnection._instance = MongoConnection()

        return MongoConnection._instance