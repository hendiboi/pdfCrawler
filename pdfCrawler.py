import PyPDF2

def crawl_pdf(pdf_file_path):
    # Open the PDF file in read-binary mode
    with open(pdf_file_path, 'rb') as file:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(file)

        # Get the number of pages in the PDF
        num_pages = len(pdf_reader.pages)

        # Extract text from each page
        for page_num in range(num_pages):
            # Get the page object
            page = pdf_reader.pages[page_num]

            # Extract text from the page
            page_text = page.extract_text()

            # Process or store the extracted text as needed
            print(f"Page {page_num + 1}:")
            print(page_text)
            print("---")

# Specify the path to the PDF file you want to crawl
pdf_file_path = '/Users/hendiboi/Downloads/PLAW-117publ169.pdf'

# Call the crawl_pdf function with the specified PDF file path
crawl_pdf(pdf_file_path)