class a:
    def __init__(self):
        self.a = 'a'

    def update(self, variable):
        self.a = variable

    def imprime(self):
        print(self.a)


class b(a):
    def __init__(self):
        self.b = 'b'
        super().__init__()

    def imprime(self):
        self.b = self.a
        print(self.b)


a = a()
b = b()
a.update('xesque')
b.imprime()
a.imprime()
