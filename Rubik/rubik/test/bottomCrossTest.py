import unittest
from rubik.controller.bottomCross import *
from rubik.model.cube import Cube
from rubik.controller.bottomCross import _UTMCheckPerimeter
from rubik.controller.bottomCross import _UTMCheckSides


class BottomCrossTest(unittest.TestCase):

    def test100_bottomCross_UTMCheckPerimeterShouldReturnB(self):
        encodedCube = 'wowrbyyrogggbrwyrgybbbgoywooobyowwwbwrrgyyrbrrybowgggo'
        theCube = Cube(encodedCube)
        result = _UTMCheckPerimeter(theCube)
        self.assertEqual(result, 'B')
        
    def test110_bottomCross_UTMCheckPerimeterShouldReturnb(self):
        encodedCube = 'wowrbyyroggwbryyroowyogbbbygobwowgwbogggyyrbrrybowgrrw'
        theCube = Cube(encodedCube)
        result = _UTMCheckPerimeter(theCube)
        self.assertEqual(result, 'b')
        
    def test120_bottomCross_UTMCheckPerimeterShouldReturnBB(self):
        encodedCube = 'wowrbyyroggwbrryrrboobgwybygobgowowbwyogyyrbrrybowggwg'
        theCube = Cube(encodedCube)
        result = _UTMCheckPerimeter(theCube)
        self.assertEqual(result, 'BB')
        
    def test130_bottomCross_UTMCheckSidesShouldReturnBuLU(self):
        encodedCube = 'rowobyrroggwbryyroowroggbbobwboowgwgwggryyybryybbwgyrw'
        theCube = Cube(encodedCube)
        result = _UTMCheckSides(theCube)
        self.assertEqual(result, 'BuLU')
        
    def test140_bottomCross_UTMCheckSidesShouldReturnRRB(self):
        encodedCube = 'woyrbbyrygrywrbgggobbygowyooobyowwwbwrbgygrboryrowwggr'
        theCube = Cube(encodedCube)
        result = _UTMCheckSides(theCube)
        self.assertEqual(result, 'RRB')
        
    def test150_bottomCross_UTMCheckSidesShouldReturnFuuFUU(self):
        encodedCube = 'oorgbgrbyygobrbbrywrrogygrwwogooygrbgybwywywbwwogwyobr'
        theCube = Cube(encodedCube)
        result = _UTMCheckSides(theCube)
        self.assertEqual(result, 'FuuFUU')
        
    def test160_bottomCross_solveBottomCrossShouldReturnCompleteSequence(self):
        encodedCube = 'oywygryorgbbgoyybrygbobbwwgobgyrrorbwoorywygrrwgwwowgb'
        theCube = Cube(encodedCube)
        result = solveBottomCross(theCube)
        self.assertEqual(result, 'buLULFFLLUUFFUBBRR')
        