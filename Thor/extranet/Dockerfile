#Fernando Fernández Iglesias

FROM ubuntu:18.04

RUN apt-get update && apt-get install -y openssh-server net-tools iputils-ping traceroute vim nano iproute2 iptables pkg-config nmap tcpdump libpcap-dev libnet-dev autoconf gcc make automake git python2.7 python

RUN git clone https://github.com/dotfighter/torshammer.git

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
RUN sed -i -e 's/\r$//' ./start.sh
CMD ["./start.sh"]
