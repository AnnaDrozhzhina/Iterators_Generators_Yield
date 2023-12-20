#4.* Необязательное задание. Написать генератор, аналогичный генератору из задания 2,
# но обрабатывающий списки с любым уровнем вложенности. Шаблон и тест в коде ниже:

import types

list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

def flat_generator(list_of_list):
    for i in list_of_list:
        if isinstance(i, list):
            yield from flat_generator(i)
        else:
            yield i


def test_4():

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)

res = []
if __name__ == '__main__':
    test_4()
    for item in flat_generator(list_of_lists_2):
        res.append(item)
    print(res)
    
