import subprocess

def list_images():
    """List all Docker images with sudo."""
    print("Listing images...")
    try:
        result = subprocess.run(['sudo', 'docker', 'images', '--format', '{{.Repository}}:{{.Tag}} {{.ID}}'],
                                stdout=subprocess.PIPE, text=True, check=True)
        images = result.stdout.strip().split('\n')
        if images:
            return images
        else:
            print("No Docker images found.")
            return []
    except subprocess.CalledProcessError as e:
        print(f"Error listing images: {e}")
        return []

def select_image(images):
    """Use fzf to select an image."""
    if not images:
        return None
    try:
        # Convert the list of images to a format suitable for fzf
        image_list = '\n'.join(images)
        print("Opening fzf for selection...")
        
        # Use subprocess.Popen to interact with fzf
        process = subprocess.Popen(['fzf'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = process.communicate(input=image_list)
        
        if process.returncode == 0:
            selected_image = stdout.strip()
            if selected_image:
                print(f"Selected image: {selected_image}")
                return selected_image.split(' ')[0]  # Return the repository:tag part
            else:
                print("No image selected.")
                return None
        else:
            print(f"fzf returned with code: {process.returncode}")
            print(f"stderr: {stderr}")
            return None
    except Exception as e:
        print(f"Exception during fzf execution: {e}")
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

