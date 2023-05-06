from rubik.model.constants import *
from rubik.model.cube import Cube

def solveUpCross(theCube: Cube) -> str:
    '''
        This is the top-level function  for rotating
        a cube into the up-face cross configuration.
        
        input:  an instance of the cube class with the middle layer solved
        output: the rotations required to solve the up-face cross  
    '''  
    
    if _isUpCrossSolved(theCube):
        return ''
    
    result = ''
    
    while not _isUpCrossSolved(theCube):
        
        if _isHorizontalOnUpFace(theCube):
            theCube.rotate('U')
            result += 'U'
        
        elif _isLOnUpFace(theCube) and not _isLInCorrectPosition(theCube):
            result += _moveLOnUpFaceToCorrectPosition(theCube)
            
        else:
            theCube.rotate('FURurf')
            result += 'FURurf'
    
    
    return result



def _isUpCrossSolved(theCube:Cube) -> bool:
    if theCube.get()[UTM] == theCube.get()[UMM] and \
       theCube.get()[UML] == theCube.get()[UMM] and \
       theCube.get()[UBM] == theCube.get()[UMM] and \
       theCube.get()[UMR] == theCube.get()[UMM]:
        return True
    return False

def _isLOnUpFace(theCube: Cube) -> bool:
    if theCube.get()[UTM] == theCube.get()[UMM] and \
       theCube.get()[UML] == theCube.get()[UMM] or \
       theCube.get()[UML] == theCube.get()[UMM] and \
       theCube.get()[UBM] == theCube.get()[UMM] or \
       theCube.get()[UBM] == theCube.get()[UMM] and \
       theCube.get()[UMR] == theCube.get()[UMM] or \
       theCube.get()[UMR] == theCube.get()[UMM] and \
       theCube.get()[UTM] == theCube.get()[UMM]:
        return True
    return False

def _isHorizontalOnUpFace(theCube: Cube) -> bool:
    if theCube.get()[UML] == theCube.get()[UMM] and \
       theCube.get()[UMR] == theCube.get()[UMM] and \
       theCube.get()[UTM] != theCube.get()[UMM] and \
       theCube.get()[UBM] != theCube.get()[UMM]:
        return True
    return False

def _isLInCorrectPosition(theCube: Cube) -> bool:
    if theCube.get()[UTM] == theCube.get()[UMM] and theCube.get()[UML] == theCube.get()[UMM]:
        return True
    return False

def _moveLOnUpFaceToCorrectPosition(theCube: Cube) -> str:
    result = ''
    
    if theCube.get()[UML] == theCube.get()[UMM] and theCube.get()[UBM] == theCube.get()[UMM]:
        theCube.rotate('U')
        result += 'U'
    
    elif theCube.get()[UBM] == theCube.get()[UMM] and theCube.get()[UMR] == theCube.get()[UMM]:
        theCube.rotate('UU')
        result += 'UU'
        
    elif theCube.get()[UMR] == theCube.get()[UMM] and theCube.get()[UTM] == theCube.get()[UMM]:
        theCube.rotate('u')
        result += 'u'
        
    return result
    
    
    
