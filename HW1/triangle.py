import unittest

def classifyTriangle(a,b,c):
    if a-b > c or b-c > a or c-a > b:
        return 'NotATriangle'
    else:
        if a == b == c :
            return "Equilateral"
        elif a == b or b == c or a == c:
            return "Isoceles"
        else:
            if max(a,b,c)**2 == ((a+b+c)-max(a,b,c)-min(a,b,c))**2 + min(a,b,c)**2:
                return 'Right'
            else:
                return "Scalene"    

def printClassifyTriangle(a,b,c):
    print('classifyTriangle(',a, ',', b, ',', c, ')=' + classifyTriangle(a,b,c))

class TestTriangles(unittest.TestCase):
    def testNotATriangle(self):
        self.assertEqual(classifyTriangle(3,3,7), 'NotATriangle')
        self.assertNotEqual(classifyTriangle(3,3,3), "NotATriangle")

    def testEquilateral(self):  
        self.assertEqual(classifyTriangle(3,3,3), 'Equilateral')
        self.assertNotEqual(classifyTriangle(3,4,3), 'Equilateral')  

    def testIsoceles(self):
        self.assertEqual(classifyTriangle(3,5,5), 'Isoceles')
        self.assertNotEqual(classifyTriangle(3,4,5), 'Isoceles')

    def testScalene(self):
        self.assertEqual(classifyTriangle(3,4,6), 'Scalene')
        self.assertNotEqual(classifyTriangle(3,4,5), 'Scalene')
        
    def testRight(self):
        self.assertEqual(classifyTriangle(3,4,5), 'Right')
        self.assertNotEqual(classifyTriangle(6,10,6), 'Right')

if __name__ == '__main__':

    printClassifyTriangle(3,4,5)
    printClassifyTriangle(1,5,5)
    printClassifyTriangle(1,3,5)
    printClassifyTriangle(4,4,4)
    printClassifyTriangle(1,4,5)


    unittest.main(exit=True)
