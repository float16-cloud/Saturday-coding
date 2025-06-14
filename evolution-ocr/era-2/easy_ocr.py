import easyocr
import cv2
import numpy as np 
image_path = 'image_4x.jpeg'
reader = easyocr.Reader(['en','th'])
bb_result = reader.detect(image_path)

def draw_boxes(image_path, result):
    image = cv2.imread(image_path)
    for box in result[0][0]:
        box = np.array(box, dtype=np.int32)
        cv2.rectangle(image, (box[0], box[2]), (box[1], box[3]), (0, 255, 0), 2)
    return image

output_image = draw_boxes(image_path, bb_result)
cv2.imwrite(f'bb_{image_path}', output_image)

# text_result = reader.readtext(
#                         image_path, 
#                         decoder='greedy', 
#                         add_margin=0.1, 
#                         min_size=60
#                     )
# def text_to_list(text_result):
#     text_list = []
#     for item in text_result:
#         text_list.append(item[1])
#     return text_list

# text_list = text_to_list(text_result)
# print("text_list:", text_list)