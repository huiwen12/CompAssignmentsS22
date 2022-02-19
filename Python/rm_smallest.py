import sys 

def rm_smallest(d):
    if d == {}:
        return d
    
    smallest_value = sys.maxsize
    smallest_key = sys.maxsize

    for key in d:
        if d[key] < smallest_value:
            smallest_value = d[key]
            smallest_key = key
    del d[smallest_key]

    return d

def test():
    assert 'a' in rm_smallest({'a':1,'b':-10}).keys()
    assert not 'b' in rm_smallest({'a':1,'b':-10}).keys()
    assert not 'a' in rm_smallest({'a':1,'b':5,'c':3}).keys()
    rm_smallest({})
    print("Success!")

if __name__ == "__main__":
    test()
