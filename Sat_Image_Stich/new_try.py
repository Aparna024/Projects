import cv2
import numpy as np

def stitch_images(images):
    # Detect features in the images
    detector = cv2.SIFT_create()
    keypoints = []
    descriptors = []

    for image in images:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        kp, desc = detector.detectAndCompute(gray, None)
        keypoints.append(kp)
        descriptors.append(desc)

    # Match features between consecutive image pairs
    matcher = cv2.BFMatcher()
    matches = []
    for i in range(len(descriptors) - 1):
        matches.append(matcher.match(descriptors[i], descriptors[i+1]))

    # Find homography for each image pair
    homographies = []
    for match in matches:
        src_pts = np.float32([keypoints[i][m.queryIdx].pt for i, m in enumerate(match)]).reshape(-1, 1, 2)
        dst_pts = np.float32([keypoints[i+1][m.trainIdx].pt for i, m in enumerate(match)]).reshape(-1, 1, 2)
        homography, _ = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
        homographies.append(homography)

    # Determine the final size of the stitched image
    height, width = images[0].shape[:2]
    for homography in homographies:
        corners = cv2.warpPerspective(np.ones((height, width)), homography, (width, height))
        height, width = corners.shape[:2]

    # Create the stitched image
    stitched = np.zeros((height, width), dtype=np.uint8)
    stitched = cv2.warpPerspective(images[0], np.eye(3), (width, height), dst=stitched, borderMode=cv2.BORDER_TRANSPARENT)

    # Apply the homographies to stitch each image
    for i, homography in enumerate(homographies):
        stitched = cv2.warpPerspective(images[i+1], homography, (width, height), dst=stitched, borderMode=cv2.BORDER_TRANSPARENT)

    return stitched

# Example usage:
image1 = cv2.imread("C:/Users/Aparna/Documents/Sat_Image_Stich/i1.jpg")
image2 = cv2.imread("C:/Users/Aparna/Documents/Sat_Image_Stich/i2.jpg")
image3 = cv2.imread("C:/Users/Aparna/Documents/Sat_Image_Stich/i3.jpg")

result = stitch_images([image1, image2, image3])

cv2.imshow("Stitched Image", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
