import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
print(cap.get(cv2.CAP_PROP_FPS))
height, width = 480, 640
center = (width / 2, height / 2)
while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    # print(img.shape)

    # Scaling
    cv2.resize(img,(400,400))

    # To get the rotation matrix
    rotate_matrix = cv2.getRotationMatrix2D(center=center, angle=30, scale=1)
    # Rotate / Translate the image
    rotated_image = cv2.warpAffine(src=img, M=rotate_matrix, dsize=(width, height))

    #tx, ty = width / 4, height / 4
    # create the translation matrix using tx and ty, it is a NumPy array
    '''translation_matrix = np.array([
        [1, 0, tx],
        [0, 1, ty]
    ], dtype=np.float32)'''

    pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
    pts2 = np.float32([[10, 100], [200, 50], [100, 250]])
    M = cv2.getAffineTransform(pts1, pts2)  # Affine Transformation
    pts1 = np.float32([[56, 65], [368, 52], [28, 387], [389, 390]])
    pts2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])
    M = cv2.getPerspectiveTransform(pts1, pts2)  # Perspective Transformation

    cv2.imshow("Original", img)
    cv2.imshow("Rotated image", rotated_image)
    if cv2.waitKey(5) & 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()
