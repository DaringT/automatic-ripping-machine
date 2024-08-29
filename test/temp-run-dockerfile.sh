docker build -t arm-ripper . &&\
   docker run -p "8080:8080" \
   -e ARM_UID="1001" \
   -e ARM_GID="1001" \
   -v "/home/arm:/home/arm" \
   -v "/home/arm/Music:/home/arm/Music" \
   -v "/home/arm/logs:/home/arm/logs" \
   -v "/home/arm/media:/home/arm/media" \
   -v "/home/arm/config:/etc/arm/config" \
   --device=/dev/sr0:/dev/sr0 \
   --privileged \
   --restart "always" \
   --name "arm-ripper"