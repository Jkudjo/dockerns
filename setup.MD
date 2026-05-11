# Setup notes

The preferred installation path is the package entry point from `pyproject.toml`:

```sh
python -m pip install -e .
dockerns
```

This installs a `dockerns` console command without copying source files into
system directories.

## Manual install option

If you still need a single-file install, copy the script into a directory on
your `PATH`:

```sh
sudo cp dockerns.py /usr/local/bin/dockerns
sudo chmod +x /usr/local/bin/dockerns
```

The script includes a `#!/usr/bin/env python3` shebang, so it can be executed
without the `.py` extension after it has executable permissions.

## Operational note

DockerNS currently invokes Docker with `sudo`. Make sure the target user is
allowed to run Docker commands in the environment where the tool is installed.
