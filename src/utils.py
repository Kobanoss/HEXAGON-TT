class Build_in_log(object):
    def __init__(self) -> None:
        self.__data = []

    def add(self, msg: dict) -> None:
        self.__data.append(msg)

    def get(self) -> list[dict]:
        return self.__data

