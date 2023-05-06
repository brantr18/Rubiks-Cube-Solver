from rubik.model.cube import Cube
from rubik.controller.bottomCross import solveBottomCross
from rubik.controller.bottomLayer import solveBottomLayer
from rubik.controller.middleLayer import solveMiddleLayer
from rubik.controller.upFaceCross import solveUpCross
from rubik.controller.upFaceCross import _isUpCrossSolved
from rubik.controller.upFaceCross import _isLOnUpFace
from rubik.controller.upFaceCross import _isHorizontalOnUpFace
from rubik.controller.upFaceCross import _isLInCorrectPosition
from rubik.controller.upFaceCross import _moveLOnUpFaceToCorrectPosition

'''
Created on Apr 4, 2023

@author: Brantley
'''
import unittest


class UpFaceCrossTest(unittest.TestCase):


    def test100_upFaceCross_isUpCrossSolvedShouldReturnFalse(self):
        encodedCube = 'ygrggggggyyroooooogrbbbbbbbyyorrrrrroyybyogybwwwwwwwww'
        theCube = Cube(encodedCube)
        result = _isUpCrossSolved(theCube)
        self.assertEqual(result, False)
        
    def test110_upFaceCross_isUpCrossSolvedShouldReturnTrue(self):
        encodedCube = 'gbbggggggyooooooooygrbbbbbbyrrrrrrrrbygyyyyyowwwwwwwww'
        theCube = Cube(encodedCube)
        result = _isUpCrossSolved(theCube)
        self.assertEqual(result, True)
        
    def test120_upFaceCross_isLOnUpFaceShouldReturnFalse(self):
        encodedCube = 'yyoggggggygrooooooyyrbbbbbbgrbrrrrrryobyyyobgwwwwwwwww'
        theCube = Cube(encodedCube)
        result = _isLOnUpFace(theCube)
        self.assertEqual(result, False)
    
    def test130_upFaceCross_isLOnUpFaceShouldReturnTrue(self):
        encodedCube = 'rooggggggyrbooooooyygbbbbbbyybrrrrrrrgobyyyygwwwwwwwww'
        theCube = Cube(encodedCube)
        result = _isLOnUpFace(theCube)
        self.assertEqual(result, True)
        
    def test140_upFaceCross_isHorizontalOnUpFaceShouldReturnFalse(self):
        encodedCube = 'ygrggggggyyroooooogrbbbbbbbyyorrrrrroyybyogybwwwwwwwww'
        theCube = Cube(encodedCube)
        result = _isHorizontalOnUpFace(theCube)
        self.assertEqual(result, False)
    
    def test150_upFaceCross_isHorizontalOnUpFaceShouldReturnTrue(self):
        encodedCube = 'yyoggggggygrooooooyyrbbbbbbgrbrrrrrryobyyyobgwwwwwwwww'
        theCube = Cube(encodedCube)
        result = _isHorizontalOnUpFace(theCube)
        self.assertEqual(result, True)
        
    def test160_upFaceCross_isLInCorrectPositionShouldReturnFalse(self):
        encodedCube = 'rooggggggyrbooooooyygbbbbbbyybrrrrrrrgobyyyygwwwwwwwww'
        theCube = Cube(encodedCube)
        result = _isLInCorrectPosition(theCube)
        self.assertEqual(result, False)
    
    def test170_upFaceCross_isLInCorrectPositionShouldReturnTrue(self):
        encodedCube = 'yygggggggyybooooooroobbbbbbyrbrrrrrrgyyyybogrwwwwwwwww'
        theCube = Cube(encodedCube)
        result = _isLInCorrectPosition(theCube)
        self.assertEqual(result, True)
        
    def test180_upFaceCross_moveLOnUpFaceToCorrectPositionShouldReturnCorrectString(self):
        encodedCube = 'yrbggggggyygooooooyybbbbbbbroorrrrrrybryyggyowwwwwwwww'
        theCube = Cube(encodedCube)
        result = _moveLOnUpFaceToCorrectPosition(theCube)
        self.assertEqual(result, 'U')
        
    def test190_upFaceCross_moveLOnUpFaceToCorrectPositionShouldReturnCorrectString(self):
        encodedCube = 'rooggggggyrbooooooyygbbbbbbyybrrrrrrrgobyyyygwwwwwwwww'
        theCube = Cube(encodedCube)
        result = _moveLOnUpFaceToCorrectPosition(theCube)
        self.assertEqual(result, 'UU')
        
    def test200_upFaceCross_moveLOnUpFaceToCorrectPositionShouldReturnCorrectString(self):
        encodedCube = 'yybggggggrooooooooyrbbbbbbbyygrrrrrroyggyyrbywwwwwwwww'
        theCube = Cube(encodedCube)
        result = _moveLOnUpFaceToCorrectPosition(theCube)
        self.assertEqual(result, 'u')
        
    def test210_upFaceCross_solveUpCrossShouldProduceCorrectlySolvedUpFaceCross(self):
        result = ''
        encodedCube = 'gobygggororryowgrgbbrrbgywoyorwrbybwbowgyyyywowwrwgbbo'
        theCube = Cube(encodedCube)
        result += solveBottomCross(theCube)
        result += solveBottomLayer(theCube)
        result += solveMiddleLayer(theCube)
        result += solveUpCross(theCube)
        self.assertEqual(_isUpCrossSolved(theCube), True)
        
        
        
        
        
        
        
        
        
        