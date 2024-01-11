FROM python:3-slim-buster

RUN mkdir /code

# Set the working directory inside the container
WORKDIR /code

# Copy the requirements.txt file into the container at /code
COPY ./requirements.txt /code/requirements.txt

# Install Python dependencies from requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy the entire src directory into the container at /code/src
COPY ./src /code/src

# Set the default command to run the FastAPI application using uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

