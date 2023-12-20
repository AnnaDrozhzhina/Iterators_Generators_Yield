list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

#1. Доработать класс FlatIterator в коде ниже. Должен получиться итератор, который принимает список списков
# и возвращает их плоское представление, т. е. последовательность, состоящую из вложенных элементов. Функция test
# в коде ниже также должна отработать без ошибок.
class FlatIterator:

	def __init__(self, list_):
		self.list = list_
		self.counter = 0
		self.index = -1

	def __iter__(self):
		return self

	def __next__(self):
		self.index += 1
		if self.index >= len(self.list[self.counter]):
			self.counter += 1
			if self.counter >= len(self.list):
				raise StopIteration

			self.index = 0

		return self.list[self.counter][self.index]

def test_1():

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

res = []
if __name__ == '__main__':
	test_1()
	for item in FlatIterator(list_of_lists_1):
		res.append(item)
	print(res)









