Explanation
=============================================

Within our zetabot robot, we use Robot Operating System (ROS) to control and communicate with our robot. 


If we looked at what Topic and Node was within ROS and how to publish and subscribe to the said topic with nodes, 
we will look at general ROS command lines, as well as service server and client interactions. 


ROS Command Line  
------------------

1. ``rosnode`` command line tool
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The ``rosnode`` is a command line that allows informations about the ROS Nodes to be displayed. There are few supported commands for the tool:

- ``rosnode info``: prints information about a node. For example:
  - ``rosnode info /node_name`` would display information about a node, including **publication** and **subscription**.
- ``rosnode kill``: kill a running node. Please be aware that nodes that are set to *respawn* will fail to die, or reappear.
  - Killing one or more nodes by their name:
    
    .. code-block:: bash

      $ rosnode kill rosout add_two_ints_server add_threeints_server ...
  
  - Killing nodes by user input (interactive mode):

    .. code-block:: bash

      $ rosnode kill 
      1. /rosout
      
      Please enter the number of the node you wish to kill.
      > 

  - Kill all nodes:
    
    ``kill -a, kill --all``

- ``rosnode list``: list active nodes
  - To display the current node list:

    .. code-block:: bash

      $ rosnode list
  
  - To display all the current list inside a /namespace_topic:
    
    .. code-block:: bash

      $ rosnode list /example_topic_name

  - To display XML -RPC URIs of current nodes:
  
    .. code-block:: bash

      $ rosnode list -u
  
  - To display the name and XML -RPC URIs of all the current nodes (either ``-a`` or ``--all``):
  
    .. code-block:: bash

      $ rosnode list -a

  
- ``rosnode machine``: list nodes runnning on a particular machine or list machines. For example, to see the nodes running on zetabot:
  
  .. code-block:: bash

    $ rosnode machine zetabot.local
    /talker-zetabot.local-72266-1257921234733
    /rosout
    /listener-zetabot.local-72615-1257921238320

- ``rosnode The rostopic command-line tool displays information about ROS topics. Currently, it can display a list of active topics, the publishers and subscribers of a specific topic, the publishing rate of a topic, the bandwidth of a topic, and messages published to a topic. The display of messages is configurable to output in a plotting-friendly format.ping``: test connectivity to a node by pinging them repeatedly. 
  - You may ping the nodes either individually or in total by specifying a node name ``rosnode ping /node_name`` or ping all the nodes by ``rosnode ping --all``
  - You may also ping an individual node Count number of times. 
    
    .. code-block:: bash

      $ rosnode ping -c 4 rosout
      rosnode: node is [/rosnode]
      pinging /rosout with a timeout of 3.0s
      xmlrpc reply from http://ann:46635/     time=1.195908ms
      xmlrpc reply from http://ann:46635/     time=1.123905ms
      xmlrpc reply from http://ann:46635/     time=1.144886ms
      xmlrpc reply from http://ann:46635/     time=1.137018ms
      ping average: 1.150429ms

- ``rosnode clearnup``: purge registration information of unreachable nodes. This function was added as a cosmetic solution for the ros node display and 
  should not be used for functional means. This is because it may terminate functioning nodes simply due to a delay.



2. ``rostopic`` command line tool
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


The rostopic command-line tool displays information about ROS topics. Currently, it can display a list of active topics, the publishers and subscribers of a specific topic, the publishing rate of a topic, the bandwidth of a topic, and messages published to a topic. The display of messages is configurable to output in a plotting-friendly format.

- ``rostopic list`` displays all current topics. 
  - To recieve information on a specific topic, use the ``rostopic list /topic_name`` command. This is equivalent to ``rostopic info `` command. 
  - If you wish to save the topic lists in a bag file, add ``-b`` argument.
  - If you wish to only list the publishers of the said topic, add ``-p`` argument. 
  - If you wish to only list the subscribers of the said topic, add  ``-s`` argument. 
  - You may also control the display output, by adding ``-v`` verbose argument. 

- ``rostopic echo`` displays the messages sent to a topic. 
  - In order to specify which topic, add the topic name after the command line: 
    
    .. code-block:: bash

      $ rostopic echo /imu
  
3. ``pm2`` command line tool
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``pm2`` is a deamon process manager that helps the management of application and nodes within the system. For our application we can type

.. code-block:: bash

  $ pm2 list


ROS Service
----------------


As we learned, the publish / subscribe model is a very flexible communication paradigm but it does not allow request / reply based interactions. 
Big example for this is sensors that has to recieve and send feedback inforamtions, rather than publishing every sensed information. We can implement
request / reply based communication system with *Service* which is defined by a pair of messages; one for the request and one for the reply. 

A providing ROS node offers a service under a string name, and a client calls the service by sending the request message and awaiting the reply. 

As mentioned earlier the ROS Services are defined by srv (simplified service description language) files. With the usage of rospy (python library),
we can convert the srv files into Python source code, and create three classes necessary for ROS Services:

1. Service Definition. Ex: (my_package/srv/Foo.srv -> my_package.srv.Foo)
   
   Within a python file, the Service is defined as a container for the request and response type. It must be used whenever one creates or calls a service

   .. code-block:: python 

    add_two_ints = rospy.ServiceProxy('service_name', my_package.srv.Foo)

2. Request Messages. Ex: (my_package/srv/Foo.srv -> my_package.srv.FooRequest)
   
   The resuest message is used to call the appropriate service. 


3. Response Messages. Ex: (my_package/srv/Foo.srv -> my_package.srv.FooResponse)

   The response message is used to contain the return value from the appropriate service. Hecne the Service handlers must return response messages instances of the correct type. 
  

2. Service proxies
^^^^^^^^^^^^^^^^^^^^^^^^

In most cases, you wish to set up a ``rospy.wait_for_service('service_name', timeout=None)`` to block until a service is available. 

In order to use a Service, we need to create a ``rospy.ServiceProxy(name, service_class, persistent=False, headers=None)`` with the name of the service one wishes to call. The Service may return an error
in which case, we need to have a exception handler. 

.. code-block:: python 

  rospy.wait_for_service('add_two_ints')
  try:
      add_two_ints = rospy.ServiceProxy('add_two_ints', AddTwoInts)
      resp1 = add_two_ints(x, y)
      return resp1.sum
  except rospy.ServiceException as e:
      print("Service call failed: %s"%e)

3. Calling services
^^^^^^^^^^^^^^^^^^^^^^^^

The ``rospy.ServiceProxy`` instances are callable. Within the python environment, you may call upon these instances similar to how a methos is called.

.. code-block:: python

  add_two_ints = rospy.ServiceProxy('add_two_ints', AddTwoInts)
  add_two_ints(1, 2)

There are total of three ways to pass an argument to the ServiceProxy instance.

1. Explicit style:
   
   The explicit style allows you to crewate your won * Request instance and pass it to publish. e.g:

   .. code-block:: python 

    request = rospy_tutorials.srv.AddTwoIntsRequest(1, 2)
    response = add_two_ints(request)

2. Implicit style with in-order arguments:
   
   In the in-order style, a new Message instance will be created with the arguments provided, in order. With this style, all of the fields must be provided. 

   .. code-block:: python 

    resp = add_two_ints(1, 2)

3. Implicit style with keyword arguments:

   In the keyword style, you can only initialize the fields you wish to put into as a Message. 

   .. code-block:: python 

    resp = add_two_ints(a = 1)

   The above code will set the a as 1 and b as the default value (for our case it is 0)

4. Providing Services
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In rospy, the rospy.Service instance with a callback to invoke when new requests are recieved is created to provide Service. Each inbound request is handled in its own thread,
so services must be **thread-safe**.

``rospy.Service(name, service_class, handler, buff_size=65536)``

- Create a new ROS Service with 
  - Specified name
  - Service type
  - Handler

    The handler is invoked with the service request and should invoke appropriate service response message. 

    .. code-block:: python 

      def add_two_ints(req):
        return rospy_tutorials.srv.AddTowIntsResponse(req.a + req.b)

      def add_two_ints_server():
        rospy.init_node('add_two_ints_server')
        s = rospy.Service('add_two_ints', rospy_tutorials.srv.AddTwoInts, add_two_ints)
        rospy.spin()

    The handler return type may be:

    - None(failure)
    - ServiceResponse
    - tuple or list
    - dict
    - singe-arugment responses only: value of fields.