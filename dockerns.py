#!/usr/bin/env python3
"""Interactive Docker image selector and shell launcher."""

from __future__ import annotations

import subprocess
import sys
from collections.abc import Callable, Sequence
from typing import Optional

IMAGE_FORMAT = "{{.Repository}}:{{.Tag}} {{.ID}}"
DOCKER_COMMAND = ("sudo", "docker")


class DockerCommandError(RuntimeError):
    """Raised when a Docker command cannot complete successfully."""


CommandRunner = Callable[..., subprocess.CompletedProcess[str]]


def list_images(command_runner: CommandRunner = subprocess.run) -> list[str]:
    """List all Docker images with sudo."""
    print("Listing images...")
    result = command_runner(
        [*DOCKER_COMMAND, "images", "--format", IMAGE_FORMAT],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    if result.returncode != 0:
        stderr = (result.stderr or "").strip()
        message = stderr or "docker images exited without an error message"
        raise DockerCommandError(f"Error listing images: {message}")

    images = [line for line in result.stdout.splitlines() if line.strip()]
    for i, image in enumerate(images, start=1):
        print(f"{i}. {image}")
    return images


def select_image(
    images: Sequence[str], input_func: Callable[[str], str] = input
) -> Optional[str]:
    """Prompt user to select an image."""
    if not images:
        return None
    try:
        selection = int(input_func("Select an image by number: ")) - 1
        if 0 <= selection < len(images):
            selected_image = images[selection]
            print(f"Selected image: {selected_image}")
            return selected_image.split(" ")[0]
        print("Invalid selection.")
        return None
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None


def run_container(
    image_id: str, command_runner: CommandRunner = subprocess.run
) -> subprocess.CompletedProcess[str]:
    """Run a container from the selected image and execute a shell inside it with sudo."""
    print(f"Running container from image: {image_id}")
    return command_runner([*DOCKER_COMMAND, "run", "-it", "--rm", image_id, "/bin/sh"])


def main() -> int:
    try:
        images = list_images()
    except DockerCommandError as exc:
        print(exc, file=sys.stderr)
        return 1

    if not images:
        print("No Docker images found.")
        return 0

    image = select_image(images)
    if image:
        result = run_container(image)
        return result.returncode

    print("No image selected.")
    return 1

if __name__ == "__main__":
    sys.exit(main())
