LIDAR
=====

.. raw:: html
    
    <div style="background: #C3F8FF" class="admonition note custom">
        <p style="background: light-blue" class="admonition-title">
            Follow along: LIDAR Sensor Operation Example
        </p>
        <div class="line-block">
            <div class="line">The program launching process along with parameter settings are all simplified and set up on the Jupyter Notebook Environment.</div>
        </div>
        <ul>
            <li>Open the 01_04_scan.ipynb Jupyter Notebook</li>
            <li>Import the necessary python libraries and modules</li>
            <li>Follow and Execute the example codes</li>

        </ul>
        <div class="line">(The Jetson Board used for these examples are => Jetson Nano)</div>
        
    </div>


.. raw:: html

    <hr>

Open the following jupyter notebook:

- 03_04_scan.ipynb
- To run the cells within the notebook use *Ctrl + Enter*

.. thumbnail:: /_images/content_control/sensor5.png

|

Import the necessary python libraries and modules

.. code-block:: python

    import rospy
    from sensor_msgs.msg import LaserScan



-   Create zetabot Node
-   Subscribe to the "scan" topic, and display the published information. 

.. code-block:: python

    def process_scan(msg):
        rospy.loginfo("data: {}".format(msg))

    def start_node():
        rospy.init_node('zetabot')
        rospy.Subscriber("scan", LaserScan, process_scan)
        rospy.spin()

    try:
        start_node()
    except rospy.ROSInterruptException as err:
        print(err)



