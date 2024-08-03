import subprocess

def list_images():
    """List all Docker images with sudo."""
    print("Listing images...")
    result = subprocess.run(['sudo', 'docker', 'images', '--format', '{{.Repository}}:{{.Tag}} {{.ID}}'],
                            stdout=subprocess.PIPE, text=True)
    if result.returncode != 0:
        print(f"Error listing images: {result.stderr}")
        return []
    images = result.stdout.strip().split('\n')
    for image in images:
        print(image)
    return images

def main():
    list_images()

if __name__ == "__main__":
    main()

