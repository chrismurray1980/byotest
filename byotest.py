def tests_are_equal(actual, expected):
    assert expected == actual, "Expected {0} got {1}".format(expected, actual)
 
def tests_not_equal(actual, expected):
    assert expected != actual, "Expected {0} got {1}".format(expected, actual)

def tests_is_in(collection, item):
    assert item in collection, "{0} does not contain {1}".format(collection, item)
    
def tests_not_in(collection, item):
    assert item not in collection, "{0} does contain {1}".format(collection, item)
    
def tests_between(upper, lower, value):
    assert value <= upper, "{0} is greater than {1}".format(value, upper)
    assert value >= lower, "{0} is less than {1}".format(value, lower)
