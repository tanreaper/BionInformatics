#%%
from random import choice

def random_string(length):
    """Produce a random string made of *length* uppercase ascii 
     characters"""

    return ''.join(choice(['A','G','C','T']) for i in range(length)) 
# %%

def test_random_string():
    s = random_string(200)
    str = set(s)
    assert len(str) == 4