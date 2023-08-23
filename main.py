import cv2
import winsound

cam = cv2.VideoCapture(0)

while True:

    Success, frame1 = cam.read()

    Success, frame2 = cam.read()

    difference = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(difference, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    
    dilate = cv2.dilate(thresh, None, iterations=3)

    contours, _ = cv2.findContours(dilate,  cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # cv2.drawContours(frame1, contours, -1, (0,0,255), 2)
    for c in contours:
        if cv2.contourArea(c) < 5000:
            continue
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0,0,255), 2)
        winsound.Beep(500, 200)

    cv2.imshow("Secuirty Camera", frame1)

    key = cv2.waitKey(1)

    if key == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()