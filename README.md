# Load-balancing-with-Docker-nginx

Create three folder, one for nginx, and one for each app were you can put inside the same Docker and the same requirements

![image](https://user-images.githubusercontent.com/77585805/180436023-e8446004-f401-41b2-be39-c897c1563c16.png)


Docker for nginx:

FROM nginx<br />
RUN rm /etc/nginx/conf.d/default.conf<br />
COPY nginx.conf /etc/nginx/conf.d/default.conf<br />


