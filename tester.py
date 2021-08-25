class tester:
    """
    tester class verifies the input
    """
    def __init__(self):
        pass

    def test_string(self,address):
        """
        Function to test if the type is a string
        :param address: string
        :return: assert
        """
        t=type(address) == str
        assert t, "not a string"

    def test_alnum(self, address):
        """
        Function to verify if all characters are alphanumeric
        :param address: string
        :return: assert
        """
        t=address.replace(" ", "").isalnum()
        assert t, "it only accept digits and letters"

    def test_is_valid(self, address):
        """
        Set of functions to verify the input.
        :param address:
        :return:
        """
        self.test_string(address)
        self.test_alnum(address)