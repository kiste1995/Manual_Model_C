Explanation
=============

With our **Follow Along** examples we are able to subscribe and listen to two of the 
sensors attached to our robot. 

- IMU (inertial measurement unit sensor)
- LIDAR (light detecting and ranging sensor)


IMU
-----

Inertial Measurement Unit sensor (IMU) are electronic device that measures and reports
the host's specific force, angular rate, linear velocity, position relative to the 
global reference frame and so on. 
This allows for us to detect changes in position within our robot, calculate positional
information relative to a global reference and so on. 

With our examples, we displayed the current measurments in x, y, z, w read on the 
Topic using our subscriber node. 

The data type used to store the x, y, z, w values are from sensor_msgs.msg library (IMU module). 

- Callback function

  - The example create ``process_imu(msg)`` callback function which displays the read sensor data as a loginfo.

    .. code-block:: python 

        def process_imu(msg):
            rospy.loginfo("x: {},y: {},z: {},w: {}".format(msg.orientation.x, msg.orientation.y, msg.orientation.z, msg.orientation.w))
    
- Subscriber

  .. code-block:: python 

    def start_node():
        rospy.init_node('zetabot')
        rospy.Subscriber("imu", Imu, process_imu)
        rospy.spin()

    try:
        start_node()
    except rospy.ROSInterruptException as err:
        print(err)



LIDAR
---------

Light Detecting and Ranging Sensor (LIDAR) sensors are one of the key components when it comes to self driving robots. 
It uses eye-safe laser beams to locate and draw the surrounding terrain/environment. 

The LIDAR attached onto our zetabot creates a 2 dimensional environmental image. This
can be used in applications such as self navigation, self driving and other various
tasks. 

The process of reading the data from the sensor is the same as IMU sensor. 
The only differences are the message type and the topic name. Unlike IMU Topic, the LIDAR topic publishes
messages with LaserScan module from sensor_msgs.msg library. And the topic onto which
the sensor data are published is called **"scan"**

- Callback function

  - The example create ``process_scan(msg)`` callback function which displays the sensor data as a loginfo.

    .. code-block:: python 

        def process_scan(msg):
            rospy.loginfo("data: {}".format(msg))
    
- Subscriber

  .. code-block:: python 

    def start_node():
        rospy.init_node('zetabot')
        rospy.Subscriber("scan", LaserScan, process_scan)
        rospy.spin()

    try:
        start_node()
    except rospy.ROSInterruptException as err:
        print(err)
