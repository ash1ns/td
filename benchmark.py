__license__ = 'Nathalie (c) EPITA'
__docformat__ = 'reStructuredText'
__revision__ = '$Id: prefixTrees.py 2018-02-14'

"""
Prefix Trees homework
2018
@author: login
"""


from algopy import tree
from test import *

def countwords(T):    
    """ count words in dictionnary T
    
    :param T: The prefix tree
    :rtype: int
    :Example:
    >>> countwords(Tree1)
    11
    """
    res = 0
    if T.key[1]:
        res += 1
    for child in T.children:
        appel = countwords(child)
        res += appel
    return res

def __longestwordlength(T, l):
    length = 0
    if T.key[1]:
        return l
    for child in T.children:
        length = max(length, __longestwordlength(child, l + 1))
    return length

def longestwordlength(T):
    """ longest word length
    
    :param T: The prefix tree
    :rtype: int
    :Example:
    >>> longestwordlength(Tree1)
    6
    """
    return __longestwordlength(T, 0)

def __averagelength(T, l):
    sumsize = 0
    if T.key[1]:
        sumsize += l
    for child in T.children:
        s = __averagelength(child, l + 1)
        sumsize += s
    return sumsize

def averagelength(T):
    """ average word length
    
    :param T: The prefix tree
    :rtype: float
    :Example:
    >>> averagelength(Tree1)
    4.636363636363637
    """
    sumsize = __averagelength(T, 0)
    return sumsize/countwords(T)

#####TESTS#####
print(countwords(Tree1))
print(longestwordlength(Tree1))
print(averagelength(Tree1))
