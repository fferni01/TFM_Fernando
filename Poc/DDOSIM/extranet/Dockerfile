#Fernando Fernández Iglesias

FROM ubuntu:20.04
ENV TZ=Europe/Madrid

RUN apt-get update && apt-get install -y tzdata g++

RUN apt-get install -y openssh-server net-tools iputils-ping traceroute vim nano iproute2 iptables pkg-config nmap tcpdump libpcap-dev autoconf gcc make automake git

RUN wget http://launchpadlibrarian.net/1315573/libnet0-dev_1.0.2a-7_amd64.deb
RUN wget http://launchpadlibrarian.net/1315572/libnet0_1.0.2a-7_amd64.deb
RUN  dpkg -i libnet0_1.0.2a-7_amd64.deb
RUN  dpkg -i libnet0-dev_1.0.2a-7_amd64.deb

#RUN git clone https://github.com/alanackart/DDOSIM.git

#RUN cd DDOSIM && chmod +x configure && ./configure && make && make install


RUN mkdir /var/run/sshd
RUN echo 'root:root' |chpasswd
RUN sed -ri 's/^#?PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config
RUN mkdir /root/.ssh

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

EXPOSE 22
EXPOSE 80
COPY ./start.sh .
COPY ddosim-0.2.tar.gz .
RUN tar -xvf ddosim-0.2.tar.gz
RUN cd ddosim-0.2 && ./configure && make && make install
RUN chmod +x start.sh

CMD ["./start.sh"]
