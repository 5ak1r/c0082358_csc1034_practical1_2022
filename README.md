CSC1034: Practical 1
====================
Portfolio 1
===========

This package is built as part of the CSC1034: Portfolio-1.

Type `python walking_panda.py` to run the default version of the project.
This simply creates a stationary Panda in a grassy environment.
The camera spins around the environment.

Commands
--------
You can add the following commands at the end of the line above in order to alter the panda or environment.

`--no-rotate`
-------------
Use this command to prevent the camera from spinning. The panda will simply
appear to be in a walking animation without any movement on a stationary background.

`--scale=x`
-----------
Multiply the size of the panda by x. If you select a value for x that is less than 1,
the panda will decrease in size.

`--pose`
--------
Stop the panda from moving. The panda will remain stationary.

`--friends=x`
-------------
Change the number of pandas created. The value for x must be an integer.
The value for x will be the number of pandas created. They will 
be created in neat rows of length 4 pandas.

`--color`
---------
Randomise the color of the panda. The default color is black and white.

Example Use
-----------
`python walking_panda.py --no_rotate --friends=5 --color`

This will create 5 pandas that have randomised colors, in an environment where the
camera does not move.