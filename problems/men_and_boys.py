"""
See https://www.codewars.com/kata/sort-out-the-men-from-boys-1/train/python

Now that the competition gets tough it will Sort out the men from the boys .
Men are the Even numbers and Boys are the odd

Given an array/list [] of n integers,
Separate The even numbers from the odds,
or Separate the men from the boys
"""


def men_from_boys(numbers_list):
  """
  >>> men_from_boys([7, 3, 14, 17])
  [14, 17, 7, 3]
  >>> men_from_boys([2, 43, 95, 90, 37])
  [2, 90, 95, 43, 37]
  >>> men_from_boys([20, 33, 50, 34, 43, 46])
  [20, 34, 46, 50, 43, 33]
  """
  return []



if __name__ == '__main__':
  import doctest
  doctest.testmod()
