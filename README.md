# Noughts & Crosses Project (PyQt6)

Project for my college course.

## Installation

1. Ensure [Poetry](https://python-poetry.org/) is installed (either via [pipx](https://pipx.pypa.io/stable/) or [uv](https://docs.astral.sh/uv/)):

```shell
poetry --version
```

2. Clone this repo (or download and extract the zip/tarball)

```shell
git clone https://github.com/Cornelius-Figgle/noughts-crosses-qt6
cd noughts-crosses-qt6
```

3. Install the required dependencies

```shell
poetry install
```

## Usage

```shell
poetry run python3 noughts_crosses_qt6/gui.py
```

### Troubleshooting

If you receive a `ModuleNotFound` error when running (mainly occurs on Windows), then switch `python3` for `python`:

```shell
poetry run python noughts_crosses_qt6/gui.py
```

## External Libraries Used

- qtawesome
- PyQt6

## Sources Used

- [PythonGUIs PyQt6 Basic Tutorial](https://www.pythonguis.com/pyqt6-tutorial/)
- [Python Type Hints Specification](https://docs.python.org/3/library/typing.html)
- [Javascript Noughts and Crosses](https://www.advanced-ict.info/javascript/noughts_and_crosses.html#:~:text=The%20Algorithm)
