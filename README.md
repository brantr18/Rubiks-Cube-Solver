This is a microservice built with Flask that allows a user to input a Rubik's cube configuration as a 54 character string where every 9 characters is a "face". 

Once the app is launched, a local server runs on the port 8080.

An example input to the browser address line would be:

localhost:8080/rubik/solve?cube=ywwbbowywrrogrworobyyggbwyrgwrrooyygoryoywbbbrgbowggbg


"ywwbbowywrrogrworobyyggbwyrgwrrooyygoryoywbbbrgbowggbg" is the cube configuration.


The order of the string is important because the faces must be entered as follows:

"ywwbbowyw   rrogrworo   byyggbwyr   gwrrooyyg   oryoywbbb   rgbowggbg"
  front        right       back        left        top        bottom
  
  
 It does not matter which side is picked to be the front face, as long as the face that is considered "front" does not change. (for me, green is always front)
 
 
 Another thing to note when entering the faces colors is that the colors are entered in the same order on every face. 
 
 For example:
 
 Our front face "ywwbbowyw" is entered from the top left going right. Meaning "y" is top left of the front face, "w" is the top middle of the front face, "w' is the 
 top right, "b" is the left middle and so on.
 
 Here's a visual:
 
 y  w  w
 b  b  o   <--- front face
 w  y  w
 
 r  r  o
 g  r  w   <--- right face
 o  r  o
 
 and so on...
 
 
