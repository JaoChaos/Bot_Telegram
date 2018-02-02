import unittest


class Test(unittest.TestCase):

    def test_atiende(self):
        return True

    def test_comando(self):
        cid = message.chat.id
        if cid.content_type == "text":
            return True
        else:
            return False
