"""
Exploring the various ways of implementing a "reducer". Implementations are benchmarked in
test_common_reducers.py
"""

import functools

# Some example reducers where the base operation is already defined.

# The most straight forward imperative style. Short of already having the reducer written
# (see argument_list_max()), this is probably the most readable form. Although requires
# maintaining state.
def for_loop_max(iterable):
  acc = 0  # What to do when iterable is zero length?
  for element in iterable:
    acc = max(acc, element)
  return acc

def reducer_max(iterable):
    return functools.reduce(max, iterable)

# Probably the easiest to read, and the fastest. But this is limited to the cases where
# the reducer is already implemented.
def argument_list_max(iterable):
    return max(*iterable)


# Some example reducers where the base operation is passed in

def operation(a, b):
    return max(a, b)

def reducer_passed_in(iterable):
    return functools.reduce(operation, iterable)

def reducer_with_lambda(iterable):
    return functools.reduce(lambda x, y: max(x, y), iterable)


# Some examples where there is a data structure multiple fields and you want to find the
# data structure with max value in a specific field.

# Most explicit straightfoward imperative style. Assumes that values are in an indexable
# sequence not in an iterator.
def for_loop_on_key(sequence):
    max_value, max_index = sequence[0].key, 0
    for index in range(1, len(sequence)):
        if element.key > max_value:
            max_value = element.key
            max_index = index
    return sequence[max_index]
