FROM agrigorev/zoomcamp-bees-wasps:v2

RUN pip install keras-image-helper
#RUN pip install https://github.com/alexeygrigorev/tflite-aws-lambda/raw/main/tflite/tflite_runtime-2.7.0-cp39-cp39-linux_x86_64.whl
RUN pip install https://github.com/alexeygrigorev/tflite-aws-lambda/raw/main/tflite/tflite_runtime-2.14.0-cp310-cp310-linux_x86_64.whl
COPY homework-9.py .
ENV MODEL_NAME=bees-wasps-v2.tflite

CMD [ "homework-9.lambda_handler" ]