import unittest
import requests


class PythonRepositoryTest(unittest.TestCase):
    def setUp(self):
        url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
        headers = {'Accept': 'application/vnd.github'}
        self.r = requests.get(url, headers=headers)
        self.response_dict = self.r.json()

    def test_status_code(self):
        self.assertEqual(self.r.status_code, 200)

    def test_num_repositories_returned(self):
        repo_dicts = self.response_dict['items']
        self.assertEqual(len(repo_dicts), 30)

    def test_total_repositories_threshold(self):
        self.assertEqual(self.response_dict['total_count'] > 6_472_699, True)


if __name__ == '__main__':
    unittest.main()
