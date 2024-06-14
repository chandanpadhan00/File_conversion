import fitz
import os
import sys

def extract_pages(input_file, page_range, output_file):
    try:
        # Check if the input file exists
        if not os.path.isfile(input_file):
            raise FileNotFoundError(f"Input file '{input_file}' not found.")

        doc = fitz.open(input_file)
        output = fitz.open()

        # Extract pages based on the range provided
        try:
            start, end = map(int, page_range.split('-'))
        except ValueError:
            raise ValueError("Invalid page range format. Use 'start-end' (e.g., 10-15).")

        if start < 1 or end > doc.page_count:
            raise IndexError(f"Page range '{page_range}' is out of bounds for the input PDF.")

        for page_num in range(start - 1, end):  # fitz uses 0-based indexing
            output.insert_pdf(doc, from_page=page_num, to_page=page_num)

        # Save the extracted pages to a new PDF file
        output.save(output_file)
        print(f"Pages {page_range} extracted from '{input_file}' to '{output_file}' successfully.")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)  # Exit with a non-zero status code to indicate failure

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <input_file> <page_range> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    page_range = sys.argv[2]
    output_file = sys.argv[3]

    extract_pages(input_file, page_range, output_file)