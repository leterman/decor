from datetime import datetime

def parametrized_decor(parameter):
    def decor(foo):
        def new_foo(*args, **kwars):
            result1 = foo(*args, **kwars)
            data_log = datetime.now()
            date = data_log.strftime("%A-%d-%B %Y %I:%M:%S %p")
            with open(path, 'a', encoding="utf-8") as f:
                f.write(f'Имя функции: {foo.__name__}\n{date}\nАргументы: {args}\nРезультат:{result1}\n')
                f.close()
        return new_foo
    return decor

path = r'C:\Users\Laterman\Documents\Python Projects\decorators\test.txt'
@parametrized_decor(parameter=path)
def function_to_be_used(x, y):
    z = x + y
    return z


res = function_to_be_used(23, 21)
