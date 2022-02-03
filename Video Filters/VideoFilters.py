import cv2

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 420)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)

    # Blurring / Smoothing
    # Gaussian Blur
    Gaussian = cv2.GaussianBlur(img, (5, 5), 0)
    cv2.imshow('Gaussian Blurring', Gaussian)

    # Median Blur
    median = cv2.medianBlur(img, 5)
    cv2.imshow('Median Blurring', median)

    # Bilateral Blur
    bilateral = cv2.bilateralFilter(img, 9, 75, 75)
    cv2.imshow('Bilateral Blurring', bilateral)

    # Simple Blur
    blur = cv2.blur(img, (5, 5))
    cv2.imshow("Blur", blur)

    cv2.imshow("Original", img)
    if cv2.waitKey(5) & 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()
