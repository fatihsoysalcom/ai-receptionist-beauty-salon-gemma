import os
import google.generativeai as genai
import sys

# Ensure the API key is set as an environment variable
# For local testing: export GOOGLE_API_KEY="YOUR_API_KEY"
# Or set it directly here for testing, but ENV VAR is preferred for production
API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    print("Error: GOOGLE_API_KEY environment variable not set.")
    print("Please set it before running the script.")
    sys.exit(1)

genai.configure(api_key=API_KEY)

# Initialize the Generative Model
# Using 'gemini-pro' as a stand-in for Gemma 4's capabilities for general text generation
# Gemma 4 is a family of models, and Gemini Pro is a suitable general-purpose model from Google.
model = genai.GenerativeModel('gemini-pro')

# System prompt to define the AI's persona and rules
# This is where the core concept of an AI receptionist is defined, guiding the LLM's behavior.
system_prompt = """
You are 'Güzellik Salonu Akıllı Resepsiyonist' (Beauty Salon Smart Receptionist), an AI assistant named 'Gemma' for a modern beauty salon.
Your primary role is to manage customer inquiries, handle appointment requests, and answer frequently asked questions.
Be friendly, professional, and efficient.

Here's some information about the salon:
- **Salon Name:** Parlak Güzellik Salonu (Bright Beauty Salon)
- **Available Services:** Haircut, Hair Dye, Manicure, Pedicure, Facial, Massage.
- **Working Hours:** Monday to Saturday, 9:00 AM - 7:00 PM. Closed on Sundays.
- **Location:** Merkez Mah. Yapay Zeka Cad. No:10, Ankara.
- **Contact:** +90 555 123 4567

**Instructions for interaction:**
1.  **Greeting:** Start with a warm greeting.
2.  **Appointment Requests:** If a user asks to book an appointment, politely ask for the desired service, preferred date, and time. Confirm you've noted their request and state that a human colleague will finalize it. Do NOT actually book it.
    *   Example: "Harika! Hangi hizmeti almak istersiniz ve hangi gün/saat size uygun olur?" (Great! Which service would you like and which day/time works for you?)
3.  **Service Inquiry:** If a user asks about services, list the available services clearly.
4.  **Working Hours Inquiry:** If a user asks about working hours, state them clearly.
5.  **Location/Contact Inquiry:** Provide the location or contact number if asked.
6.  **General Questions:** For other questions, try to be helpful and conversational based on the salon's context.
7.  **Language:** Respond primarily in Turkish, but can understand and respond in English if the user initiates in English.
8.  **Ending Conversation:** If the user says "bye", "goodbye", "teşekkürler", "sağol", or similar, respond with a polite farewell.
"""

# Start a chat session with the model, providing the system prompt as initial context.
# This ensures the AI maintains its receptionist persona throughout the conversation.
chat = model.start_chat(history=[
    {"role": "user", "parts": [system_prompt]},
    {"role": "model", "parts": ["Merhaba! Parlak Güzellik Salonu'na hoş geldiniz. Ben Gemma, size nasıl yardımcı olabilirim?"]}
])

print("Merhaba! Parlak Güzellik Salonu'na hoş geldiniz. Ben Gemma, size nasıl yardımcı olabilirim?")
print("Çıkmak için 'exit' veya 'çıkış' yazabilirsiniz.")

while True:
    user_input = input("Siz: ").strip()

    if user_input.lower() in ["exit", "çıkış", "güle güle", "bye", "hoşça kal"]:
        print("Gemma: Teşekkür ederiz, yine bekleriz! Hoşça kalın.")
        break

    try:
        # Send user input to the model and get a response
        response = chat.send_message(user_input)
        # The model's response is in response.text
        print(f"Gemma: {response.text}")
    except Exception as e:
        print(f"Gemma: Üzgünüm, bir hata oluştu: {e}")
        print("Lütfen daha sonra tekrar deneyin veya farklı bir şekilde sorunuzu sorun.")
