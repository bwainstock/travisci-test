import travistest
import unittest

class TravisTestCase(unittest.TestCase):

    def setUp(self):
        travistest.app.config['TESTING'] = True
        self.app = travistest.app.test_client()
    
    def test_index(self):
        rv = self.app.get('/')
        assert b'Hello world' in rv.data

    def test_failing_test(self):
        rv = self.app.get('/butt')
        assert b'Hello world' not in rv.data

if __name__ == '__main__':
    unittest.main()    
