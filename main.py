import types

class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.cursor = -1
        self.cursor_list = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.cursor += 1
        if self.cursor_list < len(self.list_of_list):
            if isinstance(self.list_of_list[self.cursor_list], list):
                if self.cursor >= len(self.list_of_list[self.cursor_list]):
                    self.cursor_list += 1
                    self.cursor = 0
                if self.cursor_list < len(self.list_of_list):
                    return self.list_of_list[self.cursor_list][self.cursor]
            else:
                if self.cursor >= len(self.list_of_list):
                    raise StopIteration
                return self.list_of_list[self.cursor_list]
        raise StopIteration
    

def flat_generator(list_of_lists):
    for sublist in list_of_lists:
        for item in sublist:
            yield item


def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)
        

def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
    test_2()