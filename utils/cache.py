from django.core.cache import cache


def set_cache(key, value):
    """
    Set a value in the cache
    """
    cache.set(key, value, timeout=60*10) # caches for 10 seconds

def get_cache(key):
    """
    get value  tfromhe cache
    """
    return cache.get(key)
