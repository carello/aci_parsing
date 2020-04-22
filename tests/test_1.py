def is_greater(a, b):
    # returns True if 'a' is greater
    if a < b:
        return False
    return True

def publish_result(test):
    def result():
        value = test()
        print(value)
        if value[0] == value[1]:
            result = "PASS"
        else:
            result = "FAIL"
        print(f"{test.__name__}: {result}")
    return result


@publish_result
def test_true_when_greater():
    result = [is_greater(5, 4), True]
    return result


@publish_result
def test_false_when_smaller():
    result = [is_greater(4, 5), False]
    return result


@publish_result
def test_false_when_equal():
    result = [is_greater(5, 5), False]

    return result


if __name__ == "__main__":
    test_true_when_greater()
    test_false_when_smaller()
    test_false_when_equal()
