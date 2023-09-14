import cv2

cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

img_counter = 0
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3));
fgbg = cv2.bgsegm.createBackgroundSubtractorGMG();

# fgbg = cv2.createBackgroundSubtractorMOG2();

while True:
    ret, frame = cam.read()
    fgmask = fgbg.apply(frame);
    img = cv2.resize(fgmask, (200, 200))
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test", img)
    img.resize((200,200))

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, img)
        print("{} written!".format(img_name))
        img_counter += 1

cam.release()

cv2.destroyAllWindows()
