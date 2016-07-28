import travistest
import unittest

class TravisTestCase(unittest.TestCase):

    def setUp(self):
        travistest.app.config['TESTING'] = True
        self.app = travistest.app.test_client()
    
    def test_hello_world(self):
        rv = self.app.get('/')
        assert b'Hello world' in rv.data

if __name__ == '__main__':
    unittest.main()    
