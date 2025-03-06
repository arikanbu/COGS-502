# Edit this file for your solutions.
# Bugra Kadir Arikan - 2740470

# Here is a sample solution for the cardinality of a set
size = lambda x: len(x.keys())

# `set_from_list` -- takes a list and returns a set.
set_from_list = lambda x:{element:None for element in x}

# `list_from_set` -- do the reverse of above. 
list_from_set = lambda x:[element for element in x.keys()]

# `add` -- takes a set and an element and returns a new set with the element added.
add = lambda x_set,x_elm: x_set | {x_elm:None}

# `remove` -- takes a set and an element and returns a new set with the element removed.
remove = lambda x_set,x_elm: {element:None for element in x_set.keys() if element != x_elm}

# `union`
union = lambda x_set,y_set: x_set | y_set

# `intersection`
intersection = lambda x_set,y_set: {element:None for element in x_set.keys() if element in y_set.keys()}

# `difference`
difference = lambda x_set,y_set: {element:None for element in x_set.keys() if element not in y_set.keys()}

# `symmetric_difference` -- the elements that are in exactly one of the sets.
symmetric_difference = lambda x_set,y_set: union(difference(x_set,y_set),difference(y_set,x_set))

# `is_subset_of`
is_subset_of = lambda x_set,y_set: sum([element in y_set.keys() for element in x_set.keys()]) == len(x_set)

# `is_superset_of`
is_superset_of = lambda y_set,x_set: sum([element in y_set.keys() for element in x_set.keys()]) == len(x_set)


def test():
    """Use this function to test your solutions"""

    def test_function(func, *args, expected):
        try:
            result = func(*args)
            return "[OK]" if result == expected else "[Not OK]"
        except Exception as e:
            return "[Error]"

    test_cases = {
        "set_from_list": ([[1, 2, 3]], {1: None, 2: None, 3: None}),
        "list_from_set": ([{1: None, 2: None, 3: None}], [1, 2, 3]),
        "add": ([{1: None, 2: None}, 3], {1: None, 2: None, 3: None}),
        "remove": ([{1: None, 2: None, 3: None}, 2], {1: None, 3: None}),
        "union": ([{1: None, 2: None}, {2: None, 3: None}], {1: None, 2: None, 3: None}),
        "intersection": ([{1: None, 2: None}, {2: None, 3: None}], {2: None}),
        "difference": ([{1: None, 2: None}, {2: None, 3: None}], {1: None}),
        "symmetric_difference": ([{1: None, 2: None}, {2: None, 3: None}], {1: None, 3: None}),
        "is_subset_of": ([{1: None, 2: None}, {1: None, 2: None, 3: None}], True),
        "is_superset_of": ([{1: None, 2: None, 3: None}, {1: None, 2: None}], True),
    }
    
    print("Function Name            | Status")
    print("-------------------------|--------")
    for name, (args, expected) in test_cases.items():
        status = test_function(eval(name), *args, expected=expected) if name in globals() else "[Not Implemented]"
        print(f"{name:<25} | {status}")