def bahola(t):
    res = []
    for x in t:
        if x >= 90:
            res.append("A")
        elif x >= 70:
            res.append("B")
        elif x >= 50:
            res.append("C")
        else:
            res.append("D")
    return res

def ism_tasnifi(names):
    res = []
    for n in names:
        if len(n) < 3:
            res.append("juda qisqa")
        elif len(n) <= 5:
            res.append("normal")
        else:
            res.append("uzun")
    return res
