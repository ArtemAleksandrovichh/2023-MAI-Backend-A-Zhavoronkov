from typing import Any


class LRUCache:

    # capacity - максимальное кол-во элементов, которые могут быть сохранены в кэше
    # cache - словарь, который хранит пары ключ - значения (кортеж из самого значения и
    # порядкового номера последнего обращения к элементу)
    # counter - порядковый номер обращения к кэшу
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.cache = {}
        self.counter = 0

    def get(self, key: str) -> str | None:
        if key in self.cache:
            self.cache[key][1] = self.counter
            self.counter += 1
            return self.cache[key][0]
        else:
            return None

    def set(self, key: str, value: str) -> None:
        if len(self.cache) >= self.capacity:
            # Ищем объект, к которому дольше всего не обращались
            oldest = min(self.cache, key=lambda k: self.cache[k][1])
            del self.cache[oldest]
        self.cache[key] = [value, self.counter]
        self.counter += 1

    def rem(self, key: str) -> None:
        if key in self.cache:
            del self.cache[key]