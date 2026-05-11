# DockerNS

DockerNS is a small Python CLI that lists local Docker images, lets you choose
one interactively, and opens `/bin/sh` in a temporary container.

## Current behavior

By default, DockerNS runs Docker through `sudo`:

- `sudo docker images --format '{{.Repository}}:{{.Tag}} {{.ID}}'`
- `sudo docker run -it --rm <image> /bin/sh`

That preserves the original behavior of this project. If your environment uses
the Docker group or rootless Docker, review `dockerns.py` before changing this
default because Docker socket access is effectively host-level privilege.

## Requirements

- Python 3.9 or newer
- Docker installed and running
- Permission to run Docker commands with `sudo`

## Installation

For local development:

```sh
python -m pip install -e .
```

After installation, run:

```sh
dockerns
```

You can also run the module directly without installing it:

```sh
python dockerns.py
```

## Usage

```text
$ dockerns
Listing images...
1. ubuntu:latest 1234567890ab
2. nginx:latest 234567890abc
3. mysql:5.7 34567890abcd
Select an image by number: 2
Selected image: nginx:latest 234567890abc
Running container from image: nginx:latest
```

The selected container is removed automatically after the shell exits because
DockerNS uses `docker run --rm`.

## Development

Run the unit tests:

```sh
python -m unittest discover -s tests
```

Compile-check the Python sources:

```sh
python -m compileall dockerns.py tests
```

The CI workflow runs both checks across supported Python versions.

## Troubleshooting

- **Docker is not running**: start Docker and rerun `dockerns`.
- **Permission denied**: confirm your user can run `sudo docker images`.
- **No images listed**: pull or build an image first, then rerun DockerNS.
- **Invalid input**: enter the number printed next to the target image.

## License

DockerNS is licensed under the MIT License. See [LICENSE](LICENSE).

## Contributing

Keep changes small and covered by tests where behavior changes. For larger
changes, open an issue first to discuss the intended behavior and operational
impact.
