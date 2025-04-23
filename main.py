from rembg import remove


def remove_background(input_path: str, output_path: str) -> None:
    with open(input_path, 'rb') as input_file:
        with open(output_path, 'wb') as output_file:
            image_bytes: bytes = input_file.read()
            output_bytes: bytes = remove(image_bytes)
            output_file.write(output_bytes)

if __name__ == "__main__":
    remove_background('input.png', 'output.png')
