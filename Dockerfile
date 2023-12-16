# Use a lightweight base image
FROM python:3.8-slim-buster

# Set the working directory
WORKDIR /service

# Copy only the requirements file first to leverage Docker caching
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy the entire application code
COPY . ./

# Expose the port that Streamlit will run on
EXPOSE 8501

# Set the command to run the application
CMD ["streamlit", "run", "app.py"]
