mport numpy as np

def regressionLine(x, y):
    """ Return the a (intercept)
        and b (slope) of Regression Line 
        (Y on X).
    """
    a,b = np.polyfit(x,y,1)
    return round(b,4),round(a,4)
