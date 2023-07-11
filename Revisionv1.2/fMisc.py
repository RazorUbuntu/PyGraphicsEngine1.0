# REMAINING UNORGANISED FUNCTIONS

#### fUNCTIONS DEFINE ####

# Sums one list's elements with the other.
def sum_in_list(l1, l2) -> list:
    if len(l1) >= len(l2):
        for idx, item in enumerate(l2):
            l1[idx] += item
        return l1

    else:
        for idx, item in enumerate(l1):
            l2[idx] += item
        return l2


# Multiplies a sequence's elements with a constant.
def mul_seq_const2tup(seq, const) -> tuple:
    list_ = list(seq)
    for idx, element in enumerate(list_):
        list_[idx] = element * const
    return tuple(list_)
