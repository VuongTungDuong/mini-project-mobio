FROM BE_BASE_COMPILE_IMAGE as compile-image

WORKDIR /home/mobio/projects/jo
ADD . /home/mobio/projects/jo

RUN pip3.8 install -r requirements.txt

FROM BE_BASE_RUN_IMAGE as run-image

ENV LC_ALL=en_US.UTF-8 \
   JO_HOME=/home/mobio/projects/jo \
   JO_FOLDER_NAME=jo \
   APPLICATION_DATA_DIR=/media/data/resources/ \
   APPLICATION_LOGS_DIR=/media/data/logs/daily/

ENV data_dir=$APPLICATION_DATA_DIR$JO_FOLDER_NAME \
   log_dir=$APPLICATION_LOGS_DIR$JO_FOLDER_NAME \
   monitor_log_dir=$APPLICATION_LOGS_DIR$JO_FOLDER_NAME/monitor_logs/

RUN mkdir -p $data_dir $log_dir $monitor_log_dir

WORKDIR $JO_HOME

COPY --from=compile-image $JO_HOME $JO_HOME

COPY --from=compile-image /usr/local/lib/python3.8/site-packages /usr/local/lib/python3.8/site-packages
COPY --from=compile-image /usr/local/bin/uwsgi /usr/local/bin/uwsgi

RUN chmod +x *.sh

CMD tail -f /dev/null