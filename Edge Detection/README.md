# Edge Detection
Edge detection is an image-processing technique, which is used to identify the boundaries (edges) of objects, or regions within an image. Edges are among the most important features associated with images. We come to know of the underlying structure of an image through its edges. Computer vision processing pipelines therefore extensively use edge detection in applications.

## Edges Detection Process
Edges are characterized by sudden changes in pixel intensity. To detect edges, we need to go looking for such changes in the neighboring pixels. Come, let’s explore the use of two important edge-detection algorithms available in OpenCV: Sobel Edge Detection and Canny Edge Detection. We will discuss  the theory as well as  demonstrate the use of each in OpenCV.

### Sobel Edge Detection
Sobel Edge Detection is one of the most widely used algorithms for edge detection. The Sobel Operator detects edges that are marked by sudden changes in pixel intensity.

In the code example below, we use the Sobel() function to compute:
1. the Sobel edge image individually, in both directions (x and y),
2. the composite gradient in both directions (xy)
The following is the syntax for applying Sobel edge detection using OpenCV:
```bash
Sobel(src, ddepth, dx, dy)
```
The parameter ddepth specifies the precision of the output image, while dx and dy specify the order of the derivative in each direction. For example:

1. If dx=1 and dy=0, we compute the 1st derivative Sobel image in the x-direction.
2. If dx=0 and dy=1, we compute the 1st derivative Sobel image in the Y-direction.
3. If both dx=1 and dy=1, we compute the 1st derivative Sobel image in both directions


<details open>
<summary>Sobel Edge Detection</summary>

```bash
sobelX = cv2.Sobel(src=img_gray, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5)
sobelY = cv2.Sobel(src=img_gray, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5)
sobelXY = cv2.Sobel(src=img_gray, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5)
```
</details>

### Canny Edge Detection
Canny Edge Detection is one of the most popular edge-detection methods in use today because it is so robust and flexible.The algorithm itself follows a three-stage process for extracting edges from an image. Add to it image blurring, a necessary preprocessing step to reduce noise.

The following is the syntax for applying Canny edge detection using OpenCV:
```bash
Canny(image, threshold1, threshold2)
```
In the code example below, the  Canny() function implements the methodology described above. We just supply the two thresholds used by the Canny Edge Detection algorithm, and OpenCV handles all the implementation details. Don’t forget to blur the image, before calling the Canny() function. It is a highly-recommended preprocessing step. To learn more about the optional arguments, please refer to the OpenCV documentation page.
<details open>
<summary>Canny Edge Detection</summary>

```bash
img_blur = cv2.GaussianBlur(img_gray, (3, 3), 0)
canny = cv2.Canny(image=img_blur, threshold1=100, threshold2=200)
```
</details>

### Laplacian Edge Detection
Unlike the Sobel edge detector, the Laplacian edge detector uses only one kernel. It calculates second order derivatives in a single pass.

The following is the syntax for applying Laplacian edge detection using OpenCV:
```bash
Laplacian( src_gray, dst, ddepth, kernel_size, scale, delta, BORDER_DEFAULT );
```
The arguments are:
1. src_gray: The input image.
2. dst: Destination (output) image
3. ddepth: Depth of the destination image. Since our input is CV_8U we define ddepth = CV_16S to avoid overflow
4. kernel_size: The kernel size of the Sobel operator to be applied internally. We use 3 in this example.
5. scale, delta and BORDER_DEFAULT: We leave them as default values.

<details open>
<summary>Laplacian Edge Detection</summary>

```bash
laplacian = cv2.Laplacian(img, cv2.CV_64F)
```
</details>
