# AI_Virtual_Mouse

## In this repository you will find a fully functional example on how to create an AI Virtual Mouse with python.

This project consist of a sample code which shows how to do the following:

* Open the webcam with OpenCV (on a laptop)
* Detect some specific landmarks and gestures on the users hand with Mediapipe
* Translate the movements of the user's hand into actual working commands on your computer with PyAutoGUI 

## The dependances you will need:

* OpenCV

* Mediapipe

* PyAutoGUI

## How to use the AI Virtual Mouse

This code can be used in any type of computer (Desktop or laptop) by downloading the given code and open it with a code editor of your choice.

## Opereting Principle

This project uses only your computer camera and none further equipment is needed. Once the camera is open, Mediapipe will detect the landmarks on user's hand and depect them on the frame. More specifically the cursor will be landmark number 9 (as it is more stable). In order to click the mouse, simply tap your index finger and your thumb (landmarks 8 & 4). In case you need to right-click, tap your middle finger and your thumb (landmarks 12 & 4). You can see the landmarks from the following picture:   


- ![Mediapipe](https://mediapipe.dev/images/mobile/hand_landmarks.png)

The AI Virtual Mouse has also a screenshot function by tapping your ring-finger and your thumb (landmarks 4 & 16). Furthermore a "Click and drag" function is provided every time the user "hold" the index finger and thumb together.


## Recommended instructions for use
It is recommended to use the Virtual Mouse from a distance around 40-50 cm from your webcam and always keep in mind your hands should be in the frame in order for it to work properly.
