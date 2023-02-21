Overall Explanation
====================

With our follow along examples, we were able to move our robot arm with precision as well as produce music with our 
integrated speaker within the zetabot. The instructional codes have been compile into a jupyter notebook for the 
ease of use. 
This section will explain the libraries used for the *follow along* section. 


Robot Arm Movements
---------------------

The instructions given to the robot arm are within Python 2 environment. We use ``Arm_Lib`` library
which contains all the necessary modules that we use to operate our robot arm. 
``Arm_Lib`` is a library provided by the Yahboom Robotics where our robot arm was made. 



Tracking a Color or a Face
------------------------------

Within our *follow along* examples, we follow a tracking examples, where our robot arm would track either track a color 
or track our face.
In order to achieve this we implore three important steps

1. Input processing
2. Processing and instructing the arm to move towards the detected a color or a face.
3. Displaying the results. 

The detection as well as imput/ output image processing was handled by ``cv2`` library from OpenCV.
The movement of the robot arm was handled by the custom made proportianal integral derivative controller 
as well as the ``Arm_Lib`` library. 




Sound 
-------------------------------

For our dancing robot demonstration, we published an array of integer to ROS Topic called ``/robot_sound``. 

The ``robot_sound`` topic recieves integer array of size 3: ``[slot1, slot2, slot3]``.

- **slot1**: Recieves binary integer (1, 0) dictating whether to play the sound (1) or stop the sound (0).
- **slot2**: File ID (ranges from 0 ~ 9).
- **slot3**: Directory ID. (set to 1)
