import os
import django
from django.conf import settings
from django.http import HttpRequest
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'makemypdfs.settings')
django.setup()

from tools.views import process_organize_pdf
from django.core.files.uploadedfile import SimpleUploadedFile

with open("test2.py", "rb") as f:
    # Just creating a fake PDF stream, though it's actually test2.py (will fail fitz)
    # Let's create a real dummy PDF first.
    pass

import fitz
doc = fitz.open()
doc.new_page()
doc.save("test.pdf")
doc.close()

with open("test.pdf", "rb") as f:
    pdf_file = SimpleUploadedFile("test.pdf", f.read(), content_type="application/pdf")

request = HttpRequest()
request.method = 'POST'
request.FILES['pdf_files'] = pdf_file
request.POST['page_data'] = '[{"page": "1", "rotation": "0"}]'

print("Calling process_organize_pdf...")
response = process_organize_pdf(request)
print("Response Status Code:", response.status_code)
print("Response Content:", response.content)
