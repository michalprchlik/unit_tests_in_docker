FROM alpine
RUN apk update && apk upgrade && apk add bash
COPY countdown.sh .
CMD ["countdown.sh"]
ENTRYPOINT ["bash"]