# Sử dụng Python làm môi trường nền
FROM python:3.9-slim

# Thiết lập thư mục làm việc
WORKDIR /app

# Copy file từ thư mục local vào container
COPY app.py .

# Cài đặt Flask
RUN pip install flask

# Expose cổng 5000
EXPOSE 5000

# Chạy ứng dụng
CMD ["python", "app.py"]
