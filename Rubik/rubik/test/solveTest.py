from unittest import TestCase
from rubik.view.solve import solve
 

class SolveTest(TestCase):
        
# Happy path
#    Test that the stubbed solve returns the correct result
    def test100_solve_returnStubbedSolution(self):
        parms = {}
        parms['cube'] = 'bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)
        self.assertEqual('', result.get('solution'))
        
        
    def test_120_solve_ReturnNoRotationsWhenGivenACubeThatAlreadyHasBottomCross(self):
        parms = {}
        parms['cube'] = 'bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)
        self.assertEqual('', result.get('solution'))

# Sad path
#    Test that cube is invalid when too long
    def test120_solve_CubeIsInvalidWhenTooLong(self):
        parms = {}
        encodedCube = 'oygbggbyworroorgybwbybbbogyrwbwryrwwgogrygwryrooowgbwyy'
        parms['cube'] = encodedCube
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('error: invalid cube', result['status'])
        
#    Test that cube is invalid when too short
    def test130_solve_CubeIsInvalidWhenTooShort(self):
        parms = {}
        encodedCube = 'oygbggbyworroorgybwbybbbogyrwbwryrwwgogrygwryrooowgbw'
        parms['cube'] = encodedCube
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('error: invalid cube', result['status'])
        
#    Test that cube is invalid when it is empty, meaning ''
    def test140_solve_CubeIsInvalidWhenCubeIsEmpty(self):
        parms = {}
        encodedCube = ''
        parms['cube'] = encodedCube
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('error: invalid cube', result['status'])
        
#    Test that cube is invalid when cube is missing
    def test150_solve_CubeIsInvalidWhenCubeIsMissing(self):
        parms = {}
        encodedCube = None
        parms['cube'] = encodedCube
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('error: invalid cube', result['status'])
        
#    Test that cube is invalid when there are not exactly 6 unique characters
    def test160_solve_CubeIsInvalidWhenThereAreNot6UniqueCharacters(self):
        parms = {}
        encodedCube = 'bbbbbbbbbyyyyyyyyywwwwwwwwwooooooooorrrrrrrrrrrrrrrrrr'
        parms['cube'] = encodedCube
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('error: invalid cube', result['status'])
        
#    Test that cube is invalid when there are not exactly 9 of each of the 6 unique characters
    def test170_solve_CubeIsInvalidWhenThereAreNot9OfEachOfThe6UniqueCharacters(self):
        parms = {}
        encodedCube = 'bbbbbbbbbyyyyyyyyywwwwwwwwwooooooooorrrrrrrrrrrrrrrggg'
        parms['cube'] = encodedCube
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('error: invalid cube', result['status'])
        
#    Test that cube is invalid when the middle of each face is not unique
    def test180_solve_CubeIsInvalidWhenMiddleOfEachFaceIsNotUnique(self):
        parms = {}
        encodedCube = 'bbbbbbbbgyyyyyyyyywwwwwwwwwooooooooorrrrrrrrrggggbgggg'
        parms['cube'] = encodedCube
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('error: invalid cube', result['status'])
        
#    Test that cube is invalid when there are characters outside of the range [A-Z, a-z, 0-9]
    def test190_solve_CubeIsInvalidWhenInvalidCharactersForCubeAreDetected(self):
        parms = {}
        encodedCube = '000000000yyyyyyyyywwwwwwwwwVVVVVVVVVrrrrrrrrr$$$$$$$$$'
        parms['cube'] = encodedCube
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('error: invalid cube', result['status'])
        
#    Test that an error occurs when there is an unsupported key passed in
    def test200_solve_ErrorThrownWhenExtraneousKeysDetected(self):
        parms = {}
        encodedCube = 'bbbbbbbbbyyyyyyyyywwwwwwwwwooooooooorrrrrrrrrggggggggg'
        parms['cube'] = encodedCube
        parms['anotherkey'] = 'anothervalue'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('error: extraneous key detected', result['status'])