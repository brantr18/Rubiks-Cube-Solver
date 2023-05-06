from rubik.model.cube import Cube
from rubik.controller.bottomCross import solveBottomCross
from rubik.controller.bottomLayer import solveBottomLayer
from rubik.controller.middleLayer import solveMiddleLayer
from rubik.controller.upFaceCross import solveUpCross
from rubik.controller.upFaceSurface import solveUpSurface
from rubik.controller.upFaceSurface import _isUpSurfaceSolved
from rubik.controller.upFaceSurface import _isFishOnUpSurface
from rubik.controller.upFaceSurface import _isFishInBottomLeftCornerOnUpSurface
from rubik.controller.upFaceSurface import _moveFishToBottomLeftCornerOnUpSurface
from rubik.controller.upFaceSurface import _isLTREqualtoUMM
from rubik.controller.upFaceSurface import _moveUMMToLTR
'''
Created on Apr 4, 2023

@author: Brantley
'''
import unittest


class UpFaceSurfaceTest(unittest.TestCase):


    def test100_upFaceSurface_isUpSurfaceSolvedShouldReturnFalse(self):
        encodedCube = 'bggggggggoobooooooyrrbbbbbbgbyrrrrrryyoyyyryywwwwwwwww'
        theCube = Cube(encodedCube)
        result = _isUpSurfaceSolved(theCube)
        self.assertEqual(result, False)
        
    def test110_upFaceSurface_isUpSurfaceSolvedShouldReturnTrue(self):
        encodedCube = 'ogbggggggrbroooooogoobbbbbbbrgrrrrrryyyyyyyyywwwwwwwww'
        theCube = Cube(encodedCube)
        result = _isUpSurfaceSolved(theCube)
        self.assertEqual(result, True)
        
    def test120_upFaceSurface_isFishOnUpSurfaceShouldReturnFalse(self):
        encodedCube = 'bggggggggoobooooooyrrbbbbbbgbyrrrrrryyoyyyryywwwwwwwww'
        theCube = Cube(encodedCube)
        result = _isFishOnUpSurface(theCube)
        self.assertEqual(result, False)
    
    def test130_upFaceSurface_isFishOnUpSurfaceShouldReturnTrue(self):
        encodedCube = 'gbbggggggyooooooooygrbbbbbbyrrrrrrrrbygyyyyyowwwwwwwww'
        theCube = Cube(encodedCube)
        result = _isFishOnUpSurface(theCube)
        self.assertEqual(result, True)
        
    def test140_upFaceSurface_isFishInBottomLeftCornerOnUpSurfaceShouldReturnFalse(self):
        encodedCube = 'oobggggggyrroooooogbybbbbbbbggrrrrrrryyyyyyyowwwwwwwww'
        theCube = Cube(encodedCube)
        result = _isFishInBottomLeftCornerOnUpSurface(theCube)
        self.assertEqual(result, False)
    
    def test150_upFaceSurface_isFishInBottomLeftCornerOnUpSurfaceShouldReturnTrue(self):
        encodedCube = 'gbbggggggyooooooooygrbbbbbbyrrrrrrrrbygyyyyyowwwwwwwww'
        theCube = Cube(encodedCube)
        result = _isFishInBottomLeftCornerOnUpSurface(theCube)
        self.assertEqual(result, True)
        
    def test160_upFaceSurface_moveFishToBottomLeftCornerOnUpSurfaceShouldReturnCorrectString(self):
        encodedCube = 'bbrggggggggyooooooooybbbbbbgryrrrrrroybyyyryywwwwwwwww'
        theCube = Cube(encodedCube)
        result = _moveFishToBottomLeftCornerOnUpSurface(theCube)
        self.assertEqual(result, 'U')
        
    def test170_upFaceSurface_moveFishToBottomLeftCornerOnUpSurfaceShouldReturnCorrectString(self):
        encodedCube = 'gryggggggbbrooooooggybbbbbbooyrrrrrrbyyyyyoyrwwwwwwwww'
        theCube = Cube(encodedCube)
        result = _moveFishToBottomLeftCornerOnUpSurface(theCube)
        self.assertEqual(result, 'UU')
        
    def test180_upFaceSurface_moveFishToBottomLeftCornerOnUpSurfaceShouldReturnCorrectString(self):
        encodedCube = 'ooygggggggryoooooobbrbbbbbbggyrrrrrryyryyybyowwwwwwwww'
        theCube = Cube(encodedCube)
        result = _moveFishToBottomLeftCornerOnUpSurface(theCube)
        self.assertEqual(result, 'u')
        
    def test190_upFaceSurface_isLTREqualtoUMMShouldReturnFalse(self):
        encodedCube = 'bbrggggggggrooooooyrybbbbbbgoorrrrrroybyyyyyywwwwwwwww'
        theCube = Cube(encodedCube)
        result = _isLTREqualtoUMM(theCube)
        self.assertEqual(result, False)
    
    def test200_upFaceSurface_isLTREqualtoUMMShouldReturnTrue(self):
        encodedCube = 'googgggggbbrooooooggrbbbbbbyryrrrrrrbyyyyyoyywwwwwwwww'
        theCube = Cube(encodedCube)
        result = _isLTREqualtoUMM(theCube)
        self.assertEqual(result, True)
        
    def test210_upFaceSurface_moveUMMToLTRShouldReturnCorrectString(self):
        encodedCube = 'yrygggggggoooooooobbrbbbbbbggrrrrrrryyyyyybyowwwwwwwww'
        theCube = Cube(encodedCube)
        result = _moveUMMToLTR(theCube)
        self.assertEqual(result, 'U')
        
    def test220_upFaceSurface_moveUMMToLTRShouldReturnCorrectString(self):
        encodedCube = 'ggrggggggyryoooooogoobbbbbbbbrrrrrrryyoyyyyybwwwwwwwww'
        theCube = Cube(encodedCube)
        result = _moveUMMToLTR(theCube)
        self.assertEqual(result, 'UU')
        
    def test230_upFaceSurface_moveUMMToLTRShouldReturnCorrectString(self):
        encodedCube = 'bbrggggggggrooooooyrybbbbbbgoorrrrrroybyyyyyywwwwwwwww'
        theCube = Cube(encodedCube)
        result = _moveUMMToLTR(theCube)
        self.assertEqual(result, 'u')
        
    def test240_upFaceSurface_solveUpSurfaceShouldProduceCorrectlySolvedUpFaceCross(self):
        result = ''
        encodedCube = 'gobygggororryowgrgbbrrbgywoyorwrbybwbowgyyyywowwrwgbbo'
        theCube = Cube(encodedCube)
        result += solveBottomCross(theCube)
        result += solveBottomLayer(theCube)
        result += solveMiddleLayer(theCube)
        result += solveUpCross(theCube)
        result += solveUpSurface(theCube)
        self.assertEqual(_isUpSurfaceSolved(theCube), True)
        
        