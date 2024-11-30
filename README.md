### Hexlet tests and linter status:
[![Actions Status](https://github.com/Ilia-Ivankov/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Ilia-Ivankov/python-project-50/actions)
### Maintanability:
[![Maintainability](https://api.codeclimate.com/v1/badges/22a84e877c1aaac04f1f/maintainability)](https://codeclimate.com/github/Ilia-Ivankov/python-project-50/maintainability)
### CI:
[![Python CI](https://github.com/Ilia-Ivankov/python-project-50/actions/workflows/pyci.yml/badge.svg)](https://github.com/Ilia-Ivankov/python-project-50/actions/workflows/pyci.yml)
### Test Coverage:
[![Test Coverage](https://api.codeclimate.com/v1/badges/22a84e877c1aaac04f1f/test_coverage)](https://codeclimate.com/github/Ilia-Ivankov/python-project-50/test_coverage)

# gendiff - A Configuration File Diff Tool

gendiff is a tool for easily comparing configuration files and displaying the differences between them in various formats. With gendiff, you can:

- Get diffs in different formats: from the human-readable stylish format to the simple plain format, and even json.
- Work with different file types, supporting YAML and JSON formats.
- Easily integrate with other tools and scripts for automatic configuration comparisons.

## Features:
- Simple command-line interface.
- Support for extendable output formats.
- Comparison of nested data structures.
- Suitable for working with any type of configuration or data files.

## Supported Output Formats:
- *Stylish*: Beautiful and human-readable output.
- *Plain*: Simple text-based output.
- *JSON*: Output in JSON format for integration with other tools.

# Installation Guide for gendiff

Follow the steps below to set up and install the gendiff project on your local machine.

## 1. Clone the Repository

Start by cloning the repository from GitHub:

```bash
git clone https://github.com/Ilia-Ivankov/python-project-50.git
```
## 2. Installation

Navigate into the project directory and install the required dependencies:

```bash
cd python-project-50
```
```bash
make install
```

This command will install all necessary dependencies listed in the project

## 3. Build the Project

Once the dependencies are installed, build the project using the following command:

```bash
make build
```

This will prepare the project for further steps and ensure everything is compiled correctly.

## 4. Publish the project

After building the project, you can publish it using the command below:

```bash
make publish
```

Publishing will prepare the project for deployment.

## 5. Install the Package Locally

Finally, install the package on your local machine by running:

```bash
make package-install
```

This will install the package locally, allowing you to use the `gendiff` tool directly on your machine

## 6. Run the Tool

After completing the above steps, you can run the `gendiff` tool locally and start using it by running:

```bash
gendiff -f <format> <first_file> <second_file>
```

Replace `<first_file>`, `<second_file>`, and `<format>` with the appropriate file paths and desired output format (such as `stylish`, `plain`, or `json`).

# Examples of the Output

Difference between two plain json files:

[![asciicast](https://asciinema.org/a/uDhEm8fX0HnP6eTWLBSPIRNxJ.svg)](https://asciinema.org/a/uDhEm8fX0HnP6eTWLBSPIRNxJ)

Difference between two plain yaml files:

[![asciicast](https://asciinema.org/a/NZgAGXX3i4Cpt98GWATrYTkRp.svg)](https://asciinema.org/a/NZgAGXX3i4Cpt98GWATrYTkRp)

Difference between two nested files:

[![asciicast](https://asciinema.org/a/4c0zQdh1g4UYlMcWM0uknCQmo.svg)](https://asciinema.org/a/4c0zQdh1g4UYlMcWM0uknCQmo)

Plain difference between two nested files:

[![asciicast](https://asciinema.org/a/83K2v4zM2cwMe3xxUQf4rje00.svg)](https://asciinema.org/a/83K2v4zM2cwMe3xxUQf4rje00)

Json difference between two nested files:

[![asciicast](https://asciinema.org/a/8bpzcpraRU6yUV5CSjW3ZAqkU.svg)](https://asciinema.org/a/8bpzcpraRU6yUV5CSjW3ZAqkU)
