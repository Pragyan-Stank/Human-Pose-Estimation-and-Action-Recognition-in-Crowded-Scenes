import cv2

from core.pose_detector import PoseDetector
from core.pose_math import calculate_angle
from viz.visualizer import draw_angle
from io.video_stream import VideoStream


def main():
    detector = PoseDetector()
    stream = VideoStream(0)

    while True:
        success, frame = stream.read()
        if not success:
            break

        results = detector.detect(frame)

        if results.pose_landmarks:
            detector.draw(frame, results.pose_landmarks)

            lm = results.pose_landmarks.landmark
            h, w, _ = frame.shape

            shoulder = (int(lm[11].x * w), int(lm[11].y * h))
            elbow = (int(lm[13].x * w), int(lm[13].y * h))
            wrist = (int(lm[15].x * w), int(lm[15].y * h))

            angle = calculate_angle(shoulder, elbow, wrist)
            draw_angle(frame, angle, elbow)

        cv2.imshow("Pose Estimation System", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    stream.release()


if __name__ == "__main__":
    main()
