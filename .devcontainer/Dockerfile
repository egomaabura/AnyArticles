# 使用するイメージ
FROM python:3.11

# 環境変数PYTHONUNBUFFEREDを1に設定します。
# これにより、Pythonの出力がバッファリングされず、コンソールに直接表示されるようになります。
# これは、Dockerコンテナのログをリアルタイムで見るのに役立ちます。
ENV PYTHONUNBUFFERED 1

# コンテナ立ち上げ時に走らせるコマンド
RUN apt-get update \
    && apt-get install -y default-mysql-client \
    && rm -rf /var/lib/apt/lists/*
RUN pip install --upgrade pip
RUN pip install django
RUN pip install djangorestframework
RUN pip install mysqlclient
