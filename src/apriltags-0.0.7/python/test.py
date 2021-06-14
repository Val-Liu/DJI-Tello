import apriltag
import cv2
img = cv2.imread('fat_tags.png',cv2.IMREAD_GRAYSCALE)
detector = apriltag.Detector()
result = detector.detect(img)
print(result)
