import google.generativeai as genai

# Cấu hình API key
api_key = ""  # Thay YOUR_API_KEY bằng API key của bạn AIzaSyCY8rrMywCQTLoQZDYW-Z6mwpft9sLXTvY
genai.configure(api_key=api_key)

# Khởi tạo mô hình
model = genai.GenerativeModel('gemini-1.5-flash')

# Gửi câu hỏi và nhận phản hồi
question = "What is RAG ?"
response = model.generate_content(question)

# In ra câu trả lời
print("Câu trả lời từ API:", response.text)

