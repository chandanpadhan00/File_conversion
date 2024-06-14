import fitz  # PyMuPDF

def extract_section(input_pdf):
    pdf_document = fitz.open(input_pdf)
    
    # Initialize variables to track start and end of section
    start_index = -1
    end_index = -1
    
    # Iterate through each page and search for the section
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        text = page.get_text()
        
        # Look for the start of Chapter 2 section
        if "All departments of India" in text:
            start_index = text.find("All departments of India")
        
        # Look for the end of Chapter 2 section
        if "we will read in next chapter" in text:
            end_index = text.find("we will read in next chapter")
            break  # Stop searching once found
        
    # Extract the section based on start and end indexes
    if start_index != -1 and end_index != -1:
        section_text = text[start_index:end_index]
        
        # Create a new PDF with this section
        new_pdf = fitz.open()
        new_page = new_pdf.new_page()
        new_page.insert_text((50, 50), section_text)
        new_pdf.save("chapter_2_section.pdf")
        new_pdf.close()
        
    else:
        print("Section not found in the PDF.")
    
    pdf_document.close()

# Usage example
extract_section("your_input.pdf")