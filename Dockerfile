FROM nicobartok0/final2023:latest

RUN apt update && apt install -y python3

CMD ["python3","/my_test.py"]
