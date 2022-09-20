import cv2


def main():
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    img_file = "arsenal.jpg"
    img = cv2.imread(img_file)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow("img", img)
    cv2.waitKey()

    img_name, img_extension = img_file.split(".")
    cv2.imwrite(f"{img_name}_faces_detected.{img_extension}", img)


if __name__ == "__main__":
    main()
