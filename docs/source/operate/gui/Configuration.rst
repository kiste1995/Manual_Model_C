Configuration
==========================

--------------------------------------------------------------------------

**GUI execution screen when button is clicked**

.. thumbnail:: /_images/start_gui/configuration.png

--------------------------------------------------------------------------

.. raw:: html

    <div style="background: #D3D3D3" class="admonition note custom">
        <p style="background: #A9A9A9" class="admonition-title">
            Traj Loop Mode
        </p>
        <ul>
            <li>
                Repeated trajectory driving
                <ul>
                    <li>If checked after executing Navigate Trajectories, trajectory driving will be performed repeatedly.</li>
                    <li>If you want to stop repetitive driving, you can uncheck and rerun Navigate Trajectories.</li>
                </ul>
            </li>
        </ul>
    </div>

--------------------------------------------------------------------------

.. raw:: html

    <div style="background: #D3D3D3" class="admonition note custom">
        <p style="background: #A9A9A9" class="admonition-title">
            Auto Charging
        </p>
        <ul>
            <li>
                Automatic charging in low battery condition
                <ul>
                    <li>The battery may discharge while driving if charging is not possible due to special circumstances (obstacles in front of the charging station, power failure)</li>
                    <li>In the case of scheduling, since the distance between charging times is long, when the low battery state is reached, the driving can be stopped and the charging process can be performed.</li>
                </ul>
            </li>
        </ul>
    </div>

--------------------------------------------------------------------------

.. raw:: html

    <div style="background: #D3D3D3" class="admonition note custom">
        <p style="background: #A9A9A9" class="admonition-title">
            Auto Purifier
        </p>
        <ul>
            <li>
                Air purifier automatic operation
                <ul>
                    <li>Activates when harmful substances above the standard value are detected based on air information</li>
                </ul>
            </li>
        </ul>
    </div>

--------------------------------------------------------------------------

.. raw:: html

    <div style="background: #D3D3D3" class="admonition note custom">
        <p style="background: #A9A9A9" class="admonition-title">
            Use Sonar
        </p>
        <ul>
            <li>
                Ultrasonic sensor used for robot backwards
                <ul>
                    <li>There are frequent cases where the robot cannot move forward due to frontal and side obstacles.</li>
                    <li>Set to move away from obstacles after moving backward for a set period of time on the driving algorithm</li>
                    <li>Since the lidar of the robot cannot detect the rear, it is used to reverse to a distance where an object is not detected within a certain distance through the sonar sensor.</li>
                </ul>
            </li>
        </ul>
    </div>