class FileObserver:
    __instance = None

    def __init__(self, subscribers=None):
        if FileObserver.__instance is not None:
            raise Exception("Direct initialization of singleton is not allowed. Use get_instance() instead.")
        else:
            FileObserver.__instance = self
            if subscribers is None:
                self.__subscribers = []
            else:
                self.__subscribers = subscribers

    @staticmethod
    def get_instance():
        if FileObserver.__instance is None:
            FileObserver()
        return FileObserver.__instance

    def add_subscriber(self, to_add):
        self.__subscribers.append(to_add)

    def notify(self, i):
        for subscriber in self.__subscribers:
            try:
                subscriber.controller.update_code(i)
            except AttributeError as e:
                print("Not implemented yet")