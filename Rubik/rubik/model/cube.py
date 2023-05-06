from rubik.model.constants import *
from rubik.model.exceptions import CubeException

class Cube:
    '''
    Rubik's cube
    '''

    def __init__(self, encodedCube):
        self._cube = encodedCube
        self._validateCube()
     
     
    def _validateCube(self):
        
        if self._cube == None or '':
            
            raise CubeException()
            
        if self._has_9_of_each_6_unique_characters() == True:
            
            if self._has_unique_middle_of_each_face() == True:
                
                return self._cube
            
            else: 
                raise CubeException()
        
        else:
            raise CubeException()
            
            
            
    def get(self):
        return self._cube
    
    def rotate(self, directions):
          
        if directions == '':
            directions = 'F'
        
        for direction in directions:
            
            if direction == "F":
                self._rotate_F()
                
            elif direction == "f":
                self._rotate_f()
                
            elif direction == "R":
                self._rotate_R()
                
            elif direction == "r":
                self._rotate_r()
                
            elif direction == "B":
                self._rotate_B()
                
            elif direction == "b":
                self._rotate_b()
                
            elif direction == "L":
                self._rotate_L()
                
            elif direction == "l":
                self._rotate_l()
                
            elif direction == "U":
                self._rotate_U()
                
            elif direction == "u":
                self._rotate_u()
            
        return self._cube
        

    def _rotate_F(self):
        cubeList = list(self._cube)
        rotatedCubeList = cubeList[:]
        
        #rotate front face clockwise
        rotatedCubeList[FTR] = cubeList[FTL]
        rotatedCubeList[FMR] = cubeList[FTM]
        rotatedCubeList[FBR] = cubeList[FTR]
        rotatedCubeList[FTM] = cubeList[FML]
        rotatedCubeList[FMM] = cubeList[FMM]
        rotatedCubeList[FBM] = cubeList[FMR]
        rotatedCubeList[FTL] = cubeList[FBL]
        rotatedCubeList[FML] = cubeList[FBM]
        rotatedCubeList[FBL] = cubeList[FBR]
        
        #rotate up to right
        rotatedCubeList[RTL] = cubeList[UBL]
        rotatedCubeList[RML] = cubeList[UBM]
        rotatedCubeList[RBL] = cubeList[UBR]
        
        #rotate right to bottom
        rotatedCubeList[DTR] = cubeList[RTL]
        rotatedCubeList[DTM] = cubeList[RML]
        rotatedCubeList[DTL] = cubeList[RBL]
        
        #rotate bottom to left
        rotatedCubeList[LTR] = cubeList[DTL]
        rotatedCubeList[LMR] = cubeList[DTM]
        rotatedCubeList[LBR] = cubeList[DTR]
        
        #rotate left to top
        rotatedCubeList[UBR] = cubeList[LTR]
        rotatedCubeList[UBM] = cubeList[LMR]
        rotatedCubeList[UBL] = cubeList[LBR]
        self._cube = "".join(rotatedCubeList)

    def _rotate_f(self):
        cubeList = list(self._cube)
        rotatedCubeList = cubeList[:]
        
        #rotate front face counter-clockwise
        rotatedCubeList[FBL] = cubeList[FTL]
        rotatedCubeList[FML] = cubeList[FTM]
        rotatedCubeList[FTL] = cubeList[FTR]
        rotatedCubeList[FBM] = cubeList[FML]
        rotatedCubeList[FMM] = cubeList[FMM]
        rotatedCubeList[FTM] = cubeList[FMR]
        rotatedCubeList[FBR] = cubeList[FBL]
        rotatedCubeList[FMR] = cubeList[FBM]
        rotatedCubeList[FTR] = cubeList[FBR]
        
        #rotate up to left
        rotatedCubeList[LTR] = cubeList[UBR]
        rotatedCubeList[LMR] = cubeList[UBM]
        rotatedCubeList[LBR] = cubeList[UBL]
        
        #rotate left to bottom
        rotatedCubeList[DTL] = cubeList[LTR]
        rotatedCubeList[DTM] = cubeList[LMR]
        rotatedCubeList[DTR] = cubeList[LBR]
        
        #rotate bottom to right
        rotatedCubeList[RBL] = cubeList[DTL]
        rotatedCubeList[RML] = cubeList[DTM]
        rotatedCubeList[RTL] = cubeList[DTR]
        
        #rotate right to top
        rotatedCubeList[UBR] = cubeList[RBL]
        rotatedCubeList[UBM] = cubeList[RML]
        rotatedCubeList[UBL] = cubeList[RTL]
        self._cube = "".join(rotatedCubeList)

    def _rotate_R(self):
        cubeList = list(self._cube)
        rotatedCubeList = cubeList[:]
        
        #rotate right face clockwise
        rotatedCubeList[RTR] = cubeList[RTL]
        rotatedCubeList[RMR] = cubeList[RTM]
        rotatedCubeList[RBR] = cubeList[RTR]
        rotatedCubeList[RTM] = cubeList[RML]
        rotatedCubeList[RMM] = cubeList[RMM]
        rotatedCubeList[RBM] = cubeList[RMR]
        rotatedCubeList[RTL] = cubeList[RBL]
        rotatedCubeList[RML] = cubeList[RBM]
        rotatedCubeList[RBL] = cubeList[RBR]
        
        #rotate up to back
        rotatedCubeList[BTL] = cubeList[UBR]
        rotatedCubeList[BML] = cubeList[UMR]
        rotatedCubeList[BBL] = cubeList[UTR]
        
        #rotate back to bottom
        rotatedCubeList[DBR] = cubeList[BTL]
        rotatedCubeList[DMR] = cubeList[BML]
        rotatedCubeList[DTR] = cubeList[BBL]
        
        #rotate bottom to front
        rotatedCubeList[FBR] = cubeList[DBR]
        rotatedCubeList[FMR] = cubeList[DMR]
        rotatedCubeList[FTR] = cubeList[DTR]
        
        #rotate front to top
        rotatedCubeList[UBR] = cubeList[FBR]
        rotatedCubeList[UMR] = cubeList[FMR]
        rotatedCubeList[UTR] = cubeList[FTR]
        self._cube = "".join(rotatedCubeList)

    def _rotate_r(self):
        cubeList = list(self._cube)
        rotatedCubeList = cubeList[:]
        
        #rotate right face counter-clockwise
        rotatedCubeList[RBL] = cubeList[RTL]
        rotatedCubeList[RML] = cubeList[RTM]
        rotatedCubeList[RTL] = cubeList[RTR]
        rotatedCubeList[RBM] = cubeList[RML]
        rotatedCubeList[RMM] = cubeList[RMM]
        rotatedCubeList[RTM] = cubeList[RMR]
        rotatedCubeList[RBR] = cubeList[RBL]
        rotatedCubeList[RMR] = cubeList[RBM]
        rotatedCubeList[RTR] = cubeList[RBR]
        
        #rotate back to up
        rotatedCubeList[UTR] = cubeList[BBL]
        rotatedCubeList[UMR] = cubeList[BML]
        rotatedCubeList[UBR] = cubeList[BTL]
        
        #rotate bottom to back
        rotatedCubeList[BBL] = cubeList[DTR]
        rotatedCubeList[BML] = cubeList[DMR]
        rotatedCubeList[BTL] = cubeList[DBR]
        
        #rotate front to bottom
        rotatedCubeList[DTR] = cubeList[FTR]
        rotatedCubeList[DMR] = cubeList[FMR]
        rotatedCubeList[DBR] = cubeList[FBR]
        
        #rotate top to front
        rotatedCubeList[FTR] = cubeList[UTR]
        rotatedCubeList[FMR] = cubeList[UMR]
        rotatedCubeList[FBR] = cubeList[UBR]
        self._cube = "".join(rotatedCubeList)

    def _rotate_B(self):
        cubeList = list(self._cube)
        rotatedCubeList = cubeList[:]
        
        #rotate back face clockwise
        rotatedCubeList[BTR] = cubeList[BTL]
        rotatedCubeList[BMR] = cubeList[BTM]
        rotatedCubeList[BBR] = cubeList[BTR]
        rotatedCubeList[BTM] = cubeList[BML]
        rotatedCubeList[BMM] = cubeList[BMM]
        rotatedCubeList[BBM] = cubeList[BMR]
        rotatedCubeList[BTL] = cubeList[BBL]
        rotatedCubeList[BML] = cubeList[BBM]
        rotatedCubeList[BBL] = cubeList[BBR]
        
        #rotate up to left
        rotatedCubeList[LTL] = cubeList[UTR]
        rotatedCubeList[LML] = cubeList[UTM]
        rotatedCubeList[LBL] = cubeList[UTL]
        
        #rotate left to bottom
        rotatedCubeList[DBL] = cubeList[LTL]
        rotatedCubeList[DBM] = cubeList[LML]
        rotatedCubeList[DBR] = cubeList[LBL]
        
        #rotate bottom to right
        rotatedCubeList[RBR] = cubeList[DBL]
        rotatedCubeList[RMR] = cubeList[DBM]
        rotatedCubeList[RTR] = cubeList[DBR]
        
        #rotate right to top
        rotatedCubeList[UTR] = cubeList[RBR]
        rotatedCubeList[UTM] = cubeList[RMR]
        rotatedCubeList[UTL] = cubeList[RTR]
        self._cube = "".join(rotatedCubeList)

    def _rotate_b(self):
        cubeList = list(self._cube)
        rotatedCubeList = cubeList[:]
        
        #rotate back face counter-clockwise
        rotatedCubeList[BBL] = cubeList[BTL]
        rotatedCubeList[BML] = cubeList[BTM]
        rotatedCubeList[BTL] = cubeList[BTR]
        rotatedCubeList[BBM] = cubeList[BML]
        rotatedCubeList[BMM] = cubeList[BMM]
        rotatedCubeList[BTM] = cubeList[BMR]
        rotatedCubeList[BBR] = cubeList[BBL]
        rotatedCubeList[BMR] = cubeList[BBM]
        rotatedCubeList[BTR] = cubeList[BBR]
        
        #rotate up to right
        rotatedCubeList[RTR] = cubeList[UTL]
        rotatedCubeList[RMR] = cubeList[UTM]
        rotatedCubeList[RBR] = cubeList[UTR]
        
        #rotate right to bottom
        rotatedCubeList[DBR] = cubeList[RTR]
        rotatedCubeList[DBM] = cubeList[RMR]
        rotatedCubeList[DBL] = cubeList[RBR]
        
        #rotate bottom to left
        rotatedCubeList[LBL] = cubeList[DBR]
        rotatedCubeList[LML] = cubeList[DBM]
        rotatedCubeList[LTL] = cubeList[DBL]
        
        #rotate left to top
        rotatedCubeList[UTL] = cubeList[LBL]
        rotatedCubeList[UTM] = cubeList[LML]
        rotatedCubeList[UTR] = cubeList[LTL]
        self._cube = "".join(rotatedCubeList)

    def _rotate_L(self):
        cubeList = list(self._cube)
        rotatedCubeList = cubeList[:]
        
        #rotate left face clockwise
        rotatedCubeList[LTR] = cubeList[LTL]
        rotatedCubeList[LMR] = cubeList[LTM]
        rotatedCubeList[LBR] = cubeList[LTR]
        rotatedCubeList[LTM] = cubeList[LML]
        rotatedCubeList[LMM] = cubeList[LMM]
        rotatedCubeList[LBM] = cubeList[LMR]
        rotatedCubeList[LTL] = cubeList[LBL]
        rotatedCubeList[LML] = cubeList[LBM]
        rotatedCubeList[LBL] = cubeList[LBR]
        
        #rotate up to front
        rotatedCubeList[FTL] = cubeList[UTL]
        rotatedCubeList[FML] = cubeList[UML]
        rotatedCubeList[FBL] = cubeList[UBL]
        
        #rotate front to bottom
        rotatedCubeList[DTL] = cubeList[FTL]
        rotatedCubeList[DML] = cubeList[FML]
        rotatedCubeList[DBL] = cubeList[FBL]
        
        #rotate bottom to back
        rotatedCubeList[BBR] = cubeList[DTL]
        rotatedCubeList[BMR] = cubeList[DML]
        rotatedCubeList[BTR] = cubeList[DBL]
        
        #rotate back to top
        rotatedCubeList[UTL] = cubeList[BBR]
        rotatedCubeList[UML] = cubeList[BMR]
        rotatedCubeList[UBL] = cubeList[BTR]
        self._cube = "".join(rotatedCubeList)
        
    def _rotate_l(self):
        cubeList = list(self._cube)
        rotatedCubeList = cubeList[:]
        
        #rotate left face counter-clockwise
        rotatedCubeList[LBL] = cubeList[LTL]
        rotatedCubeList[LML] = cubeList[LTM]
        rotatedCubeList[LTL] = cubeList[LTR]
        rotatedCubeList[LBM] = cubeList[LML]
        rotatedCubeList[LMM] = cubeList[LMM]
        rotatedCubeList[LTM] = cubeList[LMR]
        rotatedCubeList[LBR] = cubeList[LBL]
        rotatedCubeList[LMR] = cubeList[LBM]
        rotatedCubeList[LTR] = cubeList[LBR]
        
        #rotate up to back
        rotatedCubeList[BTR] = cubeList[UBL]
        rotatedCubeList[BMR] = cubeList[UML]
        rotatedCubeList[BBR] = cubeList[UTL]
        
        #rotate front to top
        rotatedCubeList[UBL] = cubeList[FBL]
        rotatedCubeList[UML] = cubeList[FML]
        rotatedCubeList[UTL] = cubeList[FTL]
        
        #rotate bottom to front
        rotatedCubeList[FBL] = cubeList[DBL]
        rotatedCubeList[FML] = cubeList[DML]
        rotatedCubeList[FTL] = cubeList[DTL]
        
        #rotate back to bottom
        rotatedCubeList[DBL] = cubeList[BTR]
        rotatedCubeList[DML] = cubeList[BMR]
        rotatedCubeList[DTL] = cubeList[BBR]
        self._cube = "".join(rotatedCubeList)
        
    def _rotate_U(self):
        cubeList = list(self._cube)
        rotatedCubeList = cubeList[:]
        
        #rotate up face clockwise
        rotatedCubeList[UTR] = cubeList[UTL]
        rotatedCubeList[UMR] = cubeList[UTM]
        rotatedCubeList[UBR] = cubeList[UTR]
        rotatedCubeList[UTM] = cubeList[UML]
        rotatedCubeList[UMM] = cubeList[UMM]
        rotatedCubeList[UBM] = cubeList[UMR]
        rotatedCubeList[UTL] = cubeList[UBL]
        rotatedCubeList[UML] = cubeList[UBM]
        rotatedCubeList[UBL] = cubeList[UBR]
        
        #rotate left to back
        rotatedCubeList[BTR] = cubeList[LTR]
        rotatedCubeList[BTM] = cubeList[LTM]
        rotatedCubeList[BTL] = cubeList[LTL]
        
        #rotate back to right
        rotatedCubeList[RTR] = cubeList[BTR]
        rotatedCubeList[RTM] = cubeList[BTM]
        rotatedCubeList[RTL] = cubeList[BTL]
        
        #rotate right to front
        rotatedCubeList[FTR] = cubeList[RTR]
        rotatedCubeList[FTM] = cubeList[RTM]
        rotatedCubeList[FTL] = cubeList[RTL]
        
        #rotate front to left
        rotatedCubeList[LTR] = cubeList[FTR]
        rotatedCubeList[LTM] = cubeList[FTM]
        rotatedCubeList[LTL] = cubeList[FTL]
        self._cube = "".join(rotatedCubeList)

    def _rotate_u(self):
        cubeList = list(self._cube)
        rotatedCubeList = cubeList[:]
        
        #rotate up face counter-clockwise
        rotatedCubeList[UBL] = cubeList[UTL]
        rotatedCubeList[UML] = cubeList[UTM]
        rotatedCubeList[UTL] = cubeList[UTR]
        rotatedCubeList[UBM] = cubeList[UML]
        rotatedCubeList[UMM] = cubeList[UMM]
        rotatedCubeList[UTM] = cubeList[UMR]
        rotatedCubeList[UBR] = cubeList[UBL]
        rotatedCubeList[UMR] = cubeList[UBM]
        rotatedCubeList[UTR] = cubeList[UBR]
        
        #rotate left to front
        rotatedCubeList[FTL] = cubeList[LTL]
        rotatedCubeList[FTM] = cubeList[LTM]
        rotatedCubeList[FTR] = cubeList[LTR]
        
        #rotate front to right
        rotatedCubeList[RTL] = cubeList[FTL]
        rotatedCubeList[RTM] = cubeList[FTM]
        rotatedCubeList[RTR] = cubeList[FTR]
        
        #rotate right to back
        rotatedCubeList[BTL] = cubeList[RTL]
        rotatedCubeList[BTM] = cubeList[RTM]
        rotatedCubeList[BTR] = cubeList[RTR]
        
        #rotate back to left
        rotatedCubeList[LTL] = cubeList[BTL]
        rotatedCubeList[LTM] = cubeList[BTM]
        rotatedCubeList[LTR] = cubeList[BTR]
        self._cube = "".join(rotatedCubeList)
        


    # Checks each unique character in the string, then checks the amount of each.
    # Also checks to make sure the characters in the string are within [A-Z, a-z, 0-9] only.
    # Will always yield a string with 54 characters.
    def _has_9_of_each_6_unique_characters(self):
    
        uniqueChars = set(self._cube)
        
        if len(uniqueChars) != NUM_OF_UNIQUE_CHARS:
            return False
        
        for char in uniqueChars:
        
            if not (char.isupper() or char.islower() or char.isdigit()):
                return False
        
            if self._cube.count(char) != NUM_OF_EACH_UNIQUE_CHAR:
                return False
        
        return True


    # Checks each face of the cube for a unique middle color
    def _has_unique_middle_of_each_face(self):
    
        seen = set()
    
        for char in [FMM, RMM, BMM, LMM, UMM, DMM]:
        
            if self._cube[char] in seen:
                return False
        
            seen.add(self._cube[char])
        
        return True
        