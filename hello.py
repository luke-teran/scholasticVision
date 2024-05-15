import cv2

# print("DISPLAY variable value:", os.environ.get('DISPLAY'))


img = cv2.imread('./assets/knight.jpg', cv2.IMREAD_UNCHANGED)

cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()