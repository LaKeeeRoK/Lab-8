import cv2

def track_marker(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    marker_position = None
    if contours:
        largest_contour = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(largest_contour)
        marker_position = (x + w // 2, y + h // 2)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.circle(frame, marker_position, 5, (0, 0, 255), -1)
    return frame, marker_position

video_capture = cv2.VideoCapture('sample.mp4')
f = open("Points.txt", "w")
while True:
    ret, frame = video_capture.read()
    if not ret:
        break
    tracked_frame, marker_position = track_marker(frame)
    if marker_position:
        cv2.putText(tracked_frame, f"Marker Position: {marker_position}", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    cv2.imshow('Video', tracked_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    f.write(str(marker_position) + "\n")
f.close

video_capture.release()
cv2.destroyAllWindows()