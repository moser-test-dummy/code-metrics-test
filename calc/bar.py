from .hurz import i_dont_exist

def main():
    result = i_dont_exist()
    return map(lambda x: x.id, result)