import click
from PIL import Image, ImageFilter, ImageEnhance

def apply_gaussian_blur(image, blur_radius):
    """Applies Gaussian blur to an image."""
    return image.filter(ImageFilter.GaussianBlur(blur_radius))

def rotate_image(image: Image.Image) -> Image.Image:
    """Rotates the image 90 degrees clockwise."""
    return image.rotate(-90.0, expand=True)

def apply_hdr_effect(image: Image.Image):
    """Applies a simulated HDR effect to the image."""
    # Enhance color
    enhancer = ImageEnhance.Color(image)
    image = enhancer.enhance(1.5)

    # Enhance contrast
    enhancer = ImageEnhance.Contrast(image)
    return enhancer.enhance(1.5)

@click.command()
@click.argument('image_path', type=click.Path(exists=True, dir_okay=False))
@click.option('--blur', 'apply_blur', is_flag=True, help='Apply Gaussian blur to the image.')
@click.option('--blur-radius', type=float, default=2.0, show_default=True, help='Radius for Gaussian blur.')
@click.option('--rotate', 'rotate_image', is_flag=True, help='Rotate the image 90 degrees clockwise.')
@click.option('--hdr', 'apply_hdr', is_flag=True, help='Apply simulated HDR effect to the image.')
@click.option('--save-path', type=click.Path(), help='Path to save the processed image.', required=True)
def main(image_path, apply_blur, blur_radius, rotate_image, apply_hdr, save_path):
    """
    Processes an IMAGE_PATH with optional effects: Gaussian blur, 90-degree rotation, and simulated HDR.
    """
    try:
        with Image.open(image_path) as img:
            if apply_blur:
                img = apply_gaussian_blur(blur_radius, img)
            
            if rotate_image:
                img = rotate_image(img)
            
            if apply_hdr:
                img = apply_hdr_effect(img)

            img.save(save_path)
            click.echo(f"Processed image saved to {save_path}")
    
    except Exception as e:
        click.echo(f"An error occurred: {e}", err=True)

if __name__ == "__main__":
    main()
