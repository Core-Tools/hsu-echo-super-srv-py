from hsu_echo.py.domain.contract import Contract

class SuperHandler(Contract):
    def __init__(self):
        pass

    def Echo(self, message: str) -> str:
        return "py-super-echo: " + message
