import cv2

img = cv2.imread('/Users/tanvi/Documents/solar-system.jpg')

cv2.putText(img, 
            "Sun", 
            (20, 300),
            cv2.FONT_HERSHEY_COMPLEX, 
            0.5, 
            (255, 255, 255)
            )

cv2.putText(img, 
            "Mercury", 
            (100, 260),
            cv2.FONT_HERSHEY_COMPLEX, 
            0.5, 
            (255, 255, 255)
            )

cv2.putText(img, 
            "Venus", 
            (185, 300),
            cv2.FONT_HERSHEY_COMPLEX, 
            0.5, 
            (255, 255, 255)
            )

cv2.putText(img, 
            "Earth", 
            (287, 270),
            cv2.FONT_HERSHEY_COMPLEX, 
            0.5, 
            (255, 255, 255)
            )

cv2.putText(img, 
            "Mars", 
            (378, 300),
            cv2.FONT_HERSHEY_COMPLEX, 
            0.5, 
            (255, 255, 255)
            )

cv2.putText(img, 
            "Jupiter", 
            (550, 400),
            cv2.FONT_HERSHEY_COMPLEX, 
            0.5, 
            (255, 255, 255)
            )

cv2.putText(img, 
            "Saturn", 
            (790, 350),
            cv2.FONT_HERSHEY_COMPLEX, 
            0.5, 
            (255, 255, 255)
            )

cv2.putText(img, 
            "Uranus", 
            (950, 320),
            cv2.FONT_HERSHEY_COMPLEX, 
            0.5, 
            (255, 255, 255)
            )

cv2.putText(img, 
            "Neptune", 
            (1110, 320),
            cv2.FONT_HERSHEY_COMPLEX, 
            0.5, 
            (255, 255, 255)
            )

#cv2.imshow("output", img)
#cv2.waitKey(0)
cv2.imwrite('/Users/tanvi/Documents/Solar_System_With_Names.jpg', img)


