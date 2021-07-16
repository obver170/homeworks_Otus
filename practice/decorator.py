def trace(func):
    def inner(*args, **kwargs):
        res = func(*args, **kwargs)
        # print(func, ' res ', res)
        return res

    return inner


@trace
def fib(n):
    if n < 2:
        return n
    # print('n-1 + n-2 = ', n-1 + n-2)
    return fib(n - 1) + fib(n - 2)


def main():
    fib(10)
    print(fib(10))
    for i in range(11):
        print(i, ' - ', fib(i))
    first_list = [1, 2, 3, 4]
    print(f'first_list = {first_list}')
    second_list = first_list
    k = second_list.pop()
    print(f'first_list = {first_list}')
    first_dict = {'one': 'one', 'two': 'two', '3': '3'}
    print(f'first_dict = {first_dict}')
    second_dict = first_dict
    second_dict.update({'4': '4'})
    print(f'first_dict = {first_dict}')

if __name__ == '__main__':
    main()
