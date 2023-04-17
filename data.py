def filter_russia():

    geo_logs = [
            {'visit1': ['Москва', 'Россия']},
            {'visit2': ['Дели', 'Индия']},
            {'visit3': ['Владимир', 'Россия']},
            {'visit4': ['Лиссабон', 'Португалия']},
            {'visit5': ['Париж', 'Франция']},
            {'visit6': ['Лиссабон', 'Португалия']},
            {'visit7': ['Тула', 'Россия']},
            {'visit8': ['Тула', 'Россия']},
            {'visit9': ['Курск', 'Россия']},
            {'visit10': ['Архангельск', 'Россия']}
        ]

    res = []

    for item in geo_logs:
        for value in item.values():
            if 'Россия' in value:
                res.append(item)
    
    geo_logs.clear()

    geo_logs.extend(res)

    return res



def unique_ids():

    ids = {
        'user1': [213, 213, 213, 15, 213],
        'user2': [54, 54, 119, 119, 119],
        'user3': [213, 98, 98, 35]
    }

    res = set()

    for id in ids.values():
        res.update(id)

    return res


def percentage_queries():

    queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
    ]

    len_queries = len(queries)

    res = dict()

    for query in queries:
        l = len(query.split())

        if l not in res:
            res[l] = {'count': 1, 'percentage': round(1 / len_queries * 100, 2)}
        else:
            res[l]['count'] += 1
            res[l]['percentage'] = round(res[l]['count'] / len_queries * 100, 2)

    return res

def ad_max_stats():
    stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}

    res = ''
    for name, value in stats.items():
        if stats.get(res, 0) < stats[name]:
            res = name

    return res