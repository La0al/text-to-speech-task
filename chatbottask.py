import google.generativeai as genai


GOOGLE_API_KEY = 'Your API Key'
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')  

def ask_gemini(question):
  response = model.generate_content(question)
  response.resolve()
  return response.text