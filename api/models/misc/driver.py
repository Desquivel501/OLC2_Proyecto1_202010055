class Driver:

    def __init__(self):
        self.console = ""
        self.errores = []

    def append(self, text):
        self.console += text
        
    def error(self, text):
        self.errores.append(text);