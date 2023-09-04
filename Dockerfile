# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.10-slim
# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
# CMD ["%%CMD%%"]
ENV PYTHONDONTWRITEBYTECODE=1
# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1
#RUN git clone https://github.com/gothinkster/django-realworld-example-app.git /drf_src
# Set the working directory to /drf
# NOTE: all the directives that follow in the Dockerfile will be executed in
# that directory.

RUN mkdir /OIApps
WORKDIR /OIApps
#COPY . /C
COPY requirements.txt /OIApps/
RUN pip install -r requirements.txt

#COPY *.* /OIApps
COPY /OIApps /OIApps
#RUN ls -lR /
RUN ls .
# Set the working directory to /drf
# NOTE: all the directives that follow in the Dockerfile will be executed in
# that directory.
# Install any needed packages specified in requirements.txt
#COPY requirements.txt .
##RUN python -m pip install -r requirements.txt
VOLUME /OIApps
EXPOSE 8080
# Install pip requirements
# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
#RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
#USER appuser
CMD python /OIApps/manage.py makemigrations && python /OIApps/manage.py migrate && python /OIApps/manage.py runserver 0.0.0.0:8000

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
#CMD ["gunicorn", "--bind", "0.0.0.0:8000", "OIApps.wsgi"]
