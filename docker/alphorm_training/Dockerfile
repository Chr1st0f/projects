FROM centos
MAINTAINER totof <totof@axalp.fr>
RUN yum install -y net-tools \
echo "<h2>Bienvenu sur la formation Docker sur Alphorm<h2>" > /usr/share/httpd/noindex/index.html
EXPOSE 80
CMD ["-D","FOREGROUND"]
ENTRYPOINT ["/usr/sbin/httpd"]
