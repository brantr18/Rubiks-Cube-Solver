from unittest import TestCase
from rubik.view.rotate import rotate
 
class RotateTest(TestCase):
        
# Happy path
#    Test that the stubbed rotate returns the correct result
    def test100_rotate_returnStubbedSolution(self):
        encodedCube = 'oygbggbyworroorgybwbybbbogyrwbwryrwwgogrygwryrooowgbwy'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'F'
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertEqual(result['cube'], 'bboygywggwrrroryybwbybbbogyrwrwrorwogogrygwybgooowgbwy')

#    Test that F is the default direction when dir is missing from the input
    def test110_rotate_DefaultDirectionToFWhenDirIsMissing(self):
        encodedCube = 'oygbggbyworroorgybwbybbbogyrwbwryrwwgogrygwryrooowgbwy'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = None
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertEqual(result['cube'], 'bboygywggwrrroryybwbybbbogyrwrwrorwogogrygwybgooowgbwy')
        
# Sad Path
#    Test that cube is invalid when too long
    def test120_rotate_CubeIsInvalidWhenTooLong(self):
        encodedCube = 'oygbggbyworroorgybwbybbbogyrwbwryrwwgogrygwryrooowgbwyy'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'F'
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('error: invalid cube', result['status'])
        
#    Test that cube is invalid when too short
    def test130_rotate_CubeIsInvalidWhenTooShort(self):
        encodedCube = 'oygbggbyworroorgybwbybbbogyrwbwryrwwgogrygwryrooowgbw'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'F'
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('error: invalid cube', result['status'])
        
#    Test that cube is invalid when it is empty, meaning ''
    def test140_rotate_CubeIsInvalidWhenCubeIsEmpty(self):
        encodedCube = ''
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'F'
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('error: invalid cube', result['status'])
        
#    Test that cube is invalid when cube is missing
    def test150_rotate_CubeIsInvalidWhenCubeIsMissing(self):
        encodedCube = None
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'F'
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('error: invalid cube', result['status'])
        
#    Test that cube is invalid when there are not exactly 6 unique characters
    def test160_rotate_CubeIsInvalidWhenThereAreNot6UniqueCharacters(self):
        encodedCube = 'bbbbbbbbbyyyyyyyyywwwwwwwwwooooooooorrrrrrrrrrrrrrrrrr'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'F'
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('error: invalid cube', result['status'])
        
#    Test that cube is invalid when there are not exactly 9 of each of the 6 unique characters
    def test170_rotate_CubeIsInvalidWhenThereAreNot9OfEachOfThe6UniqueCharacters(self):
        encodedCube = 'bbbbbbbbbyyyyyyyyywwwwwwwwwooooooooorrrrrrrrrrrrrrrggg'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'F'
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('error: invalid cube', result['status'])
        
#    Test that cube is invalid when the middle of each face is not unique
    def test180_rotate_CubeIsInvalidWhenMiddleOfEachFaceIsNotUnique(self):
        encodedCube = 'bbbbbbbbgyyyyyyyyywwwwwwwwwooooooooorrrrrrrrrggggbgggg'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'F'
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('error: invalid cube', result['status'])
        
#    Test that cube is invalid when there are characters outside of the range [A-Z, a-z, 0-9]
    def test190_rotate_CubeIsInvalidWhenInvalidCharactersForCubeAreDetected(self):
        encodedCube = '000000000yyyyyyyyywwwwwwwwwVVVVVVVVVrrrrrrrrr$$$$$$$$$'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'F'
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('error: invalid cube', result['status'])
        
#    Test that an error occurs when there is an unsupported key passed in
    def test200_rotate_ErrorThrownWhenExtraneousKeysDetected(self):
        encodedCube = 'bbbbbbbbbyyyyyyyyywwwwwwwwwooooooooorrrrrrrrrggggggggg'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'F'
        parms['anotherkey'] = 'anothervalue'
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('error: extraneous key detected', result['status'])
        
#    Test that an error occurs when an invalid direction is given
    def test210_rotate_DirIsInvalidWhenInvalidDirectionGiven(self):
        encodedCube = 'bbbbbbbbbyyyyyyyyywwwwwwwwwooooooooorrrrrrrrrggggggggg'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'V'
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('error: invalid direction', result['status'])
        
#    Test that an error occurs when an invalid direction is given amongst valid directions
    def test220_rotate_DirIsInvalidWhenInvalidDirectionGivenAmongstMultipleValidDirs(self):
        encodedCube = 'bbbbbbbbbyyyyyyyyywwwwwwwwwooooooooorrrrrrrrrggggggggg'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'FfRrVUlRf'
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('error: invalid direction', result['status'])
        
        
        
        
