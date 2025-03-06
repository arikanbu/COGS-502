#
# Assingment on mathematical functions
#
from myset import *
import random

fdomain = lambda func: func[0]
fcodomain = lambda func: func[1]
fmapping = lambda func: func[2]
frange = lambda func: set_from_list(fmapping(func).values())

fimageof = lambda func, element: set_from_list([item[0] for item in fmapping(func).items() if item[1] == element])
fimageto = lambda func, element: [item[1] for item in fmapping(func).items() if item[0] == element][0]

# Implement the following functions:

# make_func
# Input: domain (set), codomain (set)
# Output: triple (<set,set,dict>) 
make_func = lambda domain, codomain: (domain, codomain, {d: random.choice(list(codomain.keys())) for d in domain.keys()})

# is_function
# Input: triple (<set,set,dict>) 
# Output: boolean
is_function = lambda func: (
                            (set_from_list(fmapping(func).keys()) == fdomain(func)) and
                            (is_subset_of(set_from_list(fmapping(func).values()),fcodomain(func)))
                            )

# is_injective
# A function is injective (an injection or one-to-one) if every element of the codomain is the image of at most one element from the domain.
# Input: triple (<set,set,dict>) 
# Output: boolean
is_injective = lambda func: all([(size(intersection(fimageof(func, e_co),fdomain(func))) <= 1) for e_co in fcodomain(func)])

# is_surjective
# A function is surjective (a surjection or onto) if every element of the codomain is the image of at least one element from the domain.
# Input: triple (<set,set,dict>) 
# Output: boolean
is_surjective = lambda func: all([(size(intersection(fimageof(func, e_co),fdomain(func))) >= 1) for e_co in fcodomain(func)])

# is_bijective
# A bijection is a function that is both an injection and surjection. In other words, if every element of the codomain is the image of exactly one element from the domain.
# Input: triple (<set,set,dict>) 
# Output: boolean
is_bijective = lambda func: is_injective(func) and is_surjective(func)

# compose
# f(g(.))
# Input: f (triple), g (triple)
# Output: triple that represents the composition of f and g or None if not defined.
compose = lambda f,g : z if is_function(z:=(fdomain(g),fcodomain(g), {element:fimageto(f,fimageto(g,element)) for element in fdomain(g)})) else None

# inverse
# Input: triple (<set,set,dict>) 
# Output: triple or None if the inverse is not defined. 
inverse = lambda f: (frange(f),fdomain(f), {v:k for k,v in fmapping(f).items()}) if is_injective(f) else None
# Testing

def test():

    domain = {1: None, 2: None, 3: None, 4: None}
    codomain = {'a': None, 'b': None, 'c': None, 'd': None}

    results = {}
    test_cases =\
            {'is_function': [
                ([(domain, codomain, {1: 'c', 2: 'c', 3: 'b', 4: 'a'})],True),
                ([(domain, codomain, {1: 'c', 2: 'c', 3: 'b', 4: 'e'})],False),
                ([(domain, codomain, {2: 'c', 3: 'b', 4: 'c'})],False)],
             'is_injective': [
                 ([(domain, codomain |{'e':None,'f':None}, {1: 'c', 2: 'd', 3: 'a', 4:'b'})],True),
                 ([(domain, codomain, {1: 'c', 2: 'a', 3: 'c'})],False)],
             'is_surjective': [
                 ([(domain, codomain, {1: 'd', 2: 'b', 3: 'c', 4: 'a'})],True),
                 ([(domain, codomain, {1: 'b', 2: 'c', 3: 'c', 4: 'd'})],False)],
             'is_bijective': [
                 ([(domain, codomain, {1: 'b', 2: 'd', 3: 'a', 4: 'c'})],True),
                 ([(domain, codomain, {1: 'c', 2: 'a', 3: 'a', 4: 'c'})],False),
                 ([(domain, codomain|{'e':None}, {1: 'a', 2: 'b', 3: 'c', 4: 'd'})],False)
             ],
             'compose': [
                    ([(domain,codomain,{1: 'c', 2: 'd', 3: 'c', 4: 'd'}), (remove(codomain,'c'),domain,{'a': 1, 'b': 1, 'c': 2, 'd': 3} )], None)
             ],
             'inverse': [
                 ([(domain,codomain, {1: 'd', 2: 'b', 3: 'c', 4: 'a'})], ({'d': None, 'b': None, 'c': None, 'a': None}, {1: None, 2: None, 3: None, 4: None}, {'d': 1, 'b': 2, 'c': 3, 'a': 4})),
                 ([(domain,codomain, {1: 'c', 2: 'd', 3: 'd', 4: 'b'})], None)
                    ]
            } 


    for funcname, cases  in test_cases.items():
        try:
            results[funcname] =  "OK" if all([eval(funcname)(*case[0]) == case[1] for case in cases]) else "Not OK"
        except NameError:
            results[funcname] = "Not Implemented"
        except Exception as e:
            results[funcname] = "Error -- " + str(e)

    print("Function Name            | Status")
    print("-------------------------|--------")
    for key, value in results.items():
        print(f"{key:<24} | {value}")

test()
