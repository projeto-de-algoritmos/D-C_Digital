import os
import cv2

sample = cv2.imread("img.png")

best_score = 0
filename = None
image = None

kp1, kp2, mp = None, None, None

for file in [file for file in os.listdir("/real")][:1000]:
	fingerprint_image = cv2.imread("/real/" + file)
	sift = cv2.SIFT_create()
	keypoints_1, descriptors_1 = sift.detectionAndCompute(sample, None)
	keypoints_2, descriptors_2 = sift.detectAndCompute(fingerprint_image, None)
