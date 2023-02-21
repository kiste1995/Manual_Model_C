Discussion
=============

The robot control system allows us to communicate with the hardware of our robot.  

.. raw:: html

    <div style="background: #CFFDE1" class="admonition note custom">
        <p style="background: #68B984" class="admonition-title">
            Group Discussion Points
        </p>
        <ul>
            <li> If you could add another sensor to the robot what would that be?</li>
            <li>
                Why do you think we need the said sensor and where would it be used?
                <ul>
                    <li>For example, we added lidar sensors to have a functional navigational system. The lidar sensors provide 360 distnace sensor, providing a local 2D mapping for the robot.</li>
                    <li>For lidar sensor, we would add a Topic that would recieve the node connected to the output of the sensor and Publishes values to the Topic. We may use this information by Subscribing to the said Topic.</li>
                </ul>
            </li>
        </ul>
    </div>
