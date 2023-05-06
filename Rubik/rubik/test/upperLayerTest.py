from rubik.model.cube import Cube
from rubik.controller.bottomCross import solveBottomCross
from rubik.controller.bottomLayer import solveBottomLayer
from rubik.controller.middleLayer import solveMiddleLayer
from rubik.controller.upFaceCross import solveUpCross
from rubik.controller.upFaceSurface import solveUpSurface
from rubik.controller.upperLayer import solveUpperLayer
from rubik.controller.upperLayer import _isUpperLayerSolved
from rubik.controller.upperLayer import _areAllCornersSolved
from rubik.controller.upperLayer import _moveCornersToFrontFace
from rubik.controller.upperLayer import _moveCornersToRightFace
from rubik.controller.upperLayer import _moveCornersToBackFace
from rubik.controller.upperLayer import _moveCornersToLeftFace
from rubik.controller.upperLayer import _moveSolvedCornersToCorrectFace
from rubik.controller.upperLayer import _solveCorners
from rubik.controller.upperLayer import _solveMiddles
'''
Created on Apr 14, 2023

@author: Brantley
'''
import unittest


class UpperLayerTest(unittest.TestCase):


    def test100_upperLayer_isUpperLayerSolvedShouldReturnFalse(self):
        encodedCube = 'bgrgggggggoboooooorrgbbbbbboborrrrrryyyyyyyyywwwwwwwww'
        theCube = Cube(encodedCube)
        result = _isUpperLayerSolved(theCube)
        self.assertEqual(result, False)
        
    def test110_upperLayer_isUpperLayerSolvedShouldReturnTrue(self):
        encodedCube = 'gggggggggooooooooobbbbbbbbbrrrrrrrrryyyyyyyyywwwwwwwww'
        theCube = Cube(encodedCube)
        result = _isUpperLayerSolved(theCube)
        self.assertEqual(result, True)
        
    def test120_upperLayer_areAllCornersSolvedShouldReturnFalse(self):
        encodedCube = 'bgrgggggggoboooooorrgbbbbbboborrrrrryyyyyyyyywwwwwwwww'
        theCube = Cube(encodedCube)
        result = _areAllCornersSolved(theCube)
        self.assertEqual(result, False)
        
    def test130_upperLayer_areAllCornersSolvedShouldReturnTrue(self):
        encodedCube = 'grgggggggooooooooobgbbbbbbbrbrrrrrrryyyyyyyyywwwwwwwww'
        theCube = Cube(encodedCube)
        result = _areAllCornersSolved(theCube)
        self.assertEqual(result, True)
        
    def test140_upperLayer_moveCornersToFrontFaceShouldReturnCorrectString(self):
        encodedCube = 'borgggggggggooooooorbbbbbbbrborrrrrryyyyyyyyywwwwwwwww'
        theCube = Cube(encodedCube)
        result = _moveCornersToFrontFace(theCube)
        self.assertEqual(result, 'U')
        
    def test150_upperLayer_moveCornersToFrontFaceShouldReturnCorrectString(self):
        encodedCube = 'rboggggggboroooooogggbbbbbborbrrrrrryyyyyyyyywwwwwwwww'
        theCube = Cube(encodedCube)
        result = _moveCornersToFrontFace(theCube)
        self.assertEqual(result, 'UU')
        
    def test160_upperLayer_moveCornersToFrontFaceShouldReturnCorrectString(self):
        encodedCube = 'orbggggggrboooooooborbbbbbbgggrrrrrryyyyyyyyywwwwwwwww'
        theCube = Cube(encodedCube)
        result = _moveCornersToFrontFace(theCube)
        self.assertEqual(result, 'u')
        
    def test170_upperLayer_moveCornersToRightFaceShouldReturnCorrectString(self):
        encodedCube = 'gobggggggrrgooooooobobbbbbbbgrrrrrrryyyyyyyyywwwwwwwww'
        theCube = Cube(encodedCube)
        result = _moveCornersToRightFace(theCube)
        self.assertEqual(result, 'U')
        
    def test180_upperLayer_moveCornersToRightFaceShouldReturnCorrectString(self):
        encodedCube = 'bgrgggggggoboooooorrgbbbbbboborrrrrryyyyyyyyywwwwwwwww'
        theCube = Cube(encodedCube)
        result = _moveCornersToRightFace(theCube)
        self.assertEqual(result, 'UU')
        
    def test190_upperLayer_moveCornersToRightFaceShouldReturnCorrectString(self):
        encodedCube = 'oboggggggbgroooooogobbbbbbbrrgrrrrrryyyyyyyyywwwwwwwww'
        theCube = Cube(encodedCube)
        result = _moveCornersToRightFace(theCube)
        self.assertEqual(result, 'u')
        
    def test200_upperLayer_moveCornersToBackFaceShouldReturnCorrectString(self):
        encodedCube = 'rrgggggggogroooooogbobbbbbbbobrrrrrryyyyyyyyywwwwwwwww'
        theCube = Cube(encodedCube)
        result = _moveCornersToBackFace(theCube)
        self.assertEqual(result, 'U')
        
    def test210_upperLayer_moveCornersToBackFaceShouldReturnCorrectString(self):
        encodedCube = 'bobggggggrrgooooooogrbbbbbbgborrrrrryyyyyyyyywwwwwwwww'
        theCube = Cube(encodedCube)
        result = _moveCornersToBackFace(theCube)
        self.assertEqual(result, 'UU')
        
    def test220_upperLayer_moveCornersToBackFaceShouldReturnCorrectString(self):
        encodedCube = 'gboggggggboboooooorrgbbbbbbogrrrrrrryyyyyyyyywwwwwwwww'
        theCube = Cube(encodedCube)
        result = _moveCornersToBackFace(theCube)
        self.assertEqual(result, 'u')
        
    def test230_upperLayer_moveCornersToLeftFaceShouldReturnCorrectString(self):
        encodedCube = 'rgrgggggggbooooooobrgbbbbbboobrrrrrryyyyyyyyywwwwwwwww'
        theCube = Cube(encodedCube)
        result = _moveCornersToLeftFace(theCube)
        self.assertEqual(result, 'U')
        
    def test240_upperLayer_moveCornersToLeftFaceShouldReturnCorrectString(self):
        encodedCube = 'oobggggggrgroooooogbobbbbbbbrgrrrrrryyyyyyyyywwwwwwwww'
        theCube = Cube(encodedCube)
        result = _moveCornersToLeftFace(theCube)
        self.assertEqual(result, 'UU')
        
    def test250_upperLayer_moveCornersToLeftFaceShouldReturnCorrectString(self):
        encodedCube = 'brgggggggooboooooorgrbbbbbbgborrrrrryyyyyyyyywwwwwwwww'
        theCube = Cube(encodedCube)
        result = _moveCornersToLeftFace(theCube)
        self.assertEqual(result, 'u')
        
    def test260_upperLayer_moveSolvedCornersToCorrectFaceShouldReturnCorrectString(self):
        encodedCube = 'rgrgggggggbooooooobrgbbbbbboobrrrrrryyyyyyyyywwwwwwwww'
        theCube = Cube(encodedCube)
        result = _moveSolvedCornersToCorrectFace(theCube)
        self.assertEqual(result, 'U')
        
    def test270_upperLayer_moveSolvedCornersToCorrectFaceShouldReturnCorrectString(self):
        encodedCube = 'bobggggggrrgooooooogrbbbbbbgborrrrrryyyyyyyyywwwwwwwww'
        theCube = Cube(encodedCube)
        result = _moveSolvedCornersToCorrectFace(theCube)
        self.assertEqual(result, 'UU')
        
    def test280_upperLayer_moveSolvedCornersToCorrectFaceShouldReturnCorrectString(self):
        encodedCube = 'orbggggggrboooooooborbbbbbbgggrrrrrryyyyyyyyywwwwwwwww'
        theCube = Cube(encodedCube)
        result = _moveSolvedCornersToCorrectFace(theCube)
        self.assertEqual(result, 'u')
        
    def test290_upperLayer_solveCornersShouldReturnCorrectString(self):
        encodedCube = 'gggggggggorboooooorbobbbbbbborrrrrrryyyyyyyyywwwwwwwww'
        theCube = Cube(encodedCube)
        result = _solveCorners(theCube)
        self.assertEqual(result, 'fUBuFUbBUbUBUUb')
        
    def test300_upperLayer_solveCornersShouldReturnCorrectString(self):
        encodedCube = 'rrgggggggobooooooobgrbbbbbbgobrrrrrryyyyyyyyywwwwwwwww'
        theCube = Cube(encodedCube)
        result = _solveCorners(theCube)
        self.assertEqual(result, 'rULuRUlLUlULUUl')
        
    def test310_upperLayer_solveCornersShouldReturnCorrectString(self):
        encodedCube = 'ogrgggggggbooooooobobbbbbbbrrgrrrrrryyyyyyyyywwwwwwwww'
        theCube = Cube(encodedCube)
        result = _solveCorners(theCube)
        self.assertEqual(result, 'bUFuBUfFUfUFUUf')
        
    def test320_upperLayer_solveCornersShouldReturnCorrectString(self):
        encodedCube = 'gboggggggbrgoooooooobbbbbbbrgrrrrrrryyyyyyyyywwwwwwwww'
        theCube = Cube(encodedCube)
        result = _solveCorners(theCube)
        self.assertEqual(result, 'lURuLUrRUrURUUr')
        
    def test330_upperLayer_solveCornersShouldReturnCorrectString(self):
        encodedCube = 'rboggggggbrgooooooogrbbbbbbgobrrrrrryyyyyyyyywwwwwwwww'
        theCube = Cube(encodedCube)
        result = _solveCorners(theCube)
        self.assertEqual(result, 'lURuLUrRUrURUUr')
        
    def test340_upperLayer_solveMiddlesShouldReturnCorrectString(self):
        encodedCube = 'gggggggggobooooooobrbbbbbbbrorrrrrrryyyyyyyyywwwwwwwww'
        theCube = Cube(encodedCube)
        result = _solveMiddles(theCube)
        self.assertEqual(result, 'BBUlRBBrLUBB')
        
    def test350_upperLayer_solveMiddlesShouldReturnCorrectString(self):
        encodedCube = 'gbgggggggooooooooobrbbbbbbbrgrrrrrrryyyyyyyyywwwwwwwww'
        theCube = Cube(encodedCube)
        result = _solveMiddles(theCube)
        self.assertEqual(result, 'LLUfBLLbFULL')
        
    def test360_upperLayer_solveMiddlesShouldReturnCorrectString(self):
        encodedCube = 'gogggggggorooooooobbbbbbbbbrgrrrrrrryyyyyyyyywwwwwwwww'
        theCube = Cube(encodedCube)
        result = _solveMiddles(theCube)
        self.assertEqual(result, 'FFUrLFFlRUFF')
        
    def test370_upperLayer_solveMiddlesShouldReturnCorrectString(self):
        encodedCube = 'gogggggggobooooooobgbbbbbbbrrrrrrrrryyyyyyyyywwwwwwwww'
        theCube = Cube(encodedCube)
        result = _solveMiddles(theCube)
        self.assertEqual(result, 'RRUbFRRfBURR')
        
    def test380_upperLayer_solveMiddlesShouldReturnCorrectString(self):
        encodedCube = 'gogggggggogooooooobrbbbbbbbrbrrrrrrryyyyyyyyywwwwwwwww'
        theCube = Cube(encodedCube)
        result = _solveMiddles(theCube)
        self.assertEqual(result, 'FFUrLFFlRUFF')
        
    def test390_upperLayer_solveUpperLayerShouldReturnCorrectString(self):
        result = ''
        encodedCube = 'gobygggororryowgrgbbrrbgywoyorwrbybwbowgyyyywowwrwgbbo'
        theCube = Cube(encodedCube)
        result += solveBottomCross(theCube)
        result += solveBottomLayer(theCube)
        result += solveMiddleLayer(theCube)
        result += solveUpCross(theCube)
        result += solveUpSurface(theCube)
        result += solveUpperLayer(theCube)
        self.assertEqual(_isUpperLayerSolved(theCube), True)
        
        
        