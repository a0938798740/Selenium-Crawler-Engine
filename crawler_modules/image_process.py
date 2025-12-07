from PIL import Image

def crop_image(original_image, box, new_image):
    """
    Crops the original image to the specified box coordinates.
    """
    with Image.open(original_image) as img:
        cropped_image = img.crop(box)
        cropped_image.save(new_image)

def grayScaler(image, threshold=80):
    """
    Converts image to grayscale and applies binary thresholding.
    Pixels lighter than threshold become white, others black.
    """
    image = image.convert("L")  # Convert to grayscale
    pixels = image.load()

    for x in range(image.width):
        for y in range(image.height):
            # Binary threshold logic
            pixels[x, y] = 255 if pixels[x, y] > threshold else 0
            
    return image

def dePoint(image):
    """
    Custom denoising algorithm.
    Removes isolated noise pixels ('pepper noise') by checking 8-neighbor connectivity.
    """
    pixels = image.load()
    w, h = image.size

    # Iterate through inner pixels, avoiding boundaries
    for x in range(1, w - 1):
        for y in range(1, h - 1):
            # Count white neighbors in all 8 directions
            white_neighbors = 0
            
            # Check cardinal directions (N, S, W, E)
            if pixels[x, y-1] > 245: white_neighbors += 1
            if pixels[x, y+1] > 245: white_neighbors += 1
            if pixels[x-1, y] > 245: white_neighbors += 1
            if pixels[x+1, y] > 245: white_neighbors += 1
            
            # Check diagonal directions (NW, NE, SW, SE)
            if pixels[x-1, y-1] > 245: white_neighbors += 1
            if pixels[x-1, y+1] > 245: white_neighbors += 1
            if pixels[x+1, y-1] > 245: white_neighbors += 1
            if pixels[x+1, y+1] > 245: white_neighbors += 1

            # If a pixel is surrounded by mostly white space, treat it as noise
            if white_neighbors > 5:
                pixels[x, y] = 255
                
    return image
