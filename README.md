# python-utils-79

A collection of lightweight, high-performance utility functions designed to streamline repetitive Python development tasks. This library focuses on clean code principles and zero-dependency implementation for maximum portability.

## Features

*   **File System Helpers**: Simplified context managers for recursive directory traversal and atomic file writing.
*   **Data Formatting**: Robust utilities for sanitizing nested dictionaries and converting complex objects to human-readable strings.
*   **Time & Date**: Built-in decorators to measure execution time and handle timezone-aware timestamp conversions effortlessly.
*   **Logging Wrapper**: A pre-configured logging interface that supports rotating file handlers and standard console output out-of-the-box.

## Installation

Install `python-utils-79` directly from PyPI:

```bash
pip install python-utils-79
```

Alternatively, if you are developing locally, install via requirements:

```bash
git clone https://github.com/Developer/python-utils-79.git
cd python-utils-79
pip install -e .
```

## Usage

Import the required modules to simplify your workflow immediately.

```python
from utils_79.timer import measure_time
from utils_79.files import safe_write

# Measure execution time of a function
@measure_time
def process_data(data):
    # Atomic write to filesystem
    safe_write("output.txt", str(data))

process_data({"id": 79, "status": "active"})
```

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.