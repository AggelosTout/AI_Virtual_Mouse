#Import some dependances
import cv2
import mediapipe as mp
import pyautogui

#Open the camera
cap = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
screen_height , screen_width = pyautogui.size()
index_y = 0

#change the frame from the camera
while True:
    _, frame = cap.read()
    frame = cv2.flip(frame,1)
    frame_height, frame_width , _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x*frame_width)
                y = int(landmark.y*frame_height)
                #print(x,y)
                if id == 9:
                    cv2.circle(img=frame, center = (x,y), radius= 15, color=(0,255,64))
                    middle_mcp_x = (screen_width/frame_width*x)*2
                    middle_mcp_y = (screen_height/frame_height*y)-400
                    pyautogui.moveTo(middle_mcp_x,middle_mcp_y)
                if id == 8:
                    cv2.circle(img=frame, center = (x,y), radius= 15, color=(0,255,255))
                    index_x = screen_width/frame_width*x
                    index_y = screen_height/frame_height*y
                if id == 16:
                    ring_tip_x = screen_width/frame_width*x
                    ring_tip_y = screen_height/frame_height*y
                    if abs(thumb_y-ring_tip_y)<80:
                        pyautogui.screenshot()
                        print('Screenshot taken')
                        pyautogui.sleep(1)
                if id == 12:
                    cv2.circle(img=frame, center = (x,y), radius= 15, color=(0,78,235))
                    middle_tip_x = screen_width/frame_width*x
                    middle_tip_y = screen_height/frame_height*y
                    #Right click
                    if abs(middle_tip_y-thumb_y) < 80:
                        print('right click')
                        pyautogui.click(button = 'right')
                        pyautogui.sleep(1)
                if id == 4:
                    cv2.circle(img=frame, center = (x,y), radius= 15, color=(0,255,255))
                    thumb_x = screen_width/frame_width*x
                    thumb_y = screen_height/frame_height*y
                    #print(abs(index_y - thumb_y))
                    #left click
                    if abs(index_y - thumb_y) < 80:
                        print('click')
                        pyautogui.click()
                        pyautogui.dragTo(middle_mcp_x,middle_mcp_y, button= 'left')
                        #print('Click and drag')
                        pyautogui.sleep(1)
    cv2.imshow('AI Virtual Mouse', frame)
    cv2.waitKey(1)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()