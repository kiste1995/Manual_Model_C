Configuration
==========================

Indoor air quality and sensor data Topic data display

--------------------------------------------------------------------------

**GUI execution screen when button is clicked**

.. thumbnail:: /_images/start_gui/configuration.png

.. raw:: html

    <div style="background: #D3D3D3" class="admonition note custom">
        <p style="background: #FFFAFA" class="admonition-title">
            Traj Loop Mode
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