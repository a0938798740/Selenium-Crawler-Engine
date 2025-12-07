from PIL import Image
import pytesseract
import re
from image_process import crop_image, grayScaler, dePoint

def identify_captcha(file_path):
    """
    General purpose CAPTCHA solver pipeline.
    
    Args:
        file_path (str): Path to the CAPTCHA image file.
        
    Returns:
        str: The solved alphanumeric code, or None if validation fails.
    """
    original_img = Image.open(file_path)
    
    # Step 1: Preprocessing (Grayscale + Denoising)
    processed_img = grayScaler(original_img, threshold=80)
    cleaned_img = dePoint(processed_img)
    
    # Step 2: OCR Execution (Dual Pass Strategy)
    # Attempt 1: Raw processed image
    result1 = pytesseract.image_to_string(processed_img)
    # Attempt 2: Denoised image
    result2 = pytesseract.image_to_string(cleaned_img)
    
    # Step 3: Result Cleaning & Validation
    clean_r1 = _clean_text(result1)
    clean_r2 = _clean_text(result2)
    
    # Simple voting/validation logic
    if len(clean_r1) == 5:
        return clean_r1
    if len(clean_r2) == 5:
        return clean_r2
        
    return None

def _clean_text(text):
    """Removes non-alphanumeric characters."""
    return re.sub('[^0-9A-Za-z]', '', text) if text else ""
