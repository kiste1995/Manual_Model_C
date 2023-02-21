Explanation
=============

With our **Follow Along** examples we were able to test out two other sensors we have 
on our Zetabot; Camera and Sonar. 

- Camera (Raspberry PI Camera)
- Sonar (Sonic Navigation and Ranging)


Camera
-----

The zetabot has 2 cameras. One in front of the bot (which is the main camera), and one at the tip of the hand. 
With our follow up example we are using the camera on the front of the bot. 

The camera is registered as a ``/main_camera/raw`` topic. We utilize the Publisher
and Subscriber nodes to access the raw output of the main camera. 

The raw camera output is then converted to rgb8 cv object, and then converted to an image.

- RGB8 to Jpeg function:
  
  .. code-block:: python

    def rgb8_to_jpeg(value, quality=75):
      return bytes(cv2.imencode('.jpg',value)[1].tostring())


- Callback function

  - Process Image

    .. code-block:: python 

        def process_image(msg):
          try:
            cv_img = bridge.imgmsg_to_cv2(msg, "bgr8")
          except CvBridgeError as e:
            print(e)
          else:
            image_widget.value = rgb8_to_jpeg(cv_img)
            rospy.sleep(0.25)

- Subscriber

  .. code-block:: python 

    def start_node():
        rospy.init_node('zetabot')
        rospy.Subscriber("/main_camera/raw", Image, process_image)
        rospy.spin()

    try:
        start_node()
    except rospy.ROSInterruptException as err:
        print(err) #Display camera assembly



SONAR
---------

Sonic Navigation and Randing (LIDAR) sensors are used to measure distance with sound propagation. 
This type of navigation (distance measurement) is usually used in underwater, as in submarine navigation.

Within the zetabot there are 4 sonar sensors attached to each of the sides (number may wary depending on the version of zetabot that you have purchased).

They work by sending sonic waves and measuring the time it takes for the sonic waves to travel back to the sensor to measure the distance of an object. 


- Callback function

  .. code-block:: python 

      def process_sonar(msg):
          rospy.loginfo("Front: {}, Right: {}, Back: {}, Left: {}".format(msg.data[0], msg.data[1], msg.data[2], msg.data[3]))
    
- Subscriber

  .. code-block:: python 

    def start_node():
      rospy.init_node('zetabot')
      rospy.Subscriber("sonar", Float32MultiArray, process_sonar)
      rospy.spin()

    try:
        start_node()
    except rospy.ROSInterruptException as err:
        print(err)
