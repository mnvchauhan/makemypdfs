import requests
import io

print("Testing compress endpoint...")
url = "http://localhost:8003/api/compress"
files = {'pdf_files': ('test.pdf', b'%PDF-1.4\n1 0 obj <</Type /Catalog>> endobj', 'application/pdf')}
data = {'compression_level': 'extreme'}

try:
    response = requests.post(url, files=files, data=data)
    print("Status Code:", response.status_code)
    print("Response text:", response.text)
except Exception as e:
    print("Error:", e)
