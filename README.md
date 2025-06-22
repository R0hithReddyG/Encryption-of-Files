# AES File and Directory Encryption Utility

This repository provides **AEScrypter**, a Python utility for encrypting individual files and entire directories using AES encryption in Cipher Feedback (CFB) mode. The script encrypts plaintext files into secure binary outputs with minimal configuration.

---

## Features

1. **Single-File Encryption**

   * Encrypt a specified file and generate a corresponding `.bin` output file.

2. **Recursive Directory Encryption**

   * Traverse a directory and its subdirectories, encrypting every file encountered.

3. **AES-CFB Mode**

   * Utilizes Cipher Feedback mode for streaming encryption without requiring padding.

4. **Initialization Vector (IV) Management**

   * Automatically generates a unique 16-byte IV for each encryption operation and prepends it to the encrypted output.

---

## Prerequisites

* **Python 3.6 or later**
* **pycryptodomex** library

  ```bash
  pip install pycryptodomex
  ```

---

## Usage

Execute the script with the path to a file or directory as an argument:

```bash
python encrypt.py <path_to_file_or_directory>
```

* `<path_to_file>`: Encrypts the specified file and creates `<filename>.bin`.
* `<path_to_directory>`: Recursively encrypts all files within the directory.

---

## Examples

* **Encrypt a single file**

  ```bash
  python encrypt.py confidential_report.pdf
  # Output: confidential_report.pdf.bin
  ```

* **Encrypt all files in a directory**

  ```bash
  python encrypt.py /path/to/project_folder
  # Outputs: file1.txt.bin, file2.jpg.bin, etc.
  ```

---

## Implementation Details

1. The script reads the target file in binary mode.
2. It uses a hard-coded 16-byte key (`b'this is a 16 key'`) by default; a secure key should be supplied in production.
3. A 16-byte random IV is generated for each encryption operation.
4. AES cipher is initialized in CFB mode with the chosen key and IV.
5. The IV is prepended to the encrypted ciphertext and written to a new file with the `.bin` extension.

To enhance security, replace the default key handling with a secure key management approach, such as retrieving the key from an environment variable or a key vault.

---

## License

This project is released under the MIT License. You are free to use, modify, and distribute this software, provided that the original license and copyright notice are retained.

---

## Contributing

Contributions are welcome. Please submit pull requests or open issues for feature requests and bug reports.
