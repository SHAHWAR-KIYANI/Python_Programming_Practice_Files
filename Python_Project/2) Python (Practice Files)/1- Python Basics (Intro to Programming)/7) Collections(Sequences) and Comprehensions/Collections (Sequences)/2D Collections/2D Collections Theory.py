# For 2D Collections (Sequences), all of these 2D Collections (Sequences) combinations are there and many more.

                                                                                                     # Possible Combinations
# list[lists], list[tuples], list[sets], list[dicts], list[arrays], list[frozenset()]
# tuple(lists), tuple(tuples), tuple(sets), tuple(dicts), tuple(arrays), tuple(frozenset())
# set{lists}, set{tuples}, set{sets}, set{dicts}, set{arrays}, set{frozenset()}
# dict{dicts}, dict{lists}, dict{tuples}, dict{sets}, dict{arrays}, dict{frozenset()}
# Numpy Arrays: array[arrays], array[lists], array[tuples], array[dicts], array[sets], array[frozenSets()]
# frozenset(sets), frozenset(tuples), frozenset(lists), frozenset(dicts),frozenset(frozenSets()), frozenset(arrays)

                                                                                                           # Valid Combinations
# list[lists], list[tuples], list[sets] => (Already Tried all These Combinations)
# tuple(tuples), tuple(lists), tuple(sets)) => (Already Tried all These Combinations)
# dict{dicts}, dict{lists}, dict{tuples}
# set{sets} => unpredictable iteration order, sets are unordered
# set{lists} => lists are mutable, sets require hashable elements
# set{tuples} => tuples are hashable, but sets are unordered
# frozenset(set)
# array[arrays] => Numerical Python (Numpy)

                                                                                           # Valid but Less Useful Combinations
# Set of Sets: set[set] (unpredictable iteration order, sets are unordered)
# Set of Lists: set[list] (lists are mutable, sets require hashable elements)
# Set of Tuples: set[tuple] (tuples are hashable, but sets are unordered)
# Frozen Set of Sets: frozenset[set] (similar issues as Set of Sets)