# Projectile-Physics-Simulator
This is a Projectile Physics Simulator. It uses metres as a unit of measurement, using a pixel per metre ratio of 20, this is so that values like Gravity are consistent using real world metrics. Also using real time (dt) to calculate velocity etc.
# Controls
- A and D are used to control the initial velocity of the projectile
- Mousewheel is used to control the angle at which the projectile is thrown from the North Line of the projectile. 
- Left Click is used to place the projectile. 
- Right click is used to launch the projectile.
- R to reset.
# Features
- delta time dependent physics: this is to ensure it runs consistently on hardware from different devices, FPS capped at 60 to ensure smooth rendering.
- Angle and velocity based launches: throw the projectile based on an initial velocity and at an angle from the North Line of the projectile.
- Collision Landing: the projectile collides with the floor and walls, meaning it loses energy each bounce, which can be tweaked in the settings.
- Air Resistance: the projectile now behaves adjusting to air resistance, where the mass of the ball, the air density and drag coefficient can be changed in settings to tune it.
- Projectile bounciness: control the projectile bounciness (0-1) in settings, 1 meaning that it won't lose any energy. 
# Requirements
- python 3.x
- pygame
# Running
Please run main.py to make the game function.
# Showcase
!(./assets/Showcase.gif)
