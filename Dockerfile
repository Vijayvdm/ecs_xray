FROM public.ecr.aws/lambda/python:3.9

RUN yum install -y python3-pip
COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY app.py .
CMD ["python3", "app.py"]
