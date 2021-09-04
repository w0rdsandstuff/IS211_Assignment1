
def listDivide(numbers, divide = 2):
    """
    The function returns the number of elements in the numbers list that are divisibleby divide
    """
    counter = 0
    for num in numbers:
        if num % divide == 0:
            counter += 1
            
    return counter       

# Professor, Im confused about the following, can you please explain?

class listDivideException(Exception):
    def __init__(self):

def testListDivide():
    """
    Test listDivide
    """
    # Not sure what to put here
    assert listDivide([1,2,3,4,5]) == 2
    assert listDivide([2,4,6,8,10]) == 5
    assert listDivide([30, 54, 63,98, 100], divide=10) == 2
    assert listDivide([]) == 0
    assert listDivide([1,2,3,4,5], 1) == 5
    
if __name__ == "__main__":
    testListDivide()
