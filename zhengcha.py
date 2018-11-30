import cv2
import numpy as np
def absdiff_demo(image_1, image_2, sThre):
    gray_image_1 = cv2.cvtColor(image_1, cv2.COLOR_BGR2GRAY)  #灰度化
    gray_image_1 = cv2.GaussianBlur(gray_image_1, (3, 3), 0)  #高斯滤波
    gray_image_2 = cv2.cvtColor(image_2, cv2.COLOR_BGR2GRAY)
    gray_image_2 = cv2.GaussianBlur(gray_image_2, (3, 3), 0)
    d_frame = cv2.absdiff(gray_image_2, gray_image_1)
    # print("huidufenbu",np.unique(d_frame))
    ret, d_frame = cv2.threshold(d_frame, sThre, 255, cv2.THRESH_BINARY)
    # th2 = cv2.adaptiveThreshold(d_frame, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
    print(d_frame.shape[0],d_frame.shape[1],d_frame.sum)
    return d_frame
def lunkuo(img):
    shape=img.shape
    print(shape)
    img,contours,_= cv2.findContours(img, cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_SIMPLE)
    # cv2.imshow("img", img)
    # cv2.waitKey(500)
    # print("the number of contours",contours)
    # img=cv2.drawContours(img, contours, 1, (0, 0, 255), 3)
    for i in range(0, len(contours)):
        x, y, w, h = cv2.boundingRect(contours[i])
        if w >=shape[0]//15 and h >=shape[1]//15:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 5)
    # cv2.imshow("img", img)
    # cv2.waitKey(0)
    return img


def junzhi(img):
    sum_r =  img[:, :, 0].mean()
    sum_g =  img[:, :, 1].mean()
    sum_b =  img[:, :, 2].mean()

# capture = cv2.VideoCapture("//Users/zhuxuhan/Desktop/test.mp4")
# sThre = 5 #sThre表示像素阈值
# i = 0
# while(True):
#     ret, frame = capture.read()
#
#
#
#     if i == 0:
#         cv2.waitKey(3300)
#         i = i + 1
#     ret_2, frame_2 = capture.read()
#
#
#     d_frame = absdiff_demo(frame, frame_2, sThre)
#     cv2.imwrite("./imgtest/500.jpeg",frame)
    # print(d_frame)
    #
    # if not d_frame.all == None:
    #     cv2.imshow('image', d_frame)
    #     cv2.waitKey(100)
    # cv2.destroyWindow('image')
frame1=cv2.imread('./imgtest/tt/0.jpg')
frame2=cv2.imread('./imgtest/tt/1394.jpg')
sThre = 100 #sThre表示像素阈值
d_frame = absdiff_demo(frame1, frame2, sThre)
lunkuo_img=lunkuo(d_frame)
cv2.imwrite("./imgtest/500.jpeg",lunkuo_img)