from KP_PI.cache import LRUCache

if __name__ == '__main__':
    cache = LRUCache(100)
    cache.set('Jesse', 'Pinkman')
    cache.set('Walter', 'White')
    cache.set('Jesse', 'James')
    cache.get('Jesse')
    cache.rem('Walter')
    cache.get('Walter')
