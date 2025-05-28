
import google.generativeai as genai

genai.configure(api_key="AIzaSyDTY_KL65CsXfcRgBkN1SRA8Yu5kQOxE9g")

for m in genai.list_models():
    print(m.name, "=>", m.supported_generation_methods)
    