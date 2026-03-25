import numpy as np

def percentiles(x, q):
    x=np.array(x)
    q=np.array(q)

    # sort the data
    x= np.sort(x)

    result=np.percentile(x,q,method="linear")

    return result