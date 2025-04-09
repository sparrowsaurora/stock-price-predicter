import time

class Tools:
    @staticmethod
    def timer(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print(f"{func.__name__!r} took: {end - start:.4f} seconds")
            return result
        return wrapper
