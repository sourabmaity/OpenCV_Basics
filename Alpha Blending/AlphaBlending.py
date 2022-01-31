import cv2

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 420)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)
src2 = cv2.imread("under_the_sea_v2.png")
# src2 = cv2.resize(src2, (360, 640))
mask = cv2.imread("mask.png")
# mask = cv2.resize(mask, (360, 640))

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)

    # Alpha Blending
    # dst = cv2.addWeighted(src1, alpha, src2, beta, gamma[, dst[, dtype]])
    # dst = src1 * alpha + src2 * beta + gamma
    src2 = cv2.resize(src2, img.shape[1::-1])
    mask = cv2.resize(mask, img.shape[1::-1])
    dst = cv2.addWeighted(img, 0.5, src2, 0.5, 0)
    cv2.imshow("Alpha Blended", dst)

    # Masking
    and_ = cv2.bitwise_and(img, mask)
    cv2.imshow("And", and_)
    or_ = cv2.bitwise_or(img, mask)
    cv2.imshow("Or", or_)
    xor_ = cv2.bitwise_xor(img, mask)
    cv2.imshow("XOR", xor_)
    # not_ = cv2.bitwise_not(img, mask)
    # cv2.imshow("Not", not_)

    cv2.imshow("Original", img)
    if cv2.waitKey(5) & 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()
