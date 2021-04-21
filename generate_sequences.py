#%%
from random import choice
from string import ascii_uppercase

def random_string(length):
    """Produce a random string made of *length* uppercase ascii 
     characters"""
    amino_acids = set(ascii_uppercase).difference(set(['B','O','J','U','X','Z']))
    return ''.join(choice(list(amino_acids)) for i in range(length)) 
# %%

def test_random_string():
    s = random_string(200)
    str = set(s)
    assert len(str) == 4

# %%
from random import choices
def caching_fib(length):
    l = {i:0 for i in range(length)}

    return l
# %%
