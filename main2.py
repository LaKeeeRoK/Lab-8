import cv2

def blur_img():
    img = cv2.imread("images\\variant-2.png")
    gaus_img = cv2.GaussianBlur(img, (5, 5), 15)
    cv2.imshow('blur_img', gaus_img)





if __name__ == "__main__":
    blur_img()
    cv2.waitKey(0)