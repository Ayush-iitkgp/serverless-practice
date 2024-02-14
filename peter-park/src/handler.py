import json
import base64
from PIL import Image
import pytesseract

def image_handler(event, context):
    print(event)

    
    body = event.get(['body'], None)
    if body:
        encoded_image = body['image']
        text = predict_text(image=encoded_image)
        return {"statusCode": 200, "body": json.dumps(text)}

    return {
        "statusCode": 422,
        "body": "Please provide image encoding in the body"
    }

def predict_text(encoded_image):

    # # Decode base64 string to binary data
    binary_data = decode_base64_img(encoded_image)

    # Convert binary data to PIL image
    image = Image.open(io.BytesIO(binary_data))

    # Perform OCR on the image
    text = pytesseract.image_to_string(image=image)
    return text


# if __name__ == '__main__':
#     image_handler({}, {})
