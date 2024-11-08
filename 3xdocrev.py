from markdown2 import markdown as mdeee
from weasyprint import HTML
from datetime import datetime
from dotenv import load_dotenv
import os
import google.generativeai as genai


def md2pdf(input_file, output_file):

  with open(input_file, 'r') as f:
    markdown_text = f.read()
    html = mdeee(markdown_text)

  # Specify the file path where you want to save the HTML file
  html_file_path = "resume.html"
  html_with_stamp =  html + datetime.today().strftime('%d-%m-%Y')

  # Now you can write the concatenated HTML content to a file if needed
  with open(html_file_path, "w", encoding="utf-8") as html_file:
    html_file.write(html_with_stamp)
    print("HTML saved successfully!")

  HTML(string=html_with_stamp).write_pdf(output_file)
  print("PDF saved successfully!")

# AI Part

genai.configure(api_key = os.getenv('GOOGLE_GEMINI_API'))

model = genai.GenerativeModel('gemini-pro')

prompt="Generate an enhanced version of the provided resume in Markdown format, incorporating industry-specific research and maintaining the content in the same language. (do not restat the title, keep the experiences the same but improve the expression of the skills and knowledge gained in the different fields)"

with open("resume.md", 'r') as f:
  markdown_text = f.read()
  
response = model.generate_content(prompt+markdown_text)

response2 = model.generate_content(prompt+response.text)

response3 = model.generate_content(prompt+response2.text)
  
md2pdf('resume.md','resumetxt.pdf')


aimd="ai.md"
with open(aimd, "w", encoding="utf-8") as aimd_file:
  aimd_file.write(response2.text)
print("AI-revised CV saved successfully!")

aimd2="ai2.md"
with open(aimd2, "w", encoding="utf-8") as aimd_file:
  aimd_file.write(response3.text)
print("AI-revised CV saved successfully!")

md2pdf("ai.md",'resumetxt-ai.pdf')
md2pdf("ai2.md",'resumetxt-ai2.pdf')



