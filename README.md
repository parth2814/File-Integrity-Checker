# File System Integrity Checker

This Python-based tool monitors and reports changes in a specified directory structure. It creates a baseline of file states and compares the current state of the file system against this baseline to detect modifications, additions, or deletions.

## Features

- Create a baseline snapshot of a directory structure
- Detect new, modified, and deleted files
- Generate human-readable reports of changes
- Command-line interface for easy use and integration

## Requirements

- Python 3.6 or higher

## Installation

1. Clone this repository or download the source files:
   - `baseline_creator.py`
   - `run_check.py`
   - `reporting.py`
   - `main.py`

2. Ensure all files are in the same directory.

## Usage

### Create a Baseline

To create an initial baseline of a directory:
python main.py /path/to/directory --create-baseline
Copy
This will generate a `baseline.json` file in the current directory.

### Run an Integrity Check

To check for changes against the baseline:
python main.py /path/to/directory
Copy
This will display a report of any new, modified, or deleted files since the baseline was created.

### Additional Options

- Specify a custom baseline file:
python main.py /path/to/directory --baseline-file /path/to/custom_baseline.json
Copy
- For help and to see all available options:
python main.py --help
Copy
## Example

1. Create a baseline:
python main.py C:\Users\YourUsername\Documents --create-baseline
Copy
2. Run an integrity check:
python main.py C:\Users\YourUsername\Documents
Copy
## Extending the Tool

The modular design allows for easy extensions:
- Add email notifications for changes
- Implement scheduled checks
- Integrate with logging systems

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).
