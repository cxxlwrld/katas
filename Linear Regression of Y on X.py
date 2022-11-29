def regressionLine(x, y):
    import numpy as np
    x_squares = np.square(x)
    xy_product = np.array(x) * np.array(y)
    x_sum = np.sum(np.array(x))
    y_sum = np.sum(np.array(y))
    x_squares_sum = np.sum(x_squares)
    xy_product_sum = np.sum(xy_product)
    n = len(x)
    b = (n * (xy_product_sum) - (x_sum * y_sum)) / ( n * (x_squares_sum) - np.square(x_sum))
    a = (y_sum - b * x_sum ) / n
    return  (np.around(a, 4), np.around(b, 4))