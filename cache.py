from functools import cache

@cache
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(500))

# c'est la meme chose que ci-dessous :

# implémenter un cache- --> memoïsation
def fib_cache(n, cache = None):
    if cache is None:
        cache = {}

    if n <= 1:
        return n
    
    if n in cache:
        return cache[n]
    
    cache[n] = fib_cache(n - 1, cache) + fib_cache(n - 2, cache)

    return cache[n]

fib_cache(5)


#  implementer un décorateur  
# imbriquer une fonction dans une autre

def decorateur(func):
    
    def wrapper():
        print('hello')
        func()
        print('goodbye')

    return wrapper


@decorateur
def hay():
    print('how are you')

hay()


def mon_cache(func):
    memoire = {}

    def wrapper(n):
        if not in memoire:
            memoire[n] = func(n)
        return memoire[n]

    return wrapper

@mon_cache
def fib(n):
    # ....

