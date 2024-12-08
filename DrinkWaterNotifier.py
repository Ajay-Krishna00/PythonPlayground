import time
from plyer import notification
from PIL import Image, ImageDraw
#You can use the PIL library to generate a simple icon image

if __name__ == "__main__":
    # Create a new image with white background
    img = Image.new('RGB', (64, 64), color = 'white')

    # Initialize the drawing context
    d = ImageDraw.Draw(img)

    # Draw a simple water glass icon
    d.rectangle([16, 16, 48, 48], outline="blue", width=3)
    d.rectangle([20, 20, 44, 44], fill="blue")

    #Save the image
    img.save(r".\Assets\icon.ico")

    while True:
        notification.notify(
            title = "Please Drink Water Now",
            message = "Drinking water is important for your health",
            app_name="Health Notifier",
            app_icon = r".\Assets\icon.ico",
            ticker = "Drink Water Now",
            timeout = 10
        )
        time.sleep(1*60*60)
        

