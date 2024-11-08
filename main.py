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
  html_file_path = "n.html"
  html_with_stamp =  html + datetime.today().strftime('%d-%m-%Y')

  # Now you can write the concatenated HTML content to a file if needed
  with open(html_file_path, "w", encoding="utf-8") as html_file:
    html_file.write(html_with_stamp)
    print("HTML saved successfully!")

  HTML(string=html_with_stamp).write_pdf(output_file)
  print("PDF saved successfully!")

# AI APIKey: Google Gemini
genai.configure(api_key = os.getenv('GOOGLE_GEMINI_API'))
model = genai.GenerativeModel('gemini-pro')

# Recursion Prompt to make use of n-iteration
prompt="Generate an enhanced version (in chinese) of the provided resume in Markdown format, incorporating industry-specific research and maintaining the content in the same language. (do not restat the title, keep the experiences the same but improve the expression of the skills and knowledge gained in the different fields)"

n=10

def QNP(input_file,output_file,i): #Question N' Print --> NPQ
  with open(input_file, 'r') as f:
    markdown_text = f.read()
  md2pdf(input_file,output_file)
  response = model.generate_content(prompt+markdown_text)
  aimd="ai"+str(i+1)+".md"
  with open(aimd, "w", encoding="utf-8") as aimd_file:
    aimd_file.write(response.text)
  print("AI-revision saved successfully!")
  

for i in range(n):
  if i==0:
    with open("resume.md", 'r') as f:
      markdown_text = f.read()
    QNP("resume.md", "resumetxt-ai"+str(i)+".pdf",i)
  else:
    QNP("ai"+str(i)+".md", "resumetxt-ai"+str(i)+".pdf",i)




