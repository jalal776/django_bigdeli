import numpy as np

def test_args(a,*args):
    print(args)
    

test_args(2)
test_args(1,2)
test_args(1,2,3,4)
test_args(*[1,2,3])