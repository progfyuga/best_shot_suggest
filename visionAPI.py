import io
import os


# Imports the Google Cloud client library
from google.cloud import vision

# Instantiates a client
client = vision.ImageAnnotatorClient()

#番号チェック
check_num = []

# 写真枚数分VisionAPI繰り返す
for num in range(0,3100,10):
    print(num)
    
    # The name of the image file to annotate
    file_name = os.path.abspath('flame_data/sample_video_img_' + str(num).rjust(4, '0') + '.png')
    # Loads the image into memory
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    # Performs label detection on the image file
    response = client.label_detection(image=image)
    response2 = client.face_detection(image=image)
    labels = response.label_annotations
    faces = response2.face_annotations    

    # 表情のスコア
    # Names of likelihood from google.cloud.vision.enums
    likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE', 'LIKELY', 'VERY_LIKELY')
    print('Faces:')
    
    for face in faces:

        #表情のスコアが高い時
        if likelihood_name[face.anger_likelihood] == 'VERY_LIKELY' or likelihood_name[face.anger_likelihood] == 'LIKELY':
            check_num.append(num)
        elif likelihood_name[face.joy_likelihood] == 'VERY_LIKELY' or likelihood_name[face.anger_likelihood] == 'LIKELY':
            check_num.append(num)
        elif likelihood_name[face.surprise_likelihood] == 'VERY_LIKELY' or likelihood_name[face.anger_likelihood] == 'LIKELY':
            check_num.append(num)
            
        print('anger: {}'.format(likelihood_name[face.anger_likelihood]))
        print('joy: {}'.format(likelihood_name[face.joy_likelihood]))
        print('surprise: {}'.format(likelihood_name[face.surprise_likelihood]))
        #他にも項目ある！？

        # vertices = (['({},{})'.format(vertex.x, vertex.y)
        #             for vertex in face.bounding_poly.vertices])

        # print('face bounds: {}'.format(','.join(vertices)))

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

    print(check_num)