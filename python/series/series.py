def slices(series, length):
    if length <= 0 or length > len(series):
        raise ValueError(".+")
    return [series[i : i + length] for i in range(len(series) - length + 1)]
