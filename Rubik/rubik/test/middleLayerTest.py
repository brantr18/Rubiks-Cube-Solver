from rubik.model.cube import Cube
from rubik.controller.bottomCross import solveBottomCross
from rubik.controller.bottomLayer import solveBottomLayer
from rubik.controller.middleLayer import solveMiddleLayer
from rubik.controller.middleLayer import _isMiddleLayerSolved
from rubik.controller.middleLayer import _hasValidTopLayerTopFaceCombo
from rubik.controller.middleLayer import _middleMatches
from rubik.controller.middleLayer import _checkTopFaceSquareOfValidCombo
from rubik.controller.middleLayer import _checkForOffendingSquareInMiddleLayer
'''
Created on Mar 22, 2023

@author: Brantley
'''
import unittest


class MiddleLayerTest(unittest.TestCase):

    
    def test100_middleLayer_isMiddleLayerSolvedShouldReturnFalse(self):
        encodedCube = 'ygrggyggggybroooooroybbbbbbogorrrrrrbyyoybgyywwwwwwwww'
        theCube = Cube(encodedCube)
        result = _isMiddleLayerSolved(theCube)
        self.assertEqual(result, False)
        
    def test110_middleLayer_isMiddleLayerSolvedShouldReturnTrue(self):
        encodedCube = 'ygrggggggyyroooooogrbbbbbbbyyorrrrrroyybyogybwwwwwwwww'
        theCube = Cube(encodedCube)
        result = _isMiddleLayerSolved(theCube)
        self.assertEqual(result, True)
        
    def test120_middleLayer_hasValidTopLayerTopFaceComboShouldReturnFalse(self):
        encodedCube = 'royggogggrrogooooobyobbbbbbygbrrrrrrgbyyyyyygwwwwwwwww'
        theCube = Cube(encodedCube)
        result = _hasValidTopLayerTopFaceCombo(theCube)
        self.assertEqual(result, False)
        
    def test130_middleLayer_hasValidTopLayerTopFaceComboShouldReturnTrue(self):
        encodedCube = 'robggggggybyyooooorggbbbbbborbrrrrrryogyyyyyowwwwwwwww'
        theCube = Cube(encodedCube)
        result = _hasValidTopLayerTopFaceCombo(theCube)
        self.assertEqual(result, True)
        
    def test140_middleLayer_middleMatchesShouldReturnFalse(self):
        encodedCube = 'yyoygggggyrgooooooyrobbbbbbbyrrrorrryyrbygbggwwwwwwwww'
        theCube = Cube(encodedCube)
        result = _middleMatches(theCube)
        self.assertEqual(result, False)
    
    def test150_middleLayer_middleMatchesShouldReturnTrue(self):
        encodedCube = 'yroygggggbyrooooooyyobbbbbbyrgrrorrrggbgybryywwwwwwwww'
        theCube = Cube(encodedCube)
        result = _middleMatches(theCube)
        self.assertEqual(result, True)
        
    def test160_middleLayer_checkTopFaceSquareOfValidComboShouldReturnCorrectString(self):
        encodedCube = 'ggyggygggrybboooooyyrbbbbbbyyyrrrrrrbrogyooogwwwwwwwww'
        theCube = Cube(encodedCube)
        result = _checkTopFaceSquareOfValidCombo(theCube)
        self.assertEqual(result, 'URUrufuF')
        
    def test170_middleLayer_checkTopFaceSquareOfValidComboShouldReturnCorrectString(self):
        encodedCube = 'ogbygggggrgroooooogbobbbbbbbygrrrrrryyyoyyyrywwwwwwwww'
        theCube = Cube(encodedCube)
        result = _checkTopFaceSquareOfValidCombo(theCube)
        self.assertEqual(result, 'uluLUFUf')
        
    def test180_middleLayer_checkTopFaceSquareOfValidComboShouldReturnCorrectString(self):
        encodedCube = 'boygggggggogoogoooyybybbbbbryorrrrrryrrbybyyowwwwwwwww'
        theCube = Cube(encodedCube)
        result = _checkTopFaceSquareOfValidCombo(theCube)
        self.assertEqual(result, 'UBUburuR')
        
    def test190_middleLayer_checkTopFaceSquareOfValidComboShouldReturnCorrectString(self):
        encodedCube = 'bygggygggooygoooooobybbbbbbryyrrrrrrgyboygrrywwwwwwwww'
        theCube = Cube(encodedCube)
        result = _checkTopFaceSquareOfValidCombo(theCube)
        self.assertEqual(result, 'ufuFURUr')
        
    def test200_middleLayer_checkTopFaceSquareOfValidComboShouldReturnCorrectString(self):
        encodedCube = 'goyggggggoggooooooobrbbybbbyyrrrrrrrbrybyyyybwwwwwwwww'
        theCube = Cube(encodedCube)
        result = _checkTopFaceSquareOfValidCombo(theCube)
        self.assertEqual(result, 'ULUlubuB')
        
    def test210_middleLayer_checkTopFaceSquareOfValidComboShouldReturnCorrectString(self):
        encodedCube = 'yyyggggggbogooyoooobogbrbbbbrgbrrrrryoyyyyrbrwwwwwwwww'
        theCube = Cube(encodedCube)
        result = _checkTopFaceSquareOfValidCombo(theCube)
        self.assertEqual(result, 'uruRUBUb')
        
    def test220_middleLayer_checkTopFaceSquareOfValidComboShouldReturnCorrectString(self):
        encodedCube = 'gbyogggggoryoooooogyybbbbbbbrrrryrrrrgogyyyybwwwwwwwww'
        theCube = Cube(encodedCube)
        result = _checkTopFaceSquareOfValidCombo(theCube)
        self.assertEqual(result, 'UFUfuluL')
        
    def test230_middleLayer_checkTopFaceSquareOfValidComboShouldReturnCorrectString(self):
        encodedCube = 'gybggggggyyyoooooogbbbbybbbrrrrrrrrryyobyoygowwwwwwwww'
        theCube = Cube(encodedCube)
        result = _checkTopFaceSquareOfValidCombo(theCube)
        self.assertEqual(result, 'ubuBULUl')
        
    def test240_middleLayer_checkForOffendingSquareInMiddleLayerShouldReturnCorrectString(self):
        encodedCube = 'brrggoggggyygooooobyobbbbbbyyorrrrrrgorbygyyywwwwwwwww'
        theCube = Cube(encodedCube)
        result = _checkForOffendingSquareInMiddleLayer(theCube)
        self.assertEqual(result, 'RUr')
        
    def test250_middleLayer_checkForOffendingSquareInMiddleLayerShouldReturnCorrectString(self):
        encodedCube = 'grbrgggggyyoooooooyorbbbbbbybrrrgrrrbygyygyyowwwwwwwww'
        theCube = Cube(encodedCube)
        result = _checkForOffendingSquareInMiddleLayer(theCube)
        self.assertEqual(result, 'luL')
        
    def test260_middleLayer_checkForOffendingSquareInMiddleLayerShouldReturnCorrectString(self):
        encodedCube = 'rooggggggbygoobooooyrobbbbbyyyrrrrrrbrygybgyywwwwwwwww'
        theCube = Cube(encodedCube)
        result = _checkForOffendingSquareInMiddleLayer(theCube)
        self.assertEqual(result, 'BUb')
        
    def test270_middleLayer_checkForOffendingSquareInMiddleLayerShouldReturnCorrectString(self):
        encodedCube = 'broggggggyybooooooyyybbrbbbryybrrrrrgbogyorygwwwwwwwww'
        theCube = Cube(encodedCube)
        result = _checkForOffendingSquareInMiddleLayer(theCube)
        self.assertEqual(result, 'LUl')
        
    def test280_middleLayer_solveMiddleLayerShouldProduceCorrectlySolvedMiddleLayer(self):
        result = ''
        encodedCube = 'gobygggororryowgrgbbrrbgywoyorwrbybwbowgyyyywowwrwgbbo'
        theCube = Cube(encodedCube)
        result += solveBottomCross(theCube)
        result += solveBottomLayer(theCube)
        result += solveMiddleLayer(theCube)
        self.assertEqual(_isMiddleLayerSolved(theCube), True)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        