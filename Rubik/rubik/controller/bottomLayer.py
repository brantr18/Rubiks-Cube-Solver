from rubik.model.constants import *
from rubik.model.cube import Cube

def solveBottomLayer(theCube: Cube) -> str:
    '''
        This is the top-level function  for rotating
        a cube so that the bottom layer is solved.
        
        input:  an instance of the cube class with the down-face cross solved
        output: the rotations required to solve the bottom layer  
    '''  
    if _isBottomLayerSolved(theCube):
        return ''
    
    
    result = ''
    
    while not _isBottomLayerSolved(theCube):
        
        
        if _hasValidFaceTopCorner(theCube):
            result += _checkFacesUpperCorners(theCube)
            
        elif _hasValidTopFaceCorner(theCube) and not _hasDMMInTopLayer(theCube):
            result += _checkTopFaceCorners(theCube)
            
        else:
            
            if not _hasDMMInTopLayer(theCube) and not _hasDMMOnTopFace(theCube) and _hasValidFaceBottomCorner(theCube):
                
                result += _checkFacesBottomCorners(theCube)
            
            elif _isDownFaceSolved(theCube) and not _isBottomPerimSolved(theCube):
                
                result += _fixBottomPerim(theCube)
            
            else:
                theCube.rotate('U')
                result += 'U'
        
    
    optimizedResult = result.replace('UUU','u')
    
    return optimizedResult



def _checkFacesUpperCorners(theCube: Cube) -> str:
    
    result = ''
    
    if theCube.get()[FTL] == theCube.get()[FMM] and theCube.get()[LTR] == theCube.get()[DMM]:
        theCube.rotate('luL')
        result += 'luL'
    
    elif theCube.get()[FTR] == theCube.get()[FMM] and theCube.get()[RTL] == theCube.get()[DMM]:
        theCube.rotate('RUr')
        result += 'RUr'
        
    elif theCube.get()[RTL] == theCube.get()[RMM] and theCube.get()[FTR] == theCube.get()[DMM]:
        theCube.rotate('fuF')
        result += 'fuF'
        
    elif theCube.get()[RTR] == theCube.get()[RMM] and theCube.get()[BTL] == theCube.get()[DMM]:
        theCube.rotate('BUb')
        result += 'BUb'
        
    elif theCube.get()[BTL] == theCube.get()[BMM] and theCube.get()[RTR] == theCube.get()[DMM]:
        theCube.rotate('ruR')
        result += 'ruR'
        
    elif theCube.get()[BTR] == theCube.get()[BMM] and theCube.get()[LTL] == theCube.get()[DMM]:
        theCube.rotate('LUl')
        result += 'LUl'
    
    elif theCube.get()[LTL] == theCube.get()[LMM] and theCube.get()[BTR] == theCube.get()[DMM]:
        theCube.rotate('buB')
        result += 'buB'
        
    elif theCube.get()[LTR] == theCube.get()[LMM] and theCube.get()[FTL] == theCube.get()[DMM]:
        theCube.rotate('FUf')
        result += 'FUf'

    return result


def _checkTopFaceCorners(theCube: Cube) -> str:
    
    result = ''
    
    if theCube.get()[UBL] == theCube.get()[DMM]:
        theCube.rotate('luLluL')
        result += 'luLluL'
        
    elif theCube.get()[UBR] == theCube.get()[DMM]:
        theCube.rotate('RUrRUr')
        result += 'RUrRUr'
        
    elif theCube.get()[UTR] == theCube.get()[DMM]:
        theCube.rotate('ruRruR')
        result += 'ruRruR'
        
    elif theCube.get()[UTL] == theCube.get()[DMM]:
        theCube.rotate('LUlLUl')
        result += 'LUlLUl'

    return result


def _checkFacesBottomCorners(theCube: Cube) -> str:
    
    result = ''
    
    if theCube.get()[FBL] == theCube.get()[DMM]:
        theCube.rotate('luL')
        result += 'luL'
        
    elif theCube.get()[FBR] == theCube.get()[DMM]:
        theCube.rotate('RUr')
        result += 'RUr'
        
    elif theCube.get()[RBL] == theCube.get()[DMM]:
        theCube.rotate('fuF')
        result += 'fuF'
        
    elif theCube.get()[RBR] == theCube.get()[DMM]:
        theCube.rotate('BUb')
        result += 'BUb'
        
    elif theCube.get()[BBL] == theCube.get()[DMM]:
        theCube.rotate('ruR')
        result += 'ruR'
        
    elif theCube.get()[BBR] == theCube.get()[DMM]:
        theCube.rotate('LUl')
        result += 'LUl'
        
    elif theCube.get()[LBL] == theCube.get()[DMM]:
        theCube.rotate('buB')
        result += 'buB'
        
    elif theCube.get()[LBR] == theCube.get()[DMM]:
        theCube.rotate('FUf')
        result += 'FUf'

    return result


def _hasValidFaceTopCorner(theCube: Cube) -> bool:
    if theCube.get()[FTL] == theCube.get()[FMM] and theCube.get()[LTR] == theCube.get()[DMM] or \
       theCube.get()[FTR] == theCube.get()[FMM] and theCube.get()[RTL] == theCube.get()[DMM] or \
       theCube.get()[RTL] == theCube.get()[RMM] and theCube.get()[FTR] == theCube.get()[DMM] or \
       theCube.get()[RTR] == theCube.get()[RMM] and theCube.get()[BTL] == theCube.get()[DMM] or \
       theCube.get()[BTL] == theCube.get()[BMM] and theCube.get()[RTR] == theCube.get()[DMM] or \
       theCube.get()[BTR] == theCube.get()[BMM] and theCube.get()[LTL] == theCube.get()[DMM] or \
       theCube.get()[LTL] == theCube.get()[LMM] and theCube.get()[BTR] == theCube.get()[DMM] or \
       theCube.get()[LTR] == theCube.get()[LMM] and theCube.get()[FTL] == theCube.get()[DMM]:
        return True
    return False


def _hasValidTopFaceCorner(theCube: Cube) -> bool:
    if theCube.get()[UBL] == theCube.get()[DMM] or \
       theCube.get()[UBR] == theCube.get()[DMM] or \
       theCube.get()[UTR] == theCube.get()[DMM] or \
       theCube.get()[UTL] == theCube.get()[DMM]:
        return True
    return False


def _hasValidFaceBottomCorner(theCube: Cube) -> bool:
    if theCube.get()[FBL] == theCube.get()[DMM] or \
       theCube.get()[FBR] == theCube.get()[DMM] or \
       theCube.get()[RBL] == theCube.get()[DMM] or \
       theCube.get()[RBR] == theCube.get()[DMM] or \
       theCube.get()[BBL] == theCube.get()[DMM] or \
       theCube.get()[BBR] == theCube.get()[DMM] or \
       theCube.get()[LBL] == theCube.get()[DMM] or \
       theCube.get()[LBR] == theCube.get()[DMM]:
        return True
    return False





def _hasDMMInTopLayer(theCube: Cube) -> bool:
    if theCube.get()[FTL] == theCube.get()[DMM] or \
       theCube.get()[FTR] == theCube.get()[DMM] or \
       theCube.get()[RTL] == theCube.get()[DMM] or \
       theCube.get()[RTR] == theCube.get()[DMM] or \
       theCube.get()[BTL] == theCube.get()[DMM] or \
       theCube.get()[BTR] == theCube.get()[DMM] or \
       theCube.get()[LTL] == theCube.get()[DMM] or \
       theCube.get()[LTR] == theCube.get()[DMM]:
        return True
    return False


def _hasDMMOnTopFace(theCube: Cube) -> bool:
    if theCube.get()[UBL] == theCube.get()[DMM] or \
       theCube.get()[UBR] == theCube.get()[DMM] or \
       theCube.get()[UTR] == theCube.get()[DMM] or \
       theCube.get()[UTL] == theCube.get()[DMM]:
        return True
    return False



def _isBottomLayerSolved(theCube: Cube) -> bool:
    if theCube.get()[FBL] == theCube.get()[FMM] and \
            theCube.get()[FBM] == theCube.get()[FMM] and \
            theCube.get()[FBR] == theCube.get()[FMM] and \
            theCube.get()[RBL] == theCube.get()[RMM] and \
            theCube.get()[RBM] == theCube.get()[RMM] and \
            theCube.get()[RBR] == theCube.get()[RMM] and \
            theCube.get()[BBL] == theCube.get()[BMM] and \
            theCube.get()[BBM] == theCube.get()[BMM] and \
            theCube.get()[BBR] == theCube.get()[BMM] and \
            theCube.get()[LBL] == theCube.get()[LMM] and \
            theCube.get()[LBM] == theCube.get()[LMM] and \
            theCube.get()[LBR] == theCube.get()[LMM] and \
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


def _isDownFaceSolved(theCube: Cube) -> bool:
    if theCube.get()[DTL] == theCube.get()[DMM] and \
       theCube.get()[DTM] == theCube.get()[DMM] and \
       theCube.get()[DTR] == theCube.get()[DMM] and \
       theCube.get()[DML] == theCube.get()[DMM] and \
       theCube.get()[DMR] == theCube.get()[DMM] and \
       theCube.get()[DBL] == theCube.get()[DMM] and \
       theCube.get()[DBM] == theCube.get()[DMM] and \
       theCube.get()[DBR] == theCube.get()[DMM]:
        return True
    return False


def _isBottomPerimSolved(theCube: Cube) -> bool:
    if theCube.get()[FBL] == theCube.get()[FMM] and \
       theCube.get()[FBM] == theCube.get()[FMM] and \
       theCube.get()[FBR] == theCube.get()[FMM] and \
       theCube.get()[RBL] == theCube.get()[RMM] and \
       theCube.get()[RBM] == theCube.get()[RMM] and \
       theCube.get()[RBR] == theCube.get()[RMM] and \
       theCube.get()[BBL] == theCube.get()[BMM] and \
       theCube.get()[BBM] == theCube.get()[BMM] and \
       theCube.get()[BBR] == theCube.get()[BMM] and \
       theCube.get()[LBL] == theCube.get()[LMM] and \
       theCube.get()[LBM] == theCube.get()[LMM] and \
       theCube.get()[LBR] == theCube.get()[LMM]:
        return True
    return False



def _fixBottomPerim(theCube: Cube) -> str:
    result = ''
    
    if theCube.get()[FBL] != theCube.get()[FMM]:
        theCube.rotate('luL')
        result += 'luL'
        
    elif theCube.get()[FBR] != theCube.get()[FMM]:
        theCube.rotate('RUr')
        result += 'RUr'
        
    elif theCube.get()[RBR] != theCube.get()[RMM]:
        theCube.rotate('BUb')
        result += 'BUb'
        
    elif theCube.get()[BBR] != theCube.get()[BMM]:
        theCube.rotate('LUl')
        result += 'LUl'
    
    return result


