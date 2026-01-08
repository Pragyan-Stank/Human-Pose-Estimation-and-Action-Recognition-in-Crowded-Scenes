import cv2


def draw_angle(frame, angle, position):
    cv2.putText(
        frame,
        f"{int(angle)} deg",
        position,
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 255, 0),
        2
    )
