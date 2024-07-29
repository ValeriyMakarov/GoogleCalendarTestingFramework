class Singleton:
    __instance = None
    __initialized = False

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(Singleton, cls).__new__(cls)
        return cls.__instance

    @property
    def initialized(self) -> bool:
        if not self.__initialized:
            self.__initialized = True
            return False
        return True
