steps - 
1. connect to the mocap wifi network. SSID/password will be emailed.
2. clone the repo https://github.com/AlonGil-Ad/simple_mocap
3. make sure you know the NAME or ID of your "asssets" (rigid bodies)
4. make sure the asset/s are in the tracked area (cameras) 
5. open  example.py, update your computer IP , and asset number/s and run
6. first 3 numbers are xyz in meters. notice the axes are Y-UP NOT Z-UP. there is a blue L on the floor to indicate X,Y,Z=0,0,0
7. second array of 4 numbers - the angles given in Quaternions , you can use any python library to convert to roll,pitch,yaw


