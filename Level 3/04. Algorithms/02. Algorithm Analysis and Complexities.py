'''
Algorithm analysis is built by two complexities, space and time.

Space complexity of an algorithm is the total space taken with respect to
    the input size including auxiliary space.  The space is total sum of all
    components.

    S(P) = S(I) + C

    E.g. Multiply1(a,b):
    
        S(P) = 3 + 0
        S(P) = 3
    

Time complexity of an algorithm is the total time taken with respect to the
    n number of steps taken at a constant time to compute the required
    operation.

    T(n) = n * C

    Performance Boundaries for Program Execution:

        - Best Case Scenario:    Minimum Required Time
            Asymptotic Notation:
                Omega Notation (lower bound)
                ω(n) least step taken
            
        - Average Case Scenario: Average Required Time
            Asymptotic Notation:
                Theta Notation (both lower and upper bound)
                θ(n)
            
        - Worst Case Scenario:   Maximum Required Time
            Asymptotic Notation:
                Big O Notation (upper bound)
                O(n) most steps taken

                f(x) = O(f(x)) = {}



'''


'''  Constant Time  '''

def OddOrEven(n):
    return "Even" if n % 2 else "Odd"



















