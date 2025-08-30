from time import time, ctime

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
    
    @staticmethod
    def log(msg: str, log_type: str = "LOG"):
        # open file in context manager
        with open("logs.txt", "a") as f:
            # write to file on new line
            f.write(f"{ctime()}\t{log_type.upper()}: {msg}\n")

Tools.log("testing log2")