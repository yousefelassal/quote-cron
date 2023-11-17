FROM python:3.9

WORKDIR /app

COPY update_readme.py .

RUN pip install requests

CMD ["python", "update_readme.py"]
