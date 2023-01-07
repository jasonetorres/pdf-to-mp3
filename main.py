import pdfreader, pyttsx3

pdfreader = pdfreader.PDFDocument(open('ViewPdfForm.pdf', 'rb'))
speaker = pyttsx3.init()

for page_num in range(pdfreader.numPages):
  text = pdfreader.getPage(page_num).extract_text()
  clean_text = text.script().replace('\n', '')
  print(clean_text)

speaker.save_to_file(clean_text, 'story.mp3')
speaker.runAndWait

speaker.stop()