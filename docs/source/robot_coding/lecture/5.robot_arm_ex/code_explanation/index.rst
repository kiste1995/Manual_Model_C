Code Explanation
==================

Robot arm Movements
--------------------

-   In order to instruct the robot arm, we must first initialize it as an object.

    .. code-block:: python

        # Register robot arm as an object
        Arm = Arm_Device()
        time.sleep(.1)
    
    As you may have noticed, we after the arm is initialized as an object, we pause our program 
    for one tenth of a second. We will regularly follow this protocol when we are giving the 
    robot arm multiple instructions at the same time. We do not want some of the instructions cutting
    in while other insturctional movements have not finished. 


Basic Movements
--------------------

-   For basic movements, we use ``Arm_serial_servo_write(servo_id, angle, time)`` function. The function can accept 3 parameters
    from the user.

    1. servo_id: The servo_id represents the motors responsible for the robot arm movements. There are total of 6 robots, from the bottom most motor responsbile for rotational movement and to the last motor which is responsible for the pincher
    2. angle: The angle determines how much the motor should move from its current position. 
    3. time: The time in which the movement is to be conducted. (in 1/2 mili seconds)

    .. code-block:: python

        Arm = Arm_Device()
        # Move the 6th servo (which is the pincher) to 90 degree angle for 2 second. 
        Arm.Arm_serial_servo_write(6, 90, 1000)
        time.sleep(.1)
    
-   You may also move multiple servo's at the same time using ``Arm_seria_servo_write6(...params)``` function.
    The function recieves angle information for all the servor and the required time for movement completion. 

    .. code-block:: python

        # Move all the servo's 90 degrees for 2 second
        Arm.Arm_serial_servo_write6(90, 90, 90, 90, 90, 90, 1000)

    You may give the same instructions in a list format using ``Arm_seria_servo_write6_array(array, time)`` function. 

Reading the Current Angle of the Servo
----------------------------------------

-   All the servos at any given moment are rotated to a specific angle. 
    In order to determine the current angle of the motors, we may run ``Arm_serial_servo_read(servo_id)``` function.

    -   By specifying the desired servo number, we may get the current angle information of the specified servo. 
    
    .. code-block:: python

        servo_angle = Arm.Arm_serial_servo_read(servo_id)


Teaching the Robot Arm
----------------------------------------

-   Since manually instructing angle information for each of the servo for every movement is difficult, you may 
    teach you robot arm moves. 
    
    -   By default, the servos are in locked position. The function that is responsible for locking and unlocking the robot arm is ``Arm_Button_Mode(mode)`` function

        The function recieves 1 input *mode* from the user. The mode must be an binary integer of either 1 and 0.
        
        1.  ``mode=0``: All servos are locked (default)
        2.  ``mode=1``: All servos are released 

    -   To learn a movement, ``Arm_Action_Study()`` function is used. To study a movement, simply activate the function and move the arm
        If you wish to have multiple movements, after completing one movement, activate the function again and repeat the process. 
        *(NOTE!)* The after activating the function, only the first movement of the robot is registered. If it is a chain movement, please activate the function at the start of each movement. 
        After finishing the movement put the robot arm back to the locked mode. ``Arm_Button_Mode(0)``

    -   To see the number of learned movements, run ``Arm_Read_Action_Num()`` function which will return the total learned movements.
    -   To execute the learned movements, run ``Arm_Action_Mode(mode)`` function. This function will sequentially run all the learned movements from the first to last. 
        We can have 3 different execution mode: 

        1.  ``mode = 1``: Execute all the sequence only once.
        2.  ``mode = 2``: Execute all the sequence repeatedly.
        3.  ``mode = 3``: Stop the sequence. 

    -   To clear all the previously learned movements, run ``Arm_Clear_Action()`` function. 


Tacking a Color or a Face
----------------------------------------

-   For tracking tasks, we provide custom library (for color tracking ``color_folow.py`` and ``PID.py``, for face tracking ``dofbot_conf.py``, ``face_follow.py``, ``PID.py``)


Tracking a Color
^^^^^^^^^^^^^^^^^

-   Here are all the libraries used for tracking a color task. 

    -   *cv2*: Computer Vision library
    -   *threading*: Threading library for multi, singular processing.
    -   *random*: Library for generating and controlling random instances.
    -   *time*: Library for time related modules. 
    -   *ipywidgets*: Widget library used to create graphical user interfaces with IPython display.
    -   *IPython.display*: Library with modules that allow for graphical output within jupyter environment
    -   *color_follow*: Custom library with modules that allow for robot arm to follow the color. 

-   Initialization
 

    1.   Create the follow instance for the color_follow modules.
    2.   Initialize model variable with 'General'. Later on it will be changed to whether you wish to learn a new color, learn to track or simply to exit the tracking process.
    3.   Initialize HSV_learning. Later on it will house the learned movement modules. 
    4.   color_hsv: Initialize what red, green, blue, and yellow collow would be (in a spectrum)
    5.   color: Initialize the first color to be random. 

    .. code-block:: python 

        follow = color_follow()
        model = 'General'
        HSV_learning = ()
        color_hsv = {"red": ((0, 25, 90), (10, 255, 255)),
                    "green": ((53, 36, 40), (80, 255, 255)),
                    "blue": ((110, 80, 90), (120, 255, 255)),
                    "yellow": ((25, 20, 55), (50, 255, 255))}

        color = [[random.randint(0, 255) for _ in range(3)] for _ in range(255)]
    
-   Create the widgets for the user, and create a switch variables to change the model. 

    1. Whether to follow the specied color.
    2. Whether to learn a new color.
    3. Whether to learn to follow.
    4. Whether to be in a general mode.
    5. Whether to exit the task. 

-   Main process

    The main function built for our main process is camera function. Within the function:

    1. Initialize the camera input, and the framerate. 

        .. code-block:: python

            # Open camera
            capture = cv.VideoCapture(1)
            capture.set(3, 640)
            capture.set(4, 480)
            capture.set(5, 30)  #set frame

    2. Capture every frame from the camera on loop. Terminate the loop upon closure of the camera.

        .. code-block:: python
            
            while capture.isOpened():
               
        1. Import in the frame of the input feed and resize it to 640, 480 ratio. 

            .. code-block:: python

                _, img = capture.read()

                img = cv.resize(img, (640, 480))

        2. If the model is set to follow the color, activate follow_function and provide the function with the current frame and the color to follow.

            .. code-block:: python

                if model == 'color_follow':
                    img = follow.follow_function(img, color_hsv[choose_color.value])
                    cv.putText(img, choose_color.value, (int(img.shape[0] / 2), 50), cv.FONT_HERSHEY_SIMPLEX, 2, color[random.randint(0, 254)], 2)
            
        3. If the model is set to learn a new color, activate learn function.

            .. code-block:: python

                if model == 'learning_color':
                    img,HSV_learning = follow.get_hsv(img)

        4. If the model is set to learn to follow, activate the learn follow function.

            .. code-block:: python 

                if model == 'learning_follow' :
                    if len(HSV_learning)!=0:
                        print(HSV_learning)
                        img = follow.learning_follow(img, HSV_learning)

                        cv.putText(img,'LeColor', (240, 50), cv.FONT_HERSHEY_SIMPLEX, 1, color[random.randint(0, 254)], 1)
        
        5. If the model is set to exit, close all the windows opened and release the camera.

            .. code-block:: python 

                if model == 'Exit':
                    cv.destroyAllWindows()
                    capture.release()
                    break
    
    3. To activate the function above, first activate a display output, then within a thread run the function.

        .. code-block:: python

            display(controls_box,output)
            threading.Thread(target=camera, ).start()


Tracking a Face
^^^^^^^^^^^^^^^^

The steps taken for tracking a face is very similar to tracking a color. We use an cascading calssifier, an ensemble learning 
model based on the concatenation of several classifiers. We will be using a pretrained xml model named ``haarcascade_frontalface_default.xml``
with our OpenCV function. 

Our tracking model does not involve re-training with new data, hence, we do not need many different model options 
similar to the *Tracking a Color* task. 

-   Here are all the libraries used for tracking a color task. 

    -   *cv2*: Computer Vision library
    -   *threading*: Threading library for multi, singular processing.
    -   *time*: Library for time related modules. 
    -   *ipywidgets*: Widget library used to create graphical user interfaces with IPython display.
    -   *IPython.display*: Library with modules that allow for graphical output within jupyter environment
    -   *face_follow*: Custom library with modules that allow for robot arm to follow the face. 

-   First initialize the robot arm position as well as creating the instances for the face follow model and the mode for the model.

    .. code-block:: python

        import Arm_Lib
        Arm = Arm_Lib.Arm_Device()
        joints_0 = [90, 150, 20, 20, 90, 30]
        Arm.Arm_serial_servo_write6_array(joints_0, 1500)

        follow = face_follow()

        model = 'General'

-   Create the controls for the graphical user interface. Unlike the *Follow a Color* task, we do not need 
    many user interfaces, since there is no need to change color or learning a new color. 

    .. code-block:: python 

        button_layout = widgets.Layout(width='250px', height='50px', align_self='center')
        output = widgets.Output()

        exit_button = widgets.Button(description='Exit', button_style='danger', layout=button_layout)

        imgbox = widgets.Image(format='jpg', height=480, width=640, layout=widgets.Layout(align_self='center'))

        controls_box = widgets.VBox([imgbox, exit_button], layout=widgets.Layout(align_self='center'))
        # ['auto', 'flex-start', 'flex-end', 'center', 'baseline', 'stretch', 'inherit', 'initial', 'unset']
    
-   Create the controls for the exit widget.

    .. code-block:: python

        def exit_button_Callback(value):
            global model
            model = 'Exit'
        #     with output: print(model)
        exit_button.on_click(exit_button_Callback)
    
-   Main process:

    The main function built for our main process is camera function. Within the function:

    1. Initialize the camera input, and the framerate. 

        .. code-block:: python

            # Open camera
            capture = cv.VideoCapture(1)
            
    2. Capture every frame from the camera on loop. Terminate the loop upon closure of the camera.

        .. code-block:: python
            
            while capture.isOpened():
               
        1. Import in the frame of the input feed and resize it to 640, 480 ratio. 

            .. code-block:: python

                _, img = capture.read()

                img = cv.resize(img, (640, 480))

        2. Process the input frame with our follow_face model.

            .. code-block:: python

                img = follow.follow_function(img)
            
        
        3. If the model is set to exit, close all the windows opened and release the camera.

            .. code-block:: python 

                if model == 'Exit':
                    cv.destroyAllWindows()
                    capture.release()
                    break
    
    3. To activate the function above, first activate a display output, then within a thread run the function.

        .. code-block:: python

            display(controls_box,output)
            threading.Thread(target=camera, ).start()