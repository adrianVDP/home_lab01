# imagine AWS oficială pentru Lambda Python 3.11
FROM public.ecr.aws/lambda/python:3.11

# dependențe (dacă apar ulterior)
# COPY app/requirements.txt  .
# RUN pip install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

# codul aplicației
COPY app ${LAMBDA_TASK_ROOT}/app

# entrypoint: modulul.funcția
CMD ["app.src.handler.handler"]
