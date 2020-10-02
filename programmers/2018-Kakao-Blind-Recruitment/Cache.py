#  Programmers - 2018 Kakao Blind Recruitment - Cache

def set_cache_len(cache_storage, cacheSize):
    if len(cache_storage) > cacheSize:
        del cache_storage[0]


def solution(cacheSize, cities):
    answer = 0
    cache_storage = []

    for city in cities:
        city = city.lower()
        if cache_storage is None or city not in cache_storage:
            cache_storage.append(city)
            set_cache_len(cache_storage, cacheSize)
            answer += 5
        else:
            cache_storage.remove(city)
            cache_storage.append(city)
            answer += 1

    return answer
