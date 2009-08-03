import math
hex = "00111110010110010001011010000111"

def convert(text):
    sign = int(text[0]) and -1.0 or 1.0
    exp = int(text[1:9], 2)-127
    val = text[9:32]
    m = 0.5
    ret = 1.0
    for d in val:
        ret += float(d) * m
        m /= 2.0

    print ret * pow(2, exp)

    #print sign, int(exp, 2), int(val, 2)

convert(hex)


def test(one, **kwargs):
    print one, id(kwargs)
    kwargs['ala'] = 45

dict = {'one': 10, 'two': 15}
print dict, id(dict)
test(**dict)
print dict


