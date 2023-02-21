Mission
=========

.. raw:: html

    <div style="background: #ffe5b4" class="admonition note custom">
        <p style="background: #ffbf00" class="admonition-title">
            Project Name: Applying Navigation System on our Zetabot
        </p>
        <ul>
            <li><strong>-</strong> This mission is a <strong>group project</strong>.</li>
            <li><strong>-</strong> Construct a map within your team.</li>
            <li><strong>-</strong> Navigate the contructed map with the Zetabot as a team.</li>
            <div>
        </ul>
    </div>

Constructing a Map (as a Team)
--------------------------------

For our navigation mission, we we hold a cooperative mission with other teams.

- For each team, 3 map panels will be given.
- As a team try to arrange the panels so that there is a clear starting and finishing zone. For example:

  .. thumbnail:: /_images/ai_training/arrangement.png


Mapping the Constructed Map
----------------------------------------------

Place the Zetabot on the starting location of the map. 


On each of the Zetabot screen, the following will be displayed:

.. thumbnail:: /_images/ai_training/slam_nav1.png

1. Select the Mapping button. 
   
   - This will start the mapping simulation. Using SLAM method, the robot will utilize its LIDAR sensors as well as multiple odometry sensors to map out its immediate surroundings. 
   - By using the controller, move the Zetabot around the constructed map to learn its surroundings.  
   - Once the entire map is learned and constructed virually, save the map by pressing the ``Save Map``
     
     .. thumbnail:: /_images/ai_training/slam_nav2.png

2. Exit the Mapping Program without saving. 
3. Exit the Mapping Menu 
   
   .. thumbnail:: /_images/ai_training/slam_nav3.png



Executing Navigation
---------------------

Place the Zetabot in the starting position. 

- Press the Navigation button in the main menu. This will start the RViz application, whereupon the navigation will be conducted. 
  
  .. thumbnail:: /_images/ai_training/slam_nav1.png

  |

- Press the ``2D Pose Estimation`` to align the starting position of the Robot. 
- Click on ``2D Nav Goal`` and click the desired location and drag the curser to set which direction the robot should face once it reaches the said location. 

  .. thumbnail:: /_images/ai_training/rviz_2D_goal.png


Team Competition
---------------------

- With other team members, construct a large map with starting and finishing position. Example:
  
  .. thumbnail:: /_images/ai_training/team_final.png

- Team by team, execute the navigation task with your Zetabot. 