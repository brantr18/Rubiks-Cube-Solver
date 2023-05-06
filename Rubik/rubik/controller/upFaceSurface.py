from rubik.model.constants import *
from rubik.model.cube import Cube

def solveUpSurface(theCube: Cube) -> str:
    '''
        This is the top-level function  for rotating
        a cube so that the up face is solved.
        
        input:  an instance of the cube class with up-face cross solved
        output: the rotations required to solve the up surface  
    '''  
    
    if _isUpSurfaceSolved(theCube):
        return ''
    
    result = ''
    
    while not _isUpSurfaceSolved(theCube):
        
        if _isFishOnUpSurface(theCube):
            
            if _isFishInBottomLeftCornerOnUpSurface(theCube):
                
                theCube.rotate('RUrURUUr')
                result += 'RUrURUUr'
                
            else:
                result += _moveFishToBottomLeftCornerOnUpSurface(theCube)
                
        else:
            if _isLTREqualtoUMM(theCube):
                
                theCube.rotate('RUrURUUr')
                result += 'RUrURUUr'
                
            else:
                result += _moveUMMToLTR(theCube)
                
    return result



def _isUpSurfaceSolved(theCube: Cube) -> bool:
    if theCube.get()[UTL] == theCube.get()[UMM] and \
       theCube.get()[UTM] == theCube.get()[UMM] and \
       theCube.get()[UTR] == theCube.get()[UMM] and \
       theCube.get()[UML] == theCube.get()[UMM] and \
       theCube.get()[UMR] == theCube.get()[UMM] and \
       theCube.get()[UBL] == theCube.get()[UMM] and \
       theCube.get()[UBM] == theCube.get()[UMM] and \
       theCube.get()[UBR] == theCube.get()[UMM]:
        return True
    return False


def _isFishOnUpSurface(theCube: Cube) -> bool:
    if theCube.get()[UTL] == theCube.get()[UMM] and \
       theCube.get()[UTR] != theCube.get()[UMM] and \
       theCube.get()[UBL] != theCube.get()[UMM] and \
       theCube.get()[UBR] != theCube.get()[UMM] or \
       theCube.get()[UTR] == theCube.get()[UMM] and \
       theCube.get()[UTL] != theCube.get()[UMM] and \
       theCube.get()[UBL] != theCube.get()[UMM] and \
       theCube.get()[UBR] != theCube.get()[UMM] or \
       theCube.get()[UBL] == theCube.get()[UMM] and \
       theCube.get()[UTR] != theCube.get()[UMM] and \
       theCube.get()[UBR] != theCube.get()[UMM] and \
       theCube.get()[UTL] != theCube.get()[UMM] or \
       theCube.get()[UBR] == theCube.get()[UMM] and \
       theCube.get()[UTR] != theCube.get()[UMM] and \
       theCube.get()[UBL] != theCube.get()[UMM] and \
       theCube.get()[UTL] != theCube.get()[UMM]:
        return True
    return False


def _isFishInBottomLeftCornerOnUpSurface(theCube: Cube) -> bool:
    if theCube.get()[UBL] == theCube.get()[UMM] and \
       theCube.get()[UTR] != theCube.get()[UMM] and \
       theCube.get()[UBR] != theCube.get()[UMM] and \
       theCube.get()[UTL] != theCube.get()[UMM]:
        return True
    return False


def _moveFishToBottomLeftCornerOnUpSurface(theCube: Cube) -> str:
    result = ''
    
    if theCube.get()[UBR] == theCube.get()[UMM]:
        theCube.rotate('U')
        result += 'U'
        
    elif theCube.get()[UTR] == theCube.get()[UMM]:
        theCube.rotate('UU')
        result += 'UU'
        
    elif theCube.get()[UTL] == theCube.get()[UMM]:
        theCube.rotate('u')
        result += 'u'
    
    return result


def _isLTREqualtoUMM(theCube: Cube) -> bool:
    if theCube.get()[LTR] == theCube.get()[UMM]:
        return True
    return False


def _moveUMMToLTR(theCube: Cube) -> str:
    result = ''
    
    if theCube.get()[FTR] == theCube.get()[UMM]:
        theCube.rotate('U')
        result += 'U'
        
    elif theCube.get()[RTR] == theCube.get()[UMM]:
        theCube.rotate('UU')
        result += 'UU'
        
    elif theCube.get()[BTR] == theCube.get()[UMM]:
        theCube.rotate('u')
        result += 'u'
    
    return result






