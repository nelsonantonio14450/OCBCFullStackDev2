import movies
import directors


class TestSum():

    def test_movie(self):
        assert movies.read_all() is not None, "Should be there if there is data"

    def test_directors():
        assert directors.read_all() is not None, "Should be there if there is data"


if __name__ == "__main__":
    TestSum.test_movie()
    TestSum.test_directors()
    print("Everything passed")
