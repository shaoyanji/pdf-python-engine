from markdown2 import markdown
from weasyprint import HTML
from datetime import datetime
from dotenv import load_dotenv
import os
import pathlib
import textwrap
import google.generativeai as genai

import vertexai
from vertexai.generative_models import GenerativeModel

genai.configure(api_key = os.getenv('GOOGLE_GEMINI_API'))

input_file = 'resume.md'

model = genai.GenerativeModel('gemini-pro')
##time
response = model.generate_content("analyze this .md file:"+input_file)

response2 = model.generate_content("apply those changes and rewrite the resume also in markdown:"+response.text)

print(response2.text)
  #############
#from fpdf import FPDF
#from PyPDF2 import PdfReader, PdfWriter, PdfFileReader, PdfFileWriter
#import pdfkit
#
#  def create_pdf_with_image(image_path, output_pdf):
#      # Create instance of FPDF class
#      pdf = FPDF()
#      # Add a page
#      pdf.add_page()
#    # Set font for the title
#      pdf.set_font("Arial", size = 12)
#      # Add title
#      pdf.cell(200, 10, txt = "", ln = True, align = 'C')
#      # Set coordinates to place the image at the upper right corner
#      pdf.image(image_path, x = pdf.w - 50, y = 10, w = 40)
#      # Save the PDF to the output file
#      pdf.output(output_pdf)
#  
#  def merge_pdfs(output_pdf, *pdfs_to_merge):
#      writer = PdfWriter()
#  
      # Merge PDFs
#      for pdf_path in #pdfs_to_merge:
#          reader = PdfReader(pdf_path)
#          for page in reader.pages:
#              writer.add_page(page)
  
      # Save the merged PDF to the output file
#      with open(output_pdf, 'wb') as #out_file:
#          writer.write(out_file)
####################################
# Get today's date

today_date = datetime.today().strftime('%d-%m-%Y')

input_file = 'resume.md'
outputtext_file = 'resumetxt.pdf'

with open(input_file, 'r') as f:
    markdown_text = f.read()

html = markdown(markdown_text)

header_file_path = "header.html"
with open(header_file_path, "r", encoding="utf-8") as header_file:
    header = header_file.read()

footer_file_path = "footer.html"
with open(footer_file_path, "r", encoding="utf-8") as footer_file:
    footer = footer_file.read()

# Specify the file path where you want to save the HTML file
html_file_path = "resume.html"

html_with_style = header + html + today_date + footer

# Now you can write the concatenated HTML content to a file if needed
with open(html_file_path, "w", encoding="utf-8") as html_file:
    html_file.write(html_with_style)

print("HTML saved successfully!")
  
HTML(string=html_with_style).write_pdf(outputtext_file)
print("PDF saved successfully!")

# Create PDF with image

  # Paths for image and output PDFs
#image_path = "image.jpg"
#pdf_with_image = "pdf_with_image.pdf"

  # Create the PDF with the image
#create_pdf_with_image(image_path, pdf_with_image)

  # Merge the PDFs
#merge_pdfs(output_file, pdf_with_image, outputtext_file)
  
#add_picture_to_pdf(outputtext_file, image_path, output_file)

#pdfkit.from_string(html_with_style, output_file)


