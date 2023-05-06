from rubik.controller.bottomCross import solveBottomCross
from rubik.controller.bottomLayer import solveBottomLayer
from rubik.controller.middleLayer import solveMiddleLayer
from rubik.controller.upFaceCross import solveUpCross
from rubik.controller.upFaceSurface import solveUpSurface
from rubik.controller.upperLayer import solveUpperLayer
from rubik.model.cube import Cube
from rubik.model.constants import *
from rubik.model.exceptions import CubeException
import hashlib
import random

def solve(parms):
    """Return rotates needed to solve input cube"""
    result = {}
     
    for key in parms:
    
        if key not in VALID_SOLVE_KEYS:
    
            result['status'] = 'error: extraneous key detected'
            return result
     
     
    try:   
        encodedCube = parms.get('cube')
        theCube = Cube(encodedCube)
    
    except CubeException:
        result['status'] = 'error: invalid cube'
        return result
    
    rotations = ""
    rotations += solveBottomCross(theCube)      #iteration 2
    rotations += solveBottomLayer(theCube)      #iteration 3
    rotations += solveMiddleLayer(theCube)      #iteration 4
    rotations += solveUpCross(theCube)          #iteration 5
    rotations += solveUpSurface(theCube)        #iteration 5
    rotations += solveUpperLayer(theCube)       #iteration 6
    
    result['solution'] = rotations
    result['status'] = 'ok'    
    
    token = _tokenize(encodedCube, rotations)
    startIndex = random.randint(0, len(token) - 8)
    substring = token[startIndex:startIndex + 8]
    
    result['integrity'] = substring             #iteration 3
                     
    return result


def _tokenize(inputCube, solutionString):
    username = 'bar0065'
    
    itemToTokenize = inputCube + solutionString + username
    sha256Hash = hashlib.sha256()
    sha256Hash.update(itemToTokenize.encode())
    fullToken = sha256Hash.hexdigest()
    
    return fullToken
    
    
    
    
    