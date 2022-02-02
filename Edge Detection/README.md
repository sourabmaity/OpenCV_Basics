# Alpha Blending
Alpha blending is the process of overlaying a foreground image with transparency over a background image. The transparency is often the fourth channel of an image ( e.g. in a transparent PNG), but it can also be a separate image. This transparency mask is often called the alpha mask or the alpha matte.
<details open>
<summary>Alpha Blending</summary>

```bash
src2 = cv2.resize(src2, img.shape[1::-1])
dst = cv2.addWeighted(img, 0.5, src2, 0.5, 0)
cv2.imshow("Alpha Blended", dst)
```

</details>

### AND
A bitwise AND is a binary operation that takes two equal-length binary representations and performs the logical AND operation on each pair of the corresponding bits. Thus, if both bits in the compared position are 1, the bit in the resulting binary representation is 1 (1 × 1 = 1); otherwise, the result is 0 (1 × 0 = 0 and 0 × 0 = 0).

<img src="https://github.com/sourabmaity/OpenCV_Basics/blob/main/Alpha%20Blending/and.png" >
<details open>
<summary>AND</summary>

```bash
and_ = cv2.bitwise_and(img, mask)
cv2.imshow("And", and_)
```

</details>

### OR
A bitwise OR is a binary operation that takes two bit patterns of equal length and performs the logical inclusive OR operation on each pair of corresponding bits. The result in each position is 0 if both bits are 0, while otherwise the result is 1.

<img src="https://github.com/sourabmaity/OpenCV_Basics/blob/main/Alpha%20Blending/or.png" >
<details open>
<summary>OR</summary>

```bash
or_ = cv2.bitwise_or(img, mask)
cv2.imshow("Or", or_)
```

</details>

### XOR
A bitwise XOR is a binary operation that takes two bit patterns of equal length and performs the logical exclusive OR operation on each pair of corresponding bits. The result in each position is 1 if only one of the bits is 1, but will be 0 if both are 0 or both are 1. In this we perform the comparison of two bits, being 1 if the two bits are different, and 0 if they are the same.

<img src="https://github.com/sourabmaity/OpenCV_Basics/blob/main/Alpha%20Blending/xor.png" >
<details open>
<summary>XOR</summary>

```bash
xor_ = cv2.bitwise_xor(img, mask)
cv2.imshow("XOR", xor_)
```

</details>

### NOT
The bitwise NOT, or complement, is a unary operation that performs logical negation on each bit, forming the ones' complement of the given binary value. Bits that are 0 become 1, and those that are 1 become 0.

<img src="https://github.com/sourabmaity/OpenCV_Basics/blob/main/Alpha%20Blending/not.png" >
<details open>
<summary>NOT</summary>

```bash
not_ = cv2.bitwise_not(img, mask)
cv2.imshow("Not", not_)
```

</details>

## Mask Image
<img src="https://github.com/sourabmaity/OpenCV_Basics/blob/main/Alpha%20Blending/mask.png" >

## Output
<img src="https://github.com/sourabmaity/OpenCV_Basics/blob/main/Alpha%20Blending/AlphaBlending.png" >
