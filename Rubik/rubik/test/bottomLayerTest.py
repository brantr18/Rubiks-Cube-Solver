from rubik.model.cube import Cube
from rubik.controller.bottomLayer import solveBottomLayer
from rubik.controller.bottomLayer import _isBottomLayerSolved

'''
Created on Feb 24, 2023

@author: Brantley
'''
import unittest


class BottomLayerTest(unittest.TestCase):


    def test100_bottomLayer_solveBottomLayerShouldProduceCorrectRotations(self):
        encodedCube = 'yrrggbwgogbgyoggoorowybbbbyoororrbrrggwyyrbyybwywwwoww'
        theCube = Cube(encodedCube)
        result = solveBottomLayer(theCube)
        self.assertEqual(result, 'UUfuFluLluLUluLuLUlLUluLUl')
        
    def test110_bottomLayer_isBottomLayerSolvedShouldReturnFalse(self):
        encodedCube = 'yrrggbwgogbgyoggoorowybbbbyoororrbrrggwyyrbyybwywwwoww'
        theCube = Cube(encodedCube)
        result = _isBottomLayerSolved(theCube)
        self.assertEqual(result, False)
        
    def test120_bottomLayer_isBottomLayerSolvedShouldReturnTrue(self):
        encodedCube = 'oroygbgggboyrogooobbgybgbbbyogorrrrrryryybygywwwwwwwww'
        theCube = Cube(encodedCube)
        result = _isBottomLayerSolved(theCube)
        self.assertEqual(result, True)