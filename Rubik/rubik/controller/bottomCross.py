from rubik.model.constants import *
from rubik.model.cube import Cube

def solveBottomCross(theCube: Cube) -> str:
    '''
        This is the top-level function  for rotating
        a cube into the down-face cross configuration.
        
        input:  an instance of the cube class
        output: the rotations required to transform the input cube into the down-face cross 
    ''' 
    if _bottomCrossSolved(theCube):
        return ''
    
    result = ''
    
    while _daisySolved(theCube) == False:
        
        if theCube.get()[UTM] != theCube.get()[DMM]:
    
            if _UTMHasValidPerimeter(theCube) == True:
    
                result += _UTMCheckPerimeter(theCube)
    
            else:
    
                result += _UTMCheckSides(theCube)
            
        if theCube.get()[UML] != theCube.get()[DMM]:
        
            if _UMLHasValidPerimeter(theCube) == True:
        
                result += _UMLCheckPerimeter(theCube)
        
            else:
        
                result += _UMLCheckSides(theCube)
        
        if theCube.get()[UBM] != theCube.get()[DMM]:
        
            if _UBMHasValidPerimeter(theCube) == True:
        
                result += _UBMCheckPerimeter(theCube)
        
            else:
        
                result += _UBMCheckSides(theCube)
        
        if theCube.get()[UMR] != theCube.get()[DMM]:
        
            if _UMRHasValidPerimeter(theCube) == True:
        
                result += _UMRCheckPerimeter(theCube)
        
            else:
        
                result += _UMRCheckSides(theCube)
    
    
    while _bottomCrossSolved(theCube) == False:
    
        result += _turnDaisyToBottomCross(theCube)
    
    return result





# --------------UTM Methods--------------------------
def _UTMCheckPerimeter(theCube: Cube) -> str:
    result = ''

    if theCube.get()[RMR] == theCube.get()[DMM]:
        theCube.rotate('B')
        result = 'B'
    
    elif theCube.get()[LML] == theCube.get()[DMM]:
        theCube.rotate('b')
        result = 'b'
    
    
    elif theCube.get()[DBM] == theCube.get()[DMM]:
        theCube.rotate('BB')
        result = 'BB'


    return result


def _UTMCheckSides(theCube: Cube) -> str:

    rotationDict = {
        BTM: 'BuLU',
        BML: 'Uru',
        BBM: 'buLU',
        BMR: 'uLU',
        RTM: 'RB',
        RML: 'RRB',
        RBM: 'rB',
        LTM: 'lb',
        LBM: 'Lb',
        LMR: 'LLb',
        FTM: 'FURu',
        FML: 'ulU',
        FBM: 'fURu',
        FMR: 'URu',
        DTM: 'FuuFUU',
        DML: 'lulU',
        DMR: 'RURu'
    }
    
    for color, rotationSequence in rotationDict.items():
        if theCube.get()[color] == theCube.get()[DMM]:
            theCube.rotate(rotationSequence)
            return rotationSequence

    return ''
    
    
    
    
# ---------------UML Methods-----------------------
    
def _UMLCheckPerimeter(theCube: Cube) -> str:
    result = ''

    if theCube.get()[BMR] == theCube.get()[DMM]:
        theCube.rotate('L')
        result = 'L'
    
    elif theCube.get()[FML] == theCube.get()[DMM]:
        theCube.rotate('l')
        result = 'l'
    
    
    elif theCube.get()[DML] == theCube.get()[DMM]:
        theCube.rotate('LL')
        result = 'LL'


    return result

    
def _UMLCheckSides(theCube: Cube) -> str:

    rotationDict = {
        LTM: 'LuFU',
        LML: 'Ubu',
        LBM: 'luFU',
        LMR: 'uFU',
        BTM: 'BL',
        BML: 'BBL',
        BBM: 'bL',
        FTM: 'fl',
        FBM: 'Fl',
        FMR: 'FFl',
        RTM: 'RUBu',
        RML: 'ufU',
        RBM: 'rUBu',
        RMR: 'UBu',
        DMR: 'RuuRUU',
        DTM: 'fufU',
        DBM: 'BUBu'
    }
    
    for color, rotationSequence in rotationDict.items():
        if theCube.get()[color] == theCube.get()[DMM]:
            theCube.rotate(rotationSequence)
            return rotationSequence

    return ''
    

    
    
# -------------UBM Methods--------------------------
def _UBMCheckPerimeter(theCube: Cube) -> str:
    result = ''

    if theCube.get()[LMR] == theCube.get()[DMM]:
        theCube.rotate('F')
        result = 'F'
    
    elif theCube.get()[RML] == theCube.get()[DMM]:
        theCube.rotate('f')
        result = 'f'
    
    
    elif theCube.get()[DTM] == theCube.get()[DMM]:
        theCube.rotate('FF')
        result = 'FF'


    return result
    
    
def _UBMCheckSides(theCube: Cube) -> str:
    
    rotationDict = {
        FTM: 'FuRU',
        FML: 'Ulu',
        FBM: 'fuRU',
        FMR: 'uRU',
        LTM: 'LF',
        LML: 'LLF',
        LBM: 'lF',
        RTM: 'rf',
        RBM: 'Rf',
        RMR: 'RRf',
        BTM: 'BULu',
        BML: 'urU',
        BBM: 'bULu',
        BMR: 'ULu',
        DBM: 'BuuBUU',
        DMR: 'rurU',
        DML: 'LULu'
    }
    
    for color, rotationSequence in rotationDict.items():
        if theCube.get()[color] == theCube.get()[DMM]:
            theCube.rotate(rotationSequence)
            return rotationSequence

    return ''

    
    
    
# --------------UMR Methods-------------------
def _UMRCheckPerimeter(theCube: Cube) -> str:
    result = ''

    if theCube.get()[FMR] == theCube.get()[DMM]:
        theCube.rotate('R')
        result = 'R'
    
    elif theCube.get()[BML] == theCube.get()[DMM]:
        theCube.rotate('r')
        result = 'r'
    
    
    elif theCube.get()[DMR] == theCube.get()[DMM]:
        theCube.rotate('RR')
        result = 'RR'


    return result
    
    
    
def _UMRCheckSides(theCube: Cube) -> str:

    rotationDict = {
        RTM: 'RuBU',
        RML: 'Ufu',
        RBM: 'ruBU',
        RMR: 'uBU',
        FTM: 'FR',
        FML: 'FFR',
        FBM: 'fR',
        BTM: 'br',
        BBM: 'Br',
        BMR: 'BBr',
        LTM: 'LUFu',
        LML: 'ubU',
        LBM: 'lUFu',
        LMR: 'UFu',
        DML: 'LuuLUU',
        DBM: 'bubU',
        DTM: 'FUFu'
    }
    
    for color, rotationSequence in rotationDict.items():
        if theCube.get()[color] == theCube.get()[DMM]:
            theCube.rotate(rotationSequence)
            return rotationSequence

    return ''
    
    
    
    
def _daisySolved(theCube: Cube) -> bool:
    if theCube.get()[UTM] == theCube.get()[DMM] and theCube.get()[UML] == theCube.get()[DMM] \
                                                and theCube.get()[UBM] == theCube.get()[DMM] \
                                                and theCube.get()[UMR] == theCube.get()[DMM]:
        return True
    return False

def _bottomCrossSolved(theCube: Cube) -> bool:
    if theCube.get()[DTM] == theCube.get()[DMM] and theCube.get()[DML] == theCube.get()[DMM] \
                                                and theCube.get()[DBM] == theCube.get()[DMM] \
                                                and theCube.get()[DMR] == theCube.get()[DMM] \
                                                and theCube.get()[FBM] == theCube.get()[FMM] \
                                                and theCube.get()[RBM] == theCube.get()[RMM] \
                                                and theCube.get()[LBM] == theCube.get()[LMM] \
                                                and theCube.get()[BBM] == theCube.get()[BMM]:
        return True
    return False

def _UTMHasValidPerimeter(theCube: Cube) -> bool:
    if theCube.get()[RMR] == theCube.get()[DMM] or theCube.get()[LML] == theCube.get()[DMM] \
                                                or theCube.get()[DBM] == theCube.get()[DMM]:
        return True
    return False

def _UMLHasValidPerimeter(theCube: Cube) -> bool:
    if theCube.get()[BMR] == theCube.get()[DMM] or theCube.get()[FML] == theCube.get()[DMM] \
                                                or theCube.get()[DML] == theCube.get()[DMM]:
        return True
    return False

def _UBMHasValidPerimeter(theCube: Cube) -> bool:
    if theCube.get()[LMR] == theCube.get()[DMM] or theCube.get()[RML] == theCube.get()[DMM] \
                                                or theCube.get()[DTM] == theCube.get()[DMM]:
        return True
    return False

def _UMRHasValidPerimeter(theCube: Cube) -> bool:
    if theCube.get()[FMR] == theCube.get()[DMM] or theCube.get()[BML] == theCube.get()[DMM] \
                                                or theCube.get()[DMR] == theCube.get()[DMM]:
        return True
    return False
    
    
def _turnDaisyToBottomCross(theCube: Cube) -> str:
    result = ''
    
    if theCube.get()[UTM] == theCube.get()[DMM] and theCube.get()[BTM] == theCube.get()[BMM]:
        theCube.rotate('BB')
        result += 'BB'
            
    elif theCube.get()[UML] == theCube.get()[DMM] and theCube.get()[LTM] == theCube.get()[LMM]:
        theCube.rotate('LL')
        result += 'LL'
        
    elif theCube.get()[UBM] == theCube.get()[DMM] and theCube.get()[FTM] == theCube.get()[FMM]:
        theCube.rotate('FF')
        result += 'FF'
            
    elif theCube.get()[UMR] == theCube.get()[DMM] and theCube.get()[RTM] == theCube.get()[RMM]:
        theCube.rotate('RR')
        result += 'RR'
            
    else:
        theCube.rotate('U')
        result += 'U'
            
    return result

