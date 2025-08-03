# Use the official Python image as the base image
FROM python:3.10-slim

ARG VERSION
ENV APP_VERSION=$VERSION


# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the FastAPI app files into the container
COPY . .

# Expose the port that FastAPI runs on
EXPOSE 8000

# Run migrations and start the app
CMD ["bash", "-c", "alembic upgrade head && python -m src.console setup-openai-assistants && python -m src.main"]
