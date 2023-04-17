from data import filter_russia, unique_ids, ad_max_stats
import pytest


class TestHomework4:
    def test_filter_russia(self):
        result = filter_russia()
        expected = [
            {'visit1': ['Москва', 'Россия']},
            {'visit3': ['Владимир', 'Россия']},
            {'visit7': ['Тула', 'Россия']},
            {'visit8': ['Тула', 'Россия']},
            {'visit9': ['Курск', 'Россия']},
            {'visit10': ['Архангельск', 'Россия']}
        ]

        assert result == expected

    def test_unique_ids(self):
        result = unique_ids()
        expected = {98, 35, 15, 213, 54, 119}

        assert result == expected

    def test_ad_max_stats(self):
        result = ad_max_stats()
        expected = 'yandex'

        assert result == expected