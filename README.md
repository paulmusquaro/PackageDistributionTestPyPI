# PackageDistributionTestPyPI

## Overview
The **Clean Folder** package is a Python utility designed to organize files in a specified directory by sorting them into categorized folders based on file extensions. The tool also normalizes file names, converting Cyrillic characters into Latin and replacing non-alphanumeric symbols with underscores.

## Features
- Automatically sorts files into folders: `images`, `videos`, `documents`, `music`, and `archives`.
- Normalizes file names to avoid special character issues.
- Unpacks archive files (`.zip`, `.gz`, `.tar`) into separate folders.
- Works recursively within subfolders.

## Installation
This package is distributed via **TestPyPI**. To install it, use the following command:

```sh
pip install -i https://test.pypi.org/simple/ clean-folder # the package is not available yet
```

## Usage
Once installed, you can use the `clean_folder` command to organize a specified directory.

### Command-line usage:
```sh
clean_folder /path/to/directory
```

Alternatively, you can run the script manually:

```sh
python -m clean_folder.clean /path/to/directory
```

## Example
Before running the script:
```
my_folder/
  photo1.jpeg
  document1.pdf
  song.mp3
  archive.zip
```

After running:
```
my_folder/
  images/
    photo1.jpeg
  documents/
    document1.pdf
  music/
    song.mp3
  archives/
    archive/
      (unpacked files)
```

## Development & Contribution
If you’d like to contribute, feel free to clone the repository and submit pull requests.

```sh
git clone https://github.com/paulmusquaro/PackageDistributionTestPyPI.git
cd PackageDistributionTestPyPI
```

## License
This project is licensed under the MIT License.


