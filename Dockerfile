FROM python:3.8

WORKDIR /app

COPY update_readme.py .

RUN pip install requests python-frontmatter

CMD ["python", "update_readme.py"]
