# coding=utf-8

import dpkt

if __name__=="__main__":
	 with open(path, 'rb') as f_pcap:
        pcap = dpkt.pcap.Reader(f_pcap)

        count = 0

        for timestamp, buf in pcap:
            count += 1
            eth = dpkt.ethernet.Ethernet(buf)
			
			if not isinstance(eth.data, dpkt.ip.IP):
                continue
				
			ip = eth.data
			
			if isinstance(ip.data, dpkt.tcp.TCP):
                tcp = ip.data