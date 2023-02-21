Explanation
=============================================

Within our zetabot robot, we use Robot Operating System (ROS) to control and communicate with our robot. 


The ROS is a set of software libraries and tools that provides functions such as low-level device controls and many more. 
With our **Follow Along** example, we were able to see how Topic and Node modules interacted with one another. 

Topic 
-------

Topic/s are named buses over which nodes exchange messages [link]_. They provide a means for the unidirectional communication. 
This means, we may send (publish) procedue calls for our robot and recieve (subscribe) movement informations from our robot on the said topic.

The two nodes used with Topic within our **Follow Along** examples are:

- Publisher (talker node to send information)
- Subscriber (listener node to recieve information)

One important point is that every topics are strongly typed by the ROS message type. This means that the message type used during 
publishing must be the same type when subscribing to the topic. 

Nodes
-------

Node is an executable file wihtin a ROS package. These nodes use ROS client library to communicate with one another. 
They can publish a message to a Topic or subscribe to a Topic to process the published messages. 

The below picture shows the interactions between different Topics and Nodes present within our zetabot:

.. thumbnail:: /_images/ai_training/ros_topic_node.png

Publisher 
--------------

Publihser is a talker node that can broadcast a message to a Topic.

To Publish a message, initialize a distinct **Topic** (for example *"chatter"*) and generate a output stream object (Publisher object).

- We use Publisher module from the rospy library which recieves 3 parameters and initializes a publisher object.

  .. code-block:: python 

    pub_object = rospy.Publisher("topic name", Message_type, queue_size=10)

  - Parameters:

    - **topic name**: Name your topic so that you may publish or subscribe on the same name.
    - **Message_type**: What message type will be used for the communication. 
    - **queue_size**: How many published messages will be in queue for the Subscriber to recieve them. 

Below is the example used for our **Follow Along** guide. The topic was named *chatter*, the message type was Python String, and the queue size was 10 (meaning there will be 10 published messages in queue if the subscriber is not fast enough to catch every published message).

.. code-block:: python 

    pub = rospy.Publisher('chatter', String, queue_size=10)\
    


After the initialization of the "Topic" and the publisher, create the talker node to Publish the messages.

.. code-block:: python 

    rospy.init_node('talker', anonymous=True)

The node was created using a ``rospy.init_node`` function, which initializes a node with the specified name and a setting.
We initialize our talker node with anonymous setting set to True. This is so that we may have multiple different nodes at the same time. 

|

To publish a string with the initialized Topic and the talker, use publish function within the Publish object. If there are no Subscriber present during the publishing of the message, the message will go into the queue within the Topic. 

.. code-block:: python 

    string_message = "I am the message being published"
    pub.publish(string_message)


Subscriber
---------------------

Subscriber is a listener node, that can recieve published messages from a Topic. 

- For us to initialize a Subscriber we need to have a Topic name, the type of the message being recieved and function responsbile for handling the message (callback function). 
  Unlike in the initialization process of the Publisher, we do not need to create an object for our Subscriber. 

  .. code-block:: python 
    
    rospy.Subscriber("topic name", Message_type, callback_function)

  - Parameters

    - **topic name**: The Topic name used for Publishing the message.
    - **Message_type**: The message type used when publishing. 
    - **callback_function**: The function used for the handling the published message. 

- Similar to the Publisher, we need to create listener node for the message to be recieved. And since we wish to constantly listen to the message that are being published, we can set the listener function to loop indefinetly. 

  - Example:

    .. code-block:: python 

        def listener():
            rospy.init_node('listener', anonymous=True)
            rospy.Subscriber("chatter", String, callback)
            rospy.spin()

- Creating the **callback_function()**

  - The Subscriber function sends data object to the callback function which contains the published messeges. The object contains data variable which contains the message (``data_object.data``).

  .. code-block:: python 

    def callback(data):
        rospy.loginfo(rospy.get_caller_id() + " Publisher is sending this => %s", data.data)






.. [link] `<http://wiki.ros.org/Topics>`_