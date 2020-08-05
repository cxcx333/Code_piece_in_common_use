import unittest
from test_2 import DataTracker


def get_data():
    try:
        tracker = DataTracker()
        tracker.login()
        return tracker.get_current_data()
    except:
        return 0
    finally:
        print('Quit')
        tracker.quit()


class UTTestcase(unittest.TestCase):
    def test_get_data(self):
        r1 = get_data()
        r2 = get_data()
        r3 = get_data()
        r4 = get_data()
        r5 = get_data()
        self.assertNotEqual(r1, 0)
        self.assertNotEqual(r2, 0)
        self.assertNotEqual(r3, 0)
        self.assertNotEqual(r4, 0)
        self.assertNotEqual(r5, 0)


if __name__ == '__main__':
    unittest.main()
