.. _Sonar: 

Sonar
=====

- :ref:`Camera`
- :ref:`Sonar` <- you are here

.. raw:: html
    
    <div style="background: #C3F8FF" class="admonition note custom">
        <p style="background: light-blue" class="admonition-title">
            Follow along: Sonar Sensor Operation Example
        </p>
        <div class="line-block">
            <div class="line">The program launching process along with parameter settings are all simplified and set up on the Jupyter Notebook Environment.</div>
        </div>
        <ul>
            <li>Open the 02_sonar.ipynb Jupyter Notebook</li>
            <li>Import the necessary python libraries and modules</li>
            <li>Follow and Execute the example codes</li>

        </ul>
        <div class="line">(The Jetson Board used for these examples are => Jetson Nano)</div>
        
    </div>


.. raw:: html

    <hr>

Open the following jupyter notebook:

-   02_sonar.ipynb
-   To run the cells within the notebook use *Ctrl + Enter*

.. thumbnail:: /_images/content_control/sensor2.webp
.. thumbnail:: /_images/content_control/sensor3.webp


Import the necessary python libraries and modules

.. code-block:: python

    import rospy
    from std_msgs.msg import Float32MultiArray

-   Create zetabot Node
-   sonar Topic Subscribe
-   Check message in data array format

.. code-block:: python

    def process_sonar(msg):
        rospy.loginfo("data[0]: {},data[1]: {},data[2]: {},data[3]: {}".format(msg.data[0], msg.data[1], msg.data[2], msg.data[3]))

    def start_node():
        rospy.init_node('zetabot')
        rospy.Subscriber("sonar", Float32MultiArray, process_sonar)
        rospy.spin()

    try:
        start_node()
    except rospy.ROSInterruptException as err:
        print(err)



-   Create zetabot Node
-   sonar Topic Subscribe
-   Check the message according to the direction


.. code-block:: python

    def process_sonar(msg):
        rospy.loginfo("Front: {}, Right: {}, Back: {}, Left: {}".format(msg.data[0], msg.data[1], msg.data[2], msg.data[3]))

    def start_node():
        rospy.init_node('zetabot')
        rospy.Subscriber("sonar", Float32MultiArray, process_sonar)
        rospy.spin()

    try:
        start_node()
    except rospy.ROSInterruptException as err:
        print(err)



