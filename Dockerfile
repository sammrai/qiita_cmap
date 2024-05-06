FROM node:18-slim
WORKDIR /qiita

#qiita-cliのインストール
RUN npm install @qiita/qiita-cli --save-dev
RUN npx qiita version
RUN npm install @qiita/qiita-cli@latest
RUN npx qiita init

#ポートフォワーディングを用いてdockerコンテナ名で名前解決
RUN sed -e "s/localhost/qiita/g" -i /qiita/node_modules/@qiita/qiita-cli/dist/server/app.js

EXPOSE 8888