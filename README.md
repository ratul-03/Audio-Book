# Audio Book Reader using pyttsx3 and PyPDF2

This project reads out the text from a PDF file using the `pyttsx3` text-to-speech library and `PyPDF2` for PDF handling. The script processes the PDF from the 8th page to the end and reads each page's text out loud.

## Features

- Reads text from a PDF file.
- Uses text-to-speech to vocalize the content.
- Iterates from the 8th page to the last page.

## Requirements

- Python 3.x
- pyttsx3
- PyPDF2

## Installation

1. Install Python 3.x from the official website: [Python.org](https://www.python.org/).
2. Install the required libraries using pip:

   ```sh
   pip install pyttsx3 PyPDF2
   ```
## Usage
- Clone this repository or download the script file.
- Place the Atomic-Habits.pdf file in the same directory as the script.
- Run the script:
```sh
python main.py
```
## Code Explanation
The main script main.py includes:
```python
import pyttsx3
import PyPDF2

book = open('Atomic-Habits.pdf', 'rb')
reader = PyPDF2.PdfReader(book)
pages = len(reader.pages)

for num in range(7, pages):
    friend = pyttsx3.init()
    page = reader.pages[num]  # Accessing the 8th page (index starts at 0)
    text = page.extract_text()
    friend.say(text)
    friend.runAndWait()

print(pages)

```

## Contributing
Feel free to fork this repository and contribute by submitting a pull request. Any improvements or new features are welcome!

## License
This project is licensed under the MIT License.
