import contextlib
import io
import subprocess
import unittest

import dockerns


class DockerNSTests(unittest.TestCase):
    def test_list_images_returns_non_empty_lines(self):
        def runner(command, **kwargs):
            self.assertEqual(
                command,
                [
                    "sudo",
                    "docker",
                    "images",
                    "--format",
                    "{{.Repository}}:{{.Tag}} {{.ID}}",
                ],
            )
            self.assertEqual(kwargs["stdout"], subprocess.PIPE)
            self.assertEqual(kwargs["stderr"], subprocess.PIPE)
            self.assertTrue(kwargs["text"])
            return subprocess.CompletedProcess(
                command,
                0,
                stdout="ubuntu:latest abc123\n\nnginx:stable def456\n",
                stderr="",
            )

        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            images = dockerns.list_images(command_runner=runner)

        self.assertEqual(images, ["ubuntu:latest abc123", "nginx:stable def456"])
        self.assertIn("1. ubuntu:latest abc123", output.getvalue())
        self.assertIn("2. nginx:stable def456", output.getvalue())

    def test_list_images_raises_with_stderr_on_docker_failure(self):
        def runner(command, **kwargs):
            return subprocess.CompletedProcess(
                command, 1, stdout="", stderr="Cannot connect to Docker daemon"
            )

        with self.assertRaisesRegex(
            dockerns.DockerCommandError, "Cannot connect to Docker daemon"
        ):
            dockerns.list_images(command_runner=runner)

    def test_select_image_returns_repository_tag(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            image = dockerns.select_image(
                ["ubuntu:latest abc123", "nginx:stable def456"],
                input_func=lambda prompt: "2",
            )

        self.assertEqual(image, "nginx:stable")
        self.assertIn("Selected image: nginx:stable def456", output.getvalue())

    def test_select_image_rejects_invalid_input(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            image = dockerns.select_image(
                ["ubuntu:latest abc123"], input_func=lambda prompt: "not-a-number"
            )

        self.assertIsNone(image)
        self.assertIn("Invalid input", output.getvalue())

    def test_run_container_invokes_interactive_docker_shell(self):
        calls = []

        def runner(command, **kwargs):
            calls.append((command, kwargs))
            return subprocess.CompletedProcess(command, 0)

        result = dockerns.run_container("ubuntu:latest", command_runner=runner)

        self.assertEqual(result.returncode, 0)
        self.assertEqual(
            calls,
            [(["sudo", "docker", "run", "-it", "--rm", "ubuntu:latest", "/bin/sh"], {})],
        )


if __name__ == "__main__":
    unittest.main()
