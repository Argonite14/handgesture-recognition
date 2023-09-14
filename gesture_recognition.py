from tensorflow import keras
import os
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import cvzone
import cv2
import datetime


kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3));
fgbg = cv2.bgsegm.createBackgroundSubtractorGMG();

model = keras.models.load_model('C:\\Users\\neil2\\PycharmProjects\\computer vision\\my_model.h5')
video = cv2.VideoCapture(0)

pcount=0
while True:
        _, frame = video.read()

        fgmask = fgbg.apply(frame);
        fgmask = cv2.cvtColor(fgmask, cv2.COLOR_GRAY2RGB)
        im = Image.fromarray(fgmask, 'RGB')
        # print(im)

        im = im.resize((200,200))
        img_array = np.array(im)

        img_array = np.expand_dims(img_array, axis=0)

        prediction = model.predict(img_array)#[0][0]
        print(prediction)
        if (prediction[0][0] >= 0.8):
                cv2.putText(frame, 'Default '.format(100 * prediction[0][1]), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1,(255, 0, 0), 2, cv2.LINE_4)
                print("Default")

        elif(prediction[0][1] >= 0.8):
                cv2.putText(frame,'PALM'.format(100 * prediction[0][0]),(50, 50),cv2.FONT_HERSHEY_SIMPLEX, 1,(255, 0, 0),2,cv2.LINE_4)
                print("PALM")
                pcount+=1
        elif(prediction[0][2] >= 0.8):
            cv2.putText(frame,'ThumbDown: '.format(100 * prediction[0][1]),(50, 50),cv2.FONT_HERSHEY_SIMPLEX, 1,(255, 0, 0),2,cv2.LINE_4)
            print("ThumbDown")
        elif(prediction[0][3] >= 0.8):
            cv2.putText(frame,'Thumbup: '.format(100 * prediction[0][1]),(50, 50),cv2.FONT_HERSHEY_SIMPLEX, 1,(255, 0, 0),2,cv2.LINE_4)
            print("Thumbup")
        # else:
        #     cv2.putText(frame,'Default '.format(100 * prediction[0][1]),(50, 50),cv2.FONT_HERSHEY_SIMPLEX, 1,(255, 0, 0),2,cv2.LINE_4)

        print(pcount)
        if pcount > 70:
                break
        cv2.imshow("Prediction", frame, )
        key=cv2.waitKey(1)
        if key == ord('q'):
                break
video.release()
cv2.destroyAllWindows()
# dir_path = "basedata/test"
# dir_path = "basedata/test"
# for i in os.listdir(dir_path):QQ
#     img = image.load_img(dir_path + '//' + i, target_size=(200, 200))
#     plt.imshow(img)
#     plt.show()
#
#     x = image.img_to_array(img)
#     x = np.expand_dims(x, axis=0)
#     images = np.vstack([x])
#
#     val = model.predict(images)
#     if val[0][0] == True:
#         print('Palm')
#     elif val[0][1] == True:
#         print('ThumbDown')
#     elif val[0][2] == True:
#         print('Thumbup')



