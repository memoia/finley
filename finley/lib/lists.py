def as_str(chars):
    return ''.join(map(str, chars))


def none_or(chars, fn):
    return None if chars is None else fn(chars)


def first(chars):
    fst = lambda c: as_str(c)[:1] or None
    return none_or(chars, fst)


def rest(chars):
    rst = lambda c: as_str(c)[1:] or None
    return none_or(chars, rst)


def second(chars):
    return first(rest(chars))
