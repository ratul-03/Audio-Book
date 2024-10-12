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
