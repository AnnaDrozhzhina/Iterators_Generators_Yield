#Доработать функцию flat_generator. Должен получиться генератор, который принимает
# список списков и возвращает их плоское представление. Функция test в коде ниже
# также должна отработать без ошибок.

import types

list_of_lists_1 = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None]
]

def flat_generator(list_):
	for el in list_:
		for i in el:
			yield i

def test_2():
    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


res = []
if __name__ == '__main__':
	test_2()
	for item in flat_generator(list_of_lists_1):
		res.append(item)
	print(res)

