# NumberAnalyzer

A Python script that analyzes a list of integers from a file to:
- Identify prime numbers.
- Count distinct factors for each number.
- Calculate the Least Common Multiple (LCM) of all numbers using the Euclidean algorithm.

---

## Features
- Reads integers from a `numbers.txt` file.
- Finds prime numbers in the input list.
- Computes the number of distinct factors for each integer.
- Calculates the LCM of all numbers using `functools.reduce` and GCD.
- Includes error handling for invalid inputs, empty files, or missing files.

---

## Requirements
- Python 3.x
- Standard library modules: `functools`, `typing`

---

## Usage
1. Create a `numbers.txt` file in the same directory as the script.
2. Add one integer per line in `numbers.txt`. Example:
   ```
   10
   25
   13
   6
   ```

---

3. Run the script:
   ```bash
   python main.py
   ```
4. The script outputs:
   - List of numbers from the file.
   - Prime numbers in the list.
   - Count of distinct factors for each number.
   - LCM of all numbers.

---

## Example Output
For `numbers.txt` containing:
```
10
25
13
6
```

---
Running the script produces:
```
Numbers in file: [10, 25, 13, 6]
Prime numbers: [13]
Factors count
- 10 has 4
- 25 has 3
- 13 has 2
- 6 has 4
LCM of all numbers: 1950
```
---

## Error Handling
- If `numbers.txt` is missing: `Error: numbers.txt file not found`.
- If the file is empty or contains no valid numbers: `Error: File is empty or contains no valid numbers`.
- If negative or zero numbers are included: `Error: File contains negative or zero numbers`.

---

## File Structure
```
NumberAnalyzer/
├── main.py
├── numbers.txt
└── README.md
```

---

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/muhammadhunzalaarshad/NumberAnalyzer.git
   
   ```
2. Navigate to the project directory:
   ```bash
   cd NumberAnalyzer
   ```
3. Create and populate `numbers.txt` with integers.
4. Run the script as described in the Usage section.

---

## Contributing
Contributions are welcome! Please submit issues or pull requests for bug fixes or enhancements.

---

## License
This project is licensed under the MIT License.