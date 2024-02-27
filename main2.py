import cv2
import time

def blur_img():
    img = cv2.imread("images\\variant-2.png")
    gaus_img = cv2.GaussianBlur(img, (5, 5), 15)
    cv2.imshow('blur_img', gaus_img)


def video_process():
    cap = cv2.VideoCapture(0)
    i = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        time.sleep(0.1)
        i += 1

    cap.release()

    

if __name__ == "__main__":
    video_process()

cv2.waitKey("q")
    