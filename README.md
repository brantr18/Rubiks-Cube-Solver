This is a microservice built with Flask that allows a user to input a Rubik's cube configuration as a 54 character string where every 9 characters is a "face". 

Once app.py is launched, a local server runs on the port 8080.

An example input to the browser address line would be:

localhost:8080/rubik/solve?cube=ywwbbowywrrogrworobyyggbwyrgwrrooyygoryoywbbbrgbowggbg


"ywwbbowywrrogrworobyyggbwyrgwrrooyygoryoywbbbrgbowggbg" is the cube configuration.


The order of the string is important because the faces must be entered as follows:

"ywwbbowyw &ensp;  rrogrworo &ensp;  byyggbwyr &ensp;  gwrrooyyg &ensp;  oryoywbbb &ensp;  rgbowggbg"

  &ensp;&ensp;&ensp;front &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;      right &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;      back &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;       left &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;       top &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;      bottom
  
  
 It does not matter which side is picked to be the front face, as long as the face that is considered "front" does not change. (for me, green is always front)
 
 
 Another thing to note when entering the faces colors is that the colors are entered in the same order on every face. 
 
 For example:
 
 Our front face "ywwbbowyw" is entered from the top left going right. Meaning "y" is top left of the front face, "w" is the top middle of the front face, "w' is the 
 top right, "b" is the left middle and so on.
 
 Here's a visual:
 
 front face:<br>
 y&emsp;w&emsp;w<br>
 b&emsp;b&emsp;o<br>
 w&emsp;y&emsp;w
 
 
 right face:<br>
 r&emsp;&nbsp;r&emsp;o<br>
 g&emsp;r&emsp;w<br>
 o&emsp;r&emsp;o
 
 and so on...
 
 
