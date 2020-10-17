def setup_module():
    print("set up module")


def teardown_module():
    print("tear down module")


def test_case():
    print("test1")


def setup_function():
    print("startup: setup function")


def teardown_function():
    print("recover resource function")


class TestDemo:
    def setup_class(self):
        print("test demo setup_class")

    def teardown_class(self):
        print("test demo teardown class")

    def setup(self):
        print("test demo setup")

    def teardown(self):
        print("test demo teardown")

    def test_demo1(self):
        print("test demo1")

    def test_demo2(self):
        print("test demo2")
