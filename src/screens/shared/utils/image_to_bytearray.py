def image_to_bytearray(image_path):
    with open(image_path, 'rb') as file:
        image_data = file.read()
        bytearray_data = bytearray(image_data)
        return bytearray_data