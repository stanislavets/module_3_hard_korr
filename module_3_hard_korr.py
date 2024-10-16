def calculate_structure_sum(data):
    numbers = 0
    strings = 0

    def recurse(element):
        nonlocal numbers, strings
        if isinstance(element, int):
            numbers += element
        elif isinstance(element, str):
            strings += len(element)
        elif isinstance(element, list):
            for item in element:
                recurse(item)
        elif isinstance(element, dict):
            for key, value in element.items():
                strings += len(key)
                recurse(value)
        elif isinstance(element, tuple):
            for item in element:
                recurse(item)
        elif isinstance(element, set):
            for item in element:
                recurse(item)

    recurse(data)

    return (numbers + strings)


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
