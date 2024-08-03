import subprocess

def list_images():
    """List all Docker images with sudo."""
    print("Listing images...")
    try:
        result = subprocess.run(['sudo', 'docker', 'images', '--format', '{{.Repository}}:{{.Tag}} {{.ID}}'],
                                stdout=subprocess.PIPE, text=True, check=True)
        images = result.stdout.strip().split('\n')
        if images:
            for i, image in enumerate(images, start=1):
                print(f"{i}. {image}")
            return images
        else:
            print("No Docker images found.")
            return []
    except subprocess.CalledProcessError as e:
        print(f"Error listing images: {e}")
        return []

def select_image(images):
    """Prompt user to select an image."""
    if not images:
        return None
    try:
        selection = int(input("Select an image by number: ")) - 1
        if 0 <= selection < len(images):
            selected_image = images[selection]
            print(f"Selected image: {selected_image}")
            return selected_image.split(' ')[0]  # Return the repository:tag part
        else:
            print("Invalid selection.")
            return None
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None

def run_container(image_id):
    """Run a container from the selected image and execute a shell inside it with sudo."""
    print(f"Running container from image: {image_id}")
    subprocess.run(['sudo', 'docker', 'run', '-it', '--rm', image_id, '/bin/sh'])

def main():
    images = list_images()
    if not images:
        print("No Docker images found.")
        return

    image = select_image(images)
    if image:
        run_container(image)
    else:
        print("No image selected.")

if __name__ == "__main__":
    main()

