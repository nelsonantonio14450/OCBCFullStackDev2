import movies
import directors
import unittest


def test_movie():
    assert movies.read_all(
    ) is not None, "you should insert first, if there is data, then this is really an error"


def test_directors():
    assert directors.read_all(
    ) is not None, "you should insert first, if there is data, then this is really an error"


class TestSum(unittest.TestCase):

    def test_directors(self):
        self.assertIs(type(directors.read_all()), list)

    def test_movie(self):
        self.assertIs(type(movies.read_all()), list)


if __name__ == "__main__":
    # TestSum.test_movie()
    # TestSum.test_directors()
    unittest.main()

    print("Everything passed")
