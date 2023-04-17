from pprint import pprint
from unittest import TestCase
import unittest
from YaDiskClient import YaDiskClient
from person_data import YA_TOKEN


ya = YaDiskClient(ya_token=YA_TOKEN)

class TestCreateFolder(TestCase):

    @unittest.expectedFailure
    def test_1check_folder_failure(self):
        disk_resources_path = 'netology_test_17-04-2023'
        result = ya.get_status_resources(disk_resources_path=disk_resources_path)
        excepted = 200

        self.assertEqual(result, excepted, msg=f'Не удалось найти запрошенный ресурс.')

    def test_2create_folder(self):
        result = ya.create_folder(disk_folder_path='netology_test_17-04-2023')
        excepted = 201

        self.assertEqual(result, excepted)

    def test_3check_folder(self):
        result = ya.get_status_resources(disk_resources_path='netology_test_17-04-2023')
        excepted = 200

        self.assertEqual(result, excepted)

    @unittest.expectedFailure
    def test_4create_folder_failure(self):
        disk_resources_path = 'netology_test_17-04-2023'
        result = ya.get_status_resources(disk_resources_path=disk_resources_path)
        excepted = 201

        self.assertEqual(result, excepted, msg=f'Ресурс "{disk_resources_path}" уже существует. Status code 409')


if __name__ == '__main__':
    unittest.main(argv=['ignored', '-v',])