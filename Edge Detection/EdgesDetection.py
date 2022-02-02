import cv2

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
print(cap.get(cv2.CAP_PROP_FPS))

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Sobel Edges Detection
    sobelX = cv2.Sobel(src=img_gray, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5)
    sobelY = cv2.Sobel(src=img_gray, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5)
    sobelXY = cv2.Sobel(src=img_gray, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5)

    # Laplacian Edges Detection
    laplacian = cv2.Laplacian(img, cv2.CV_64F)

    # Canny Edges Detection
    img_blur = cv2.GaussianBlur(img_gray, (3, 3), 0)
    canny = cv2.Canny(image=img_blur, threshold1=100, threshold2=200)

    cv2.imshow("SobelX", sobelX)
    cv2.imshow("SobelY", sobelY)
    cv2.imshow("SobelXY", sobelXY)
    cv2.imshow("Laplacian", laplacian)
    cv2.imshow("Canny", canny)

    cv2.imshow("Original", img)
    if cv2.waitKey(5) & 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()
