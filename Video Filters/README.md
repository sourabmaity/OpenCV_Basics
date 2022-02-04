# Video Filters
OpenCV (Open Source Computer Vision Library) is a library of programming functions mainly aimed at real-time computer vision. Originally developed by Intel, it was later supported by Willow Garage then Itseez (which was later acquired by Intel). The library is cross-platform and free for use under the open-source Apache 2 License. Starting with 2011, OpenCV features GPU acceleration for real-time operations.
### Gaussian Blurring
```bash
GaussianBlur(src, ksize, sigmaX[, dst[, sigmaY[, borderType]]])
```
The GaussianBlur() function requires four input arguments:

- The first argument, src, specifies the source image that you want to filter.
- The second argument is ksize, which defines the size of the Gaussian kernel. Here, we are using a 5×5 kernel.
- The final two arguments are sigmaX and sigmaY, which are both set to 0. These are the Gaussian kernel standard deviations, in the X (horizontal) and Y (vertical) direction. The default setting of sigmaY is zero. If you simply  set sigmaX to zero, then the standard deviations are computed from the kernel size (width and height respectively). You can also explicitly set the size of each argument to positive values greater than zero.
<details open>
<summary>Gaussian Blurr</summary>

```bash
Gaussian = cv2.GaussianBlur(img, (5, 5), 0)
```
</details>

### Median Blur
```bash
medianBlur(src, ksize)
```
This function has just two required arguments:

- The first is the source image.
- The second is the kernel size, which must be an odd, positive integer.
<details open>
<summary>Median Blur</summary>

```bash
median = cv2.medianBlur(img, 5)
```
</details>

### Bilateral Blur
```bash
bilateralFilter(src, d, sigmaColor, sigmaSpace)
```
This function has four required arguments:

- The first argument of the function is the source image.
- The next argument d, defines the diameter of the pixel neighborhood used for filtering.
- The next two arguments, sigmaColor and sigmaSpace define the standard deviation of the (1D) color-intensity distribution and (2D) spatial distribution respectively.
   - The sigmaSpace parameter defines the spatial extent of the kernel, in both the x and y directions (just like the Gaussian blur filter previously described).
   - The sigmaColor parameter defines the one-dimensional Gaussian distribution, which specifies the degree to which differences in pixel intensity can be tolerated.
<details open>
<summary>Bilateral Blur</summary>

```bash
bilateral = cv2.bilateralFilter(img, 9, 75, 75)
```
</details>

## Blur
```bash
blur(src, ksize[, dst[, anchor[, borderType]]])
```
This function has four required arguments:

- src: It is the image whose is to be blurred.
- ksize: A tuple representing the blurring kernel size.
- dst: It is the output image of the same size and type as src.
- anchor: It is a variable of type integer representing anchor point and it’s default value Point is (-1, -1) which means that the anchor is at the kernel center.
- borderType: It depicts what kind of border to be added. It is defined by flags like cv2.BORDER_CONSTANT, cv2.BORDER_REFLECT, etc
- Return Value: It returns an image.
<details open>
<summary>Blur</summary>

```bash
blur = cv2.blur(img, (5, 5))
```
</details>
