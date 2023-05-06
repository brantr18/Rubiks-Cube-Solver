from rubik.model.constants import *
from rubik.model.cube import Cube

def solveUpperLayer(theCube: Cube) -> str:
    '''
        This is the top-level function  for rotating
        a cube so that the entire upper layer is solved.
        
        input:  an instance of the cube class with up-face surface solved
        output: the rotations required to solve the upper layer  
    '''  
    if _isUpperLayerSolved(theCube):
        return ''
    
    result = ''
    
    while not _isUpperLayerSolved(theCube):
        
        result += _moveSolvedCornersToCorrectFace(theCube)
        
        if not _areAllCornersSolved(theCube):
            result += _solveCorners(theCube)
            
        elif not _isUpperLayerSolved(theCube):
            result += _solveMiddles(theCube)
            
    
    return result




def _isUpperLayerSolved(theCube: Cube) -> bool:
    if theCube.get()[FTL] == theCube.get()[FMM] and \
       theCube.get()[FTM] == theCube.get()[FMM] and \
       theCube.get()[FTR] == theCube.get()[FMM] and \
       theCube.get()[RTR] == theCube.get()[RMM] and \
       theCube.get()[RTM] == theCube.get()[RMM] and \
       theCube.get()[RTL] == theCube.get()[RMM] and \
       theCube.get()[BTR] == theCube.get()[BMM] and \
       theCube.get()[BTM] == theCube.get()[BMM] and \
       theCube.get()[BTL] == theCube.get()[BMM] and \
       theCube.get()[LTR] == theCube.get()[LMM] and \
       theCube.get()[LTM] == theCube.get()[LMM] and \
       theCube.get()[LTL] == theCube.get()[LMM]:
        return True
    return False


def _areAllCornersSolved(theCube: Cube) -> bool:
    if theCube.get()[FTR] == theCube.get()[FMM] and \
       theCube.get()[FTL] == theCube.get()[FMM] and \
       theCube.get()[RTR] == theCube.get()[RMM] and \
       theCube.get()[RTL] == theCube.get()[RMM] and \
       theCube.get()[BTR] == theCube.get()[BMM] and \
       theCube.get()[BTL] == theCube.get()[BMM] and \
       theCube.get()[LTR] == theCube.get()[LMM] and \
       theCube.get()[LTL] == theCube.get()[LMM]:
        return True
    return False


def _moveCornersToFrontFace(theCube: Cube) -> str:
    result = ''
    
    if theCube.get()[RTL] == theCube.get()[FMM] and theCube.get()[RTR] == theCube.get()[FMM]:
        theCube.rotate('U')
        result += 'U'
        
    elif theCube.get()[BTL] == theCube.get()[FMM] and theCube.get()[BTR] == theCube.get()[FMM]:
        theCube.rotate('UU')
        result += 'UU'
        
    elif theCube.get()[LTL] == theCube.get()[FMM] and theCube.get()[LTR] == theCube.get()[FMM]:
        theCube.rotate('u')
        result += 'u'
    
    return result


def _moveCornersToRightFace(theCube: Cube) -> str:
    result = ''
    
    if theCube.get()[BTL] == theCube.get()[RMM] and theCube.get()[BTR] == theCube.get()[RMM]:
        theCube.rotate('U')
        result += 'U'
        
    elif theCube.get()[LTL] == theCube.get()[RMM] and theCube.get()[LTR] == theCube.get()[RMM]:
        theCube.rotate('UU')
        result += 'UU'
        
    elif theCube.get()[FTL] == theCube.get()[RMM] and theCube.get()[FTR] == theCube.get()[RMM]:
        theCube.rotate('u')
        result += 'u'
    
    return result


def _moveCornersToBackFace(theCube: Cube) -> str:
    result = ''
    
    if theCube.get()[LTL] == theCube.get()[BMM] and theCube.get()[LTR] == theCube.get()[BMM]:
        theCube.rotate('U')
        result += 'U'
        
    elif theCube.get()[FTL] == theCube.get()[BMM] and theCube.get()[FTR] == theCube.get()[BMM]:
        theCube.rotate('UU')
        result += 'UU'
        
    elif theCube.get()[RTL] == theCube.get()[BMM] and theCube.get()[RTR] == theCube.get()[BMM]:
        theCube.rotate('u')
        result += 'u'
    
    return result


def _moveCornersToLeftFace(theCube: Cube) -> str:
    result = ''
    
    if theCube.get()[FTL] == theCube.get()[LMM] and theCube.get()[FTR] == theCube.get()[LMM]:
        theCube.rotate('U')
        result += 'U'
        
    elif theCube.get()[RTL] == theCube.get()[LMM] and theCube.get()[RTR] == theCube.get()[LMM]:
        theCube.rotate('UU')
        result += 'UU'
        
    elif theCube.get()[BTL] == theCube.get()[LMM] and theCube.get()[BTR] == theCube.get()[LMM]:
        theCube.rotate('u')
        result += 'u'
    
    return result


def _moveSolvedCornersToCorrectFace(theCube: Cube) -> str:
    result = ''
    
    squareDict = {
        FTL: FTR,
        RTL: RTR,
        BTL: BTR,
        LTL: LTR
    }
    
    for topLeftSquare, topRightSquare in squareDict.items():
    
        if theCube.get()[topLeftSquare] == theCube.get()[FMM] and theCube.get()[topRightSquare] == theCube.get()[FMM]:
            result += _moveCornersToFrontFace(theCube)
            
        elif theCube.get()[topLeftSquare] == theCube.get()[RMM] and theCube.get()[topRightSquare] == theCube.get()[RMM]:
            result += _moveCornersToRightFace(theCube)
            
        elif theCube.get()[topLeftSquare] == theCube.get()[BMM] and theCube.get()[topRightSquare] == theCube.get()[BMM]:
            result += _moveCornersToBackFace(theCube)
            
        elif theCube.get()[topLeftSquare] == theCube.get()[LMM] and theCube.get()[topRightSquare] == theCube.get()[LMM]:
            result += _moveCornersToLeftFace(theCube)
    
    return result


def _solveCorners(theCube: Cube) -> str:
    result = ''
    
    if theCube.get()[FTL] == theCube.get()[FMM] and theCube.get()[FTR] == theCube.get()[FMM]:
        theCube.rotate('fUBuFUbBUbUBUUb')
        result += 'fUBuFUbBUbUBUUb'
        
    elif theCube.get()[RTL] == theCube.get()[RMM] and theCube.get()[RTR] == theCube.get()[RMM]:
        theCube.rotate('rULuRUlLUlULUUl')
        result += 'rULuRUlLUlULUUl'
        
    elif theCube.get()[BTL] == theCube.get()[BMM] and theCube.get()[BTR] == theCube.get()[BMM]:
        theCube.rotate('bUFuBUfFUfUFUUf')
        result += 'bUFuBUfFUfUFUUf'
        
    elif theCube.get()[LTL] == theCube.get()[LMM] and theCube.get()[LTR] == theCube.get()[LMM]:
        theCube.rotate('lURuLUrRUrURUUr')
        result += 'lURuLUrRUrURUUr'
        
    else:
        theCube.rotate('lURuLUrRUrURUUr')
        result += 'lURuLUrRUrURUUr'
    
    return result


def _solveMiddles(theCube: Cube) -> str:
    result = ''
    
    if theCube.get()[FTL] == theCube.get()[FMM] and theCube.get()[FTR] == theCube.get()[FMM] and theCube.get()[FTM] == theCube.get()[FMM]:
        theCube.rotate('BBUlRBBrLUBB')
        result += 'BBUlRBBrLUBB'
        
    elif theCube.get()[RTL] == theCube.get()[RMM] and theCube.get()[RTR] == theCube.get()[RMM] and theCube.get()[RTM] == theCube.get()[RMM]:
        theCube.rotate('LLUfBLLbFULL')
        result += 'LLUfBLLbFULL'
        
    elif theCube.get()[BTL] == theCube.get()[BMM] and theCube.get()[BTR] == theCube.get()[BMM] and theCube.get()[BTM] == theCube.get()[BMM]:
        theCube.rotate('FFUrLFFlRUFF')
        result += 'FFUrLFFlRUFF'
        
    elif theCube.get()[LTL] == theCube.get()[LMM] and theCube.get()[LTR] == theCube.get()[LMM] and theCube.get()[LTM] == theCube.get()[LMM]:
        theCube.rotate('RRUbFRRfBURR')
        result += 'RRUbFRRfBURR'
        
    else:
        theCube.rotate('FFUrLFFlRUFF')
        result += 'FFUrLFFlRUFF'
    
    return result


