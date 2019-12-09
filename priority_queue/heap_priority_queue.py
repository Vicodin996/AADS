# Copyright 2013, Michael H. Goldwasser
#
# Developed for use with the book:
#
#    Data Structures and Algorithms in Python
#    Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
#    John Wiley & Sons, 2013
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
from priority_queue.priority_queue_base import PriorityQueueBase


class Empty(Exception):
  pass


class HeapPriorityQueue(PriorityQueueBase): # base class defines _Item
  """A min-oriented priority queue implemented with a binary heap."""

  #------------------------------ nonpublic behaviors ------------------------------
  def _parent(self, j):
    return (j-1) // 2

  def _left(self, j):
    return 2*j + 1

  def _right(self, j):
    return 2*j + 2

  def _has_left(self, j):
    return self._left(j) < len(self._data)     # index beyond end of list?

  def _has_right(self, j):
    return self._right(j) < len(self._data)    # index beyond end of list?

  def _swap(self, i, j):
    """Swap the elements at indices i and j of array."""
    self._data[i], self._data[j] = self._data[j], self._data[i]

  def _upheap(self, j):
    parent = self._parent(j)
    if j > 0 and self._data[j] < self._data[parent]:
      self._swap(j, parent)
      self._upheap(parent)             # recur at position of parent

  def _downheap(self, j):
    if self._has_left(j):
      left = self._left(j)
      small_child = left               # although right may be smaller
      if self._has_right(j):
        right = self._right(j)
        if self._data[right] < self._data[left]:
          small_child = right
      if self._data[small_child] < self._data[j]:
        self._swap(j, small_child)
        self._downheap(small_child)    # recur at position of small child

  #------------------------------ public behaviors ------------------------------
  def __init__(self):
    """Create a new empty Priority Queue."""
    self._data = []

  def __len__(self):
    """Return the number of items in the priority queue."""
    return len(self._data)

  def add(self, key, value):
    """Add a key-value pair to the priority queue."""
    self._data.append(self._Item(key, value))
    self._upheap(len(self._data) - 1)            # upheap newly added position

  def min(self):
    """Return but do not remove (k,v) tuple with minimum key.

    Raise Empty exception if empty.
    """
    if self.is_empty():
      raise Empty('Priority queue is empty.')
    item = self._data[0]
    return (item._key, item._value)

  def remove_min(self):
    """Remove and return (k,v) tuple with minimum key.

    Raise Empty exception if empty.
    """
    if self.is_empty():
      raise Empty('Priority queue is empty.')
    self._swap(0, len(self._data) - 1)           # put minimum item at the end
    item = self._data.pop()                      # and remove it from the list;
    self._downheap(0)                            # then fix new root
    return (item._key, item._value)

  def _increment_priority(self):
    '''Increment by one the priority of all the element in the queue.'''
    for i in range(len(self._data)):
      if self._data[i]._key != -20:
        self._data[i]._key -= 1

  '''def es11(self, lists):
    max = lists[0][0]
    min = lists[0][lists[0].size()-1]
    for i in range(1..lists.size()):
      if (min > lists[i][lists[0].size()-1]):
        min = lists[i][lists[0].size()-1]
      if (max < lists[i][0]):
        max = lists[i][0]
    if max < min:
      max = min
    return range(min, max)
  #O(M)

  def bubbleSort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):

      # Last i elements are already in place
      for j in range(0, n - i - 1):

        # traverse the array from 0 to n-i-1
        # Swap if the element found is greater
        # than the next element
        if arr[j] > arr[j + 1]:
          arr[j], arr[j + 1] = arr[j + 1], arr[j]

  def es13(self, arr, k):
    d = {arr[0], 1}
    for i in range(1..arr.size()):
      c = False
      for j in range(len(d)):
        if arr[i] == d[j]._key:
          d[j]._value += 1
          c = True
      if not c:
        d2 = {arr[i], 1}
        d.add(d2)
    d = sorted(d)
    return [v for v in d.value()[:k]]
'''