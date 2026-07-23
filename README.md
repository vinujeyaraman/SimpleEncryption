# Caesar Cipher in Python

A simple yet complete Python implementation of the **Caesar Cipher**, one of the oldest and most well-known encryption techniques. This program allows users to both **encode** (encrypt) and **decode** (decrypt) messages using any integer key while preserving uppercase letters, lowercase letters, numbers, spaces, and special characters.

---

## Features

- Encrypt plain text using the Caesar Cipher
- Decrypt encrypted text
- Supports both uppercase (`A-Z`) and lowercase (`a-z`) letters
- Preserves spaces, numbers, and special characters
- Accepts integer keys of any size
- Uses modular arithmetic (`% 26`) to wrap around the alphabet
- Simple command-line interface

---

## How It Works

The Caesar Cipher shifts each alphabetic character by a fixed number of positions.

For example, with a key of **3**:

| Original | Encrypted |
|----------|-----------|
| A | D |
| B | E |
| X | A |
| Y | B |
| Z | C |

Non-alphabetic characters such as spaces, punctuation, and numbers remain unchanged.

---

## Requirements

- Python 3.x

No external libraries are required.

---

## Usage

Run the program:

```bash
python caesar_cipher.py
```

The program will ask for:

1. The cipher key
2. The input text
3. Whether to encode or decode

Example:

```
Enter the key: 5
Enter the original string or cypher: Hello World
Enter if you want to encode or decode the cypher (1 to encode and 0 to decode): 0
```

Output:

```
Mjqqt Btwqi
```

---

## Example

### Encoding

Input

```
Key: 5
Text: Code
```

Output

```
Htij
```

---

### Decoding

Input

```
Key: 5
Cipher: Htij
```

Output

```
Code
```

---

## Project Structure

```
.
├── caesar_cipher.py
├── README.md
└── LICENSE
```

---

## Algorithm

### Encoding

For uppercase letters:

```
Encrypted = ((Letter - 'A' + Key) % 26) + 'A'
```

For lowercase letters:

```
Encrypted = ((Letter - 'a' + Key) % 26) + 'a'
```

### Decoding

For uppercase letters:

```
Decrypted = ((Letter - 'A' - Key) % 26) + 'A'
```

For lowercase letters:

```
Decrypted = ((Letter - 'a' - Key) % 26) + 'a'
```

---

## Future Improvements

- Graphical User Interface (GUI)
- File encryption and decryption
- Support for custom alphabets
- Brute-force Caesar Cipher cracker
- Frequency analysis tool
- Save encrypted/decrypted output to a file

---

## Learning Outcomes

This project demonstrates:

- Python string manipulation
- ASCII values using `ord()` and `chr()`
- Conditional statements
- Loops
- Modular arithmetic
- Basic cryptography concepts
- User input handling

---

## License

This project is licensed under the MIT License.

---

## Author

Developed as a beginner-friendly Python project to demonstrate the implementation of the classical Caesar Cipher encryption algorithm.
