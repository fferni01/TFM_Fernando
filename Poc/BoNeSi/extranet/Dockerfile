#Fernando Fernández Iglesias

FROM ubuntu:18.04

RUN apt-get update 

RUN apt-get install -y openssh-server net-tools iputils-ping traceroute vim nano iproute2 iptables pkg-config nmap tcpdump
RUN apt-get update && apt-get install -y git
RUN apt-get install -y libpcap-dev 
RUN apt-get install -y libnet-dev
RUN apt-get install -y autoconf
RUN apt-get install -y gcc
RUN apt-get install -y make
RUN apt-get install -y automake
#RUN apt-get install -y apache2  
RUN git clone https://github.com/Markus-Go/bonesi.git

RUN cd bonesi && autoreconf -f -i && ./configure && make && make install

RUN mkdir /var/run/sshd
RUN echo 'root:root' |chpasswd
RUN sed -ri 's/^#?PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config
RUN mkdir /root/.ssh

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

EXPOSE 22
EXPOSE 80
COPY ./start.sh .

RUN chmod +x start.sh

CMD ["./start.sh"]
