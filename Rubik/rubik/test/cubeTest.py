import unittest
import rubik.model.cube as cube

class CubeTest(unittest.TestCase):

# Analysis of Cube
#
#    Cube: class, instance of a state machine, maintain internal state
#    Methods:    _init_    constructs cube from a serialized string
#                get       yields serialized string of internal representation
#                rotate    performs rotations on the cube per 'dir' key
#
#    Analysis: Cube.rotate
#        inputs:
#            directions: string, len .GE. 0, [FfRrBbLlUu]; optional, defaulting to F if missing; unvalidated
#        outputs:
#            side-effects:    no external effects; internal state change
#            nominal:
#                return serialized rotated cube
#            abnormal: 
#                raise DirException
#
#        happy path:
#            test 010:    F rotation
#            test 020:    f rotation
#            test 030:    R rotation
#            test 040:    r rotation
#            test 050:    B rotation
#            test 060:    b rotation
#            test 070:    L rotation
#            test 080:    l rotation
#            test 090:    U rotation
#            test 100:    u rotation
#            test 130:    empty direction, meaning ""
#            test 140:    multi-string rotation
#
#        sad path:
#            test 910:    invalid direction
#
#        evil path:
#            none

# Happy Path
#    Test that F rotates the front face clockwise
    def test_rotate_010_ShouldRotateCubeInFDirection(self):
        cubeToRotate = 'oygbggbyworroorgybwbybbbogyrwbwryrwwgogrygwryrooowgbwy'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('F')
        self.assertEqual(rotatedCube, 'bboygywggwrrroryybwbybbbogyrwrwrorwogogrygwybgooowgbwy')
        
#    Test that f rotates the front face counter-clockwise        
    def test_rotate_020_ShouldRotateCubeInfDirection(self):
        cubeToRotate = 'oygbggbyworroorgybwbybbbogyrwbwryrwwgogrygwryrooowgbwy'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('f')
        self.assertEqual(rotatedCube, 'ggwygyobborroorrybwbybbbogyrwywrrrwwgogrygoogbywowgbwy')
    
#    Test that R rotates the right face clockwise    
    def test_rotate_030_ShouldRotateCubeinRDirection(self):
        cubeToRotate = 'oygbggbyworroorgybwbybbbogyrwbwryrwwgogrygwryrooowgbwy'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('R')
        self.assertEqual(rotatedCube, 'oyobggbyygooyorbrrybygbbggyrwbwryrwwgogrygwrwrooowbbww')
        
#    Test that r rotates the right face counter-clockwise     
    def test_rotate_040_ShouldRotateCubeinrDirection(self):
        cubeToRotate = 'oygbggbyworroorgybwbybbbogyrwbwryrwwgogrygwryrooowgbwy'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('r')
        self.assertEqual(rotatedCube, 'oygbggbyyrrbroyoogybygbbogyrwbwryrwwgoorybwrwrogowgbww')
        
#    Test that B rotates the back face clockwise     
    def test_rotate_050_ShouldRotateCubeinBDirection(self):
        cubeToRotate = 'oygbggbyworroorgybwbybbbogyrwbwryrwwgogrygwryrooowgbwy'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('B')
        self.assertEqual(rotatedCube, 'oygbggbyworyoowgybobwgbbybygwborygwwrrbrygwryrooowgrwr')
        
#    Test that b rotates the back face counter-clockwise     
    def test_rotate_060_ShouldRotateCubeinbDirection(self):
        cubeToRotate = 'oygbggbyworroorgybwbybbbogyrwbwryrwwgogrygwryrooowgbwy'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('b')
        self.assertEqual(rotatedCube, 'oygbggbyworgooogygybybbgwbobwbwryywwrwrrygwryrooowgbrr')
        
#    Test that L rotates the left face clockwise     
    def test_rotate_070_ShouldRotateCubeinLDirection(self):
        cubeToRotate = 'oygbggbyworroorgybwbybbbogyrwbwryrwwgogrygwryrooowgbwy'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('L')
        self.assertEqual(rotatedCube, 'gygrggwyworroorgybwbbbboogrrwrwrwwybyogbygyryooobwgbwy')
        
#    Test that l rotates the left face counter-clockwise     
    def test_rotate_080_ShouldRotateCubeinlDirection(self):
        cubeToRotate = 'oygbggbyworroorgybwbybbbogyrwbwryrwwgogrygwryrooowgbwy'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('l')
        self.assertEqual(rotatedCube, 'rygoggbyworroorgybwbwbbroggbywwrwrwroogbygbryyoobwgywy')
        
#    Test that U rotates the up face clockwise     
    def test_rotate_090_ShouldRotateCubeinUDirection(self):
        cubeToRotate = 'oygbggbyworroorgybwbybbbogyrwbwryrwwgogrygwryrooowgbwy'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('U')
        self.assertEqual(rotatedCube, 'orrbggbywwbyoorgybrwbbbbogyoygwryrwwwrgryoyggrooowgbwy')
        
#    Test that u rotates the up face counter-clockwise     
    def test_rotate_100_ShouldRotateCubeinuDirection(self):
        cubeToRotate = 'oygbggbyworroorgybwbybbbogyrwbwryrwwgogrygwryrooowgbwy'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('u')
        self.assertEqual(rotatedCube, 'rwbbggbywoygoorgyborrbbbogywbywryrwwggyoyrgrwrooowgbwy')
              
#    Test that the cube defaults to rotating by F when dir is empty     
    def test_rotate_110_ShouldRotateCubeInFDirectionWhenDirIsEmpty(self):
        cubeToRotate = 'oygbggbyworroorgybwbybbbogyrwbwryrwwgogrygwryrooowgbwy'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('')
        self.assertEqual(rotatedCube, 'bboygywggwrrroryybwbybbbogyrwrwrorwogogrygwybgooowgbwy')
                   
#    Test that the cube is rotated by multiple directions when they are given
    def test_rotate_120_ShouldRotateCubeCorrectlyWhenGivenMultipleDirections(self):
        cubeToRotate = 'oygbggbyworroorgybwbybbbogyrwbwryrwwgogrygwryrooowgbwy'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('Ff')
        self.assertEqual(rotatedCube, 'oygbggbyworroorgybwbybbbogyrwbwryrwwgogrygwryrooowgbwy')
    
    
    
    
    
    
    
    
    
    
    