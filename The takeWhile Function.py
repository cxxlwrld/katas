def take_while(arr, pred_fun):
    # TODO: Do your best !
    result = []
    for item in arr:
        if pred_fun(item):
            result.append(item)
        else:
            break
    return result
