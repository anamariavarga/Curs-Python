def average(p):
    """
    Functia caculeaza media notelor
    Parameters:
        p (list) : lista notelor
    Returns:
        float : media notelor
    >>>average([2, 3, 4])
    3.0
    >>>average([])
    0.0
    >>>average([2, -7.9, -5])
    -3.63
    """
    if p:
        return (round(sum(p) / len(p), 2))
    return 0.0


if __name__ == "__main__":
    from doctest import testmod

    testmod()
