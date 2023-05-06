from rubik.model.cube import Cube
from rubik.model.constants import *
from rubik.model.exceptions import CubeException

def rotate(parms):
    """Return rotated cube""" 
    result = {}
    
    for key in parms:
        
        if key not in VALID_ROTATE_KEYS:
            
            result['status'] = 'error: extraneous key detected'
            return result
    
    
    
    try:
        encodedCube = parms.get('cube')
        theCube = Cube(encodedCube)
        
    except CubeException:
        result['status'] = 'error: invalid cube'
        return result
        
    
    if parms.get('dir') != None:
        
        for direction in parms.get('dir'):
            if direction not in VALID_DIRS:
                result['status'] = 'error: invalid direction'
                return result
        
        directions = parms.get('dir')
        
    else:
        directions = 'F'
    
            
    theCube.rotate(directions)
    result['cube'] = theCube.get()
    result['status'] = 'ok'
    return result
    
    