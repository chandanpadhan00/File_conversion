import fitz  # PyMuPDF

def extract_section(input_pdf, chapter_number):
    # Open the PDF file
    pdf_document = fitz.open(input_pdf)

    # Iterate through each page and search for the chapter start
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        text = page.get_text()

        # Example logic to find chapter 2 start
        if f"Chapter {chapter_number}" in text:
            # Example logic to find end of chapter 2
            end_index = text.find("Chapter ", text.find(f"Chapter {chapter_number + 1}"))

            # Extract the section
            section_text = text[text.find(f"Chapter {chapter_number}") : end_index]

            # Create a new PDF with this section
            new_pdf = fitz.open()
            new_page = new_pdf.new_page()
            new_page.insert_text((50, 50), section_text)
            new_pdf.save(f"chapter_{chapter_number}_section.pdf")
            new_pdf.close()

            break

    pdf_document.close()

# Usage example
extract_section("your_input.pdf", 2)