import PyPDF2
import json

pdf_data = {}

with open("File_handling/pdf_file_headling/sample.pdf", "rb") as file:
    reader = PyPDF2.PdfReader(file)

    for page_no, page in enumerate(reader.pages, start=1):
        pdf_data[f"page_{page_no}"] = page.extract_text()

# save as JSON
with open("output.json", "w", encoding="utf-8") as f:
    json.dump(pdf_data, f, indent=4, ensure_ascii=False)

print("Done ✅ PDF converted to Dictionary & JSON")

