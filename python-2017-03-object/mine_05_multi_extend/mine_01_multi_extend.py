class A:
    def __init__(self):
        self.name = "A name"

    def test(self):
        print("A test")

    def demo(self):
        print("A demo")


class B:
    def __init__(self):
        self.name = "B name"

    def test(self):
        print("B test")

    def demo(self):
        print("B demo")


class C(A, B):
    pass


c = C()
print(c.name)
c.demo()
c.test()
