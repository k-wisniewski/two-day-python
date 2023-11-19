import click
from PIL import Image, ImageFilter, ImageEnhance
from pathlib import Path

def apply_gaussian_blur(image: Image.Image, blur_radius: float) -> Image.Image:
    """Applies Gaussian blur to an image."""
    return image.filter(ImageFilter.GaussianBlur(blur_radius))

def rotate_image(image: Image.Image) -> Image.Image:
    """Rotates the image 90 degrees clockwise."""
    return image.rotate(-90.0, expand=True)

def apply_hdr_effect(image: Image.Image) -> Image.Image:
    """Applies a simulated HDR effect to the image."""
    # Enhance color
    color_enhancer = ImageEnhance.Color(image)
    image = color_enhancer.enhance(1.5)

    # Enhance contrast
    contrast_enhancer = ImageEnhance.Contrast(image)
    return contrast_enhancer.enhance(1.5)

@click.command()
@click.argument('image_path', type=click.Path(exists=True, dir_okay=False))
@click.option('--blur', 'should_apply_blur', is_flag=True, help='Apply Gaussian blur to the image.', type=click.BOOL)
@click.option('--blur-radius', type=float, default=2.0, show_default=True, help='Radius for Gaussian blur.', type=click.FLOAT)
@click.option('--rotate', 'should_rotate_image', is_flag=True, help='Rotate the image 90 degrees clockwise.', type=click.BOOL)
@click.option('--hdr', 'should_apply_hdr', is_flag=True, help='Apply simulated HDR effect to the image.', type=click.BOOL)
@click.option('--save-path', type=click.Path(dir_okay=False), help='Path to save the processed image.', required=True)
def main(
    image_path: Path,
    should_apply_blur: bool,
    blur_radius: float,
    should_rotate_image: bool,
    should_apply_hdr: bool,
    save_path: Path
) -> None:
    """
    Processes an IMAGE_PATH with optional effects: Gaussian blur, 90-degree rotation, and simulated HDR.
    """
    try:
        with Image.open(image_path) as img:
            if should_apply_blur:
                img = apply_gaussian_blur(img, blur_radius)
            
            if should_rotate_image:
                img = rotate_image(img)
            
            if should_apply_hdr:
                img = apply_hdr_effect(img)

            img.save(save_path)
            click.echo(f"Processed image saved to {save_path}")
    
    except Exception as e:
        click.echo(f"An error occurred: {e}", err=True)

if __name__ == "__main__":
    main()
