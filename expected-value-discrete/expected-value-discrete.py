import numpy as np

def expected_value_discrete(x, p):
    x=np.array(x)
    p=np.array(p)

    if x.shape != p.shape:
        raise ValueError("shape does not match.")
        
    if not np.allclose(np.sum(p),1):
        raise ValueError("probability must be sum to 1.")
    
    result=np.sum(x*p)
    return result