from rubik.model.constants import *
from rubik.model.cube import Cube
from rubik.controller.bottomLayer import solveBottomLayer

def solveMiddleLayer(theCube: Cube) -> str:
    '''
        This is the top-level function  for rotating
        a cube so that the middle layer is solved.
        
        input:  an instance of the cube class with the bottom layer solved
        output: the rotations required to solve the middle layer  
    '''  
    
    if _isMiddleLayerSolved(theCube):
        return ''
    
    result = ''
    
    while not _isMiddleLayerSolved(theCube):
        
        if _hasValidTopLayerTopFaceCombo(theCube):
            
            if _middleMatches(theCube):
                
                result += _checkTopFaceSquareOfValidCombo(theCube)
                
            else:
                
                theCube.rotate('U')
                result += 'U'
                
        else:
            
            result += _checkForOffendingSquareInMiddleLayer(theCube)
            result += solveBottomLayer(theCube)
    
    
    optimizedResult = result.replace('UUU', 'u')
    
    return optimizedResult





def _isMiddleLayerSolved(theCube: Cube) -> bool:
    if theCube.get()[FBL] == theCube.get()[FMM] and \
       theCube.get()[FBM] == theCube.get()[FMM] and \
       theCube.get()[FBR] == theCube.get()[FMM] and \
       theCube.get()[FMR] == theCube.get()[FMM] and \
       theCube.get()[FML] == theCube.get()[FMM] and \
       theCube.get()[RBL] == theCube.get()[RMM] and \
       theCube.get()[RBM] == theCube.get()[RMM] and \
       theCube.get()[RBR] == theCube.get()[RMM] and \
       theCube.get()[RMR] == theCube.get()[RMM] and \
       theCube.get()[RML] == theCube.get()[RMM] and \
       theCube.get()[BBL] == theCube.get()[BMM] and \
       theCube.get()[BBM] == theCube.get()[BMM] and \
       theCube.get()[BBR] == theCube.get()[BMM] and \
       theCube.get()[BMR] == theCube.get()[BMM] and \
       theCube.get()[BML] == theCube.get()[BMM] and \
       theCube.get()[LBL] == theCube.get()[LMM] and \
       theCube.get()[LBM] == theCube.get()[LMM] and \
       theCube.get()[LBR] == theCube.get()[LMM] and \
       theCube.get()[LMR] == theCube.get()[LMM] and \
       theCube.get()[LML] == theCube.get()[LMM] and \
       theCube.get()[DTL] == theCube.get()[DMM] and \
       theCube.get()[DTM] == theCube.get()[DMM] and \
       theCube.get()[DTR] == theCube.get()[DMM] and \
       theCube.get()[DML] == theCube.get()[DMM] and \
       theCube.get()[DMR] == theCube.get()[DMM] and \
       theCube.get()[DBL] == theCube.get()[DMM] and \
       theCube.get()[DBM] == theCube.get()[DMM] and \
       theCube.get()[DBR] == theCube.get()[DMM]:
        return True
    return False
    

def _hasValidTopLayerTopFaceCombo(theCube: Cube) -> bool:
    if theCube.get()[FTM] != theCube.get()[UMM] and theCube.get()[UBM] != theCube.get()[UMM] or \
       theCube.get()[RTM] != theCube.get()[UMM] and theCube.get()[UMR] != theCube.get()[UMM] or \
       theCube.get()[BTM] != theCube.get()[UMM] and theCube.get()[UTM] != theCube.get()[UMM] or \
       theCube.get()[LTM] != theCube.get()[UMM] and theCube.get()[UML] != theCube.get()[UMM]:
        return True
    return False


def _middleMatches(theCube: Cube) -> bool:
    if theCube.get()[FTM] == theCube.get()[FMM] and theCube.get()[UBM] != theCube.get()[UMM] or \
       theCube.get()[RTM] == theCube.get()[RMM] and theCube.get()[UMR] != theCube.get()[UMM] or \
       theCube.get()[BTM] == theCube.get()[BMM] and theCube.get()[UTM] != theCube.get()[UMM] or \
       theCube.get()[LTM] == theCube.get()[LMM] and theCube.get()[UML] != theCube.get()[UMM]:
        return True
    return False


def _checkTopFaceSquareOfValidCombo(theCube: Cube) -> str:
    result = ''
    
    if theCube.get()[FTM] != theCube.get()[UMM] and theCube.get()[UBM] != theCube.get()[UMM] and theCube.get()[FTM] == theCube.get()[FMM]:
        
        result += _checkFTMTopFaceSquareSide(theCube)
    
    elif theCube.get()[RTM] != theCube.get()[UMM] and theCube.get()[UMR] != theCube.get()[UMM] and theCube.get()[RTM] == theCube.get()[RMM]:
        
        result += _checkRTMTopFaceSquareSide(theCube)
            
    elif theCube.get()[BTM] != theCube.get()[UMM] and theCube.get()[UTM] != theCube.get()[UMM] and theCube.get()[BTM] == theCube.get()[BMM]:
        
        result += _checkBTMTopFaceSquareSide(theCube)
            
    elif theCube.get()[LTM] != theCube.get()[UMM] and theCube.get()[UML] != theCube.get()[UMM] and theCube.get()[LTM] == theCube.get()[LMM]:
        
        result += _checkLTMTopFaceSquareSide(theCube)
    
    return result


def _checkFTMTopFaceSquareSide(theCube: Cube) -> str:
    result = ''
    
    if theCube.get()[UBM] == theCube.get()[RMM]:
        theCube.rotate('URUr')
        result += 'URUr'
        result += solveBottomLayer(theCube)
        
    elif theCube.get()[UBM] == theCube.get()[LMM]:
        theCube.rotate('uluL')
        result += 'uluL'
        result += solveBottomLayer(theCube)
        
    return result


def _checkRTMTopFaceSquareSide(theCube: Cube) -> str:
    result = ''
    
    if theCube.get()[UMR] == theCube.get()[BMM]:
        theCube.rotate('UBUb')
        result += 'UBUb'
        result += solveBottomLayer(theCube)
        
    elif theCube.get()[UMR] == theCube.get()[FMM]:
        theCube.rotate('ufuF')
        result += 'ufuF'
        result += solveBottomLayer(theCube)
        
    return result


def _checkBTMTopFaceSquareSide(theCube: Cube) -> str:
    result = ''
    
    if theCube.get()[UTM] == theCube.get()[LMM]:
        theCube.rotate('ULUl')
        result += 'ULUl'
        result += solveBottomLayer(theCube)
        
    elif theCube.get()[UTM] == theCube.get()[RMM]:
        theCube.rotate('uruR')
        result += 'uruR'
        result += solveBottomLayer(theCube)
    
    return result


def _checkLTMTopFaceSquareSide(theCube: Cube) -> str:
    result = ''
    
    if theCube.get()[UML] == theCube.get()[FMM]:
        theCube.rotate('UFUf')
        result += 'UFUf'
        result += solveBottomLayer(theCube)
        
    elif theCube.get()[UML] == theCube.get()[BMM]:
        theCube.rotate('ubuB')
        result += 'ubuB'
        result += solveBottomLayer(theCube)
    
    return result


def _checkForOffendingSquareInMiddleLayer(theCube: Cube) -> str:
    result = ''
    
    if theCube.get()[FML] != theCube.get()[FMM]:
        theCube.rotate('luL')
        result += 'luL'
        
    elif theCube.get()[FMR] != theCube.get()[FMM]:
        theCube.rotate('RUr')
        result += 'RUr'
        
    elif theCube.get()[RMR] != theCube.get()[RMM]:
        theCube.rotate('BUb')
        result += 'BUb'
        
    elif theCube.get()[BMR] != theCube.get()[BMM]:
        theCube.rotate('LUl')
        result += 'LUl'
    
    return result


