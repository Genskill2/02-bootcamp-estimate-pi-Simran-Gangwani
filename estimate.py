import math
import unittest
from functools import reduce
import random


def wallis(n):
    i = 1
    numerator = 1
    denomenator = 1
    for i in range(n+1):
        x = 4 * i * i
        numerator *= x
        denomenator *= (x-1)
    print(2 * (numerator/denomenator))
    return (2 * (numerator/denomenator))

def monte_carlo(n):
    circle = 0
    sq = 0
    
    for i in range(1, n+1):
        # So as to cover all the 4 quadrants of square range = (-1,1)
        x = random.uniform(-1,1)
        y = random.uniform(-1,1)
        
        #assuming center of the circle as origin
        dist = x*x + y*y
        
        #since the radius of circle = 1(given) all the points lying inside the sircle should have distance less than equals to one
        if(dist <= 1):
            circle += 1
        square += 1
        
        return(4* (circle/square))
    
class TestWallis(unittest.TestCase):
    def test_low_iters(self):
        for i in range(0, 5):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) > 0.15, msg=f"Estimate with just {i} iterations is {pi} which is too accurate.\n")
            
    def test_high_iters(self):
        for i in range(500, 600):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) < 0.01, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")
    
    


class TestMC(unittest.TestCase):
    def test_randomness(self):
        pi0 = monte_carlo(15000)
        pi1 = monte_carlo(15000)
        
        self.assertNotEqual(pi0, pi1, "Two different estimates for PI are exactly the same. This is almost impossible.")

        self.assertFalse(abs(pi0 - pi1) > 0.05, "Two different estimates of PI are too different. This should not happen")

    def test_accuracy(self):
        for i in range(500, 600):
            pi = monte_carlo(i)
            self.assertTrue(abs(pi - math.pi) < 0.4, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")
        
    
if __name__ == "__main__":
    unittest.main()
