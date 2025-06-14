import cv2

def extract_text_contours(image_path):
    
    # Read image
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Threshold
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    
    # Morphological operations
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    dilated = cv2.dilate(thresh, kernel, iterations=1)
    
    # Erode to remove noise
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 1))
    erode = cv2.erode(thresh, kernel, iterations=1)

    # Save intermediate result
    cv2.imwrite("erode_image.jpg", erode)
    cv2.imwrite("dilated_image.jpg", dilated)

    # Find contours
    contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Extract text regions
    for i, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if area > 10:  # Filter small contours
            x, y, w, h = cv2.boundingRect(contour)

            # Draw rectangle on original
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    # Save result
    cv2.imwrite("contours_result.jpg", image)

# Usage
extract_text_contours("law_1.jpg")