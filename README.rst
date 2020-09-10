Draw me
-------

Author: 
#######
Gabri Botha

Date:
#####
14 August 2020


Purpose:
########
To draw stuff using python3 / Pillow / PyGame.

Low level application to allow drawing stuff to any available display.
Should be able to work without X-org / X11.

Thus this code should be able to:
*********************************
  - Determine what displays are available

  - Select available display if any are found

  - Initialize new display if none are found

  - If unable to initialize a display:

    - Switch to virtual display mode / framebuffer

    - Determine what virtual displays are available

    - Select available virtual display if any are found

    - Initialize new virtual framebuffer if none are found

    - if unable to find or create virtual display:

      - fail gracefully

      - Offer helpfull advise, e.g. apt install -y Xvfb

  - store reference to display as a handle

  - Offer a menu of options, e.g.:

    - Game

      - Instructions

      - New

      - Load

      - Options

        - Difficult

        - Keys

        - Back

      - Back

    - Screen Saver

      - Instructions

      - Start Random

      - List Screen Savers

      - Options

      - Back

    - Pixel Test

      - Instructions

      - Start

      - Back

    - Info

      - Display

      - System

      - Back

    - Options

      - Display

      - System

      - Back

    - Credits

      - Start

      - Back

    - Exit

      - Are you sure? (Y/n)

        - Y

        - N


