# Project: 0x07. Networking Basics #0

## Resources

#### Read or watch:

* [OSI model](https://intranet.alxswe.com/rltoken/k2uCsynicuNbu1cAQhXqVQ)
* [Different types of network](https://intranet.alxswe.com/rltoken/XW3ZGm5Ya_a8XVDXcAKT_A)
* [LAN network](https://intranet.alxswe.com/rltoken/en370-Hrwgi_GUvFcg3bKg)
* [WAN network](https://intranet.alxswe.com/rltoken/Ah1EKqnINR85lM4P2WnLSw)
* [Internet](https://intranet.alxswe.com/rltoken/Lwh9xQxFD4dWh5sIApXI1g)
* [MAC address](https://intranet.alxswe.com/rltoken/j-Wp-YRvFTVP04SpIeRzHQ)
* [What is an IP address](https://intranet.alxswe.com/rltoken/HaZZvrmGaQ3U7ZLDYgZb6w)
* [Private and public address](https://intranet.alxswe.com/rltoken/OPJCZYuWSEXLIZOqU9Uc0A)
* [IPv4 and IPv6](https://intranet.alxswe.com/rltoken/M8g-egWLlldTl6Y0QECdwA)
* [Localhost](https://intranet.alxswe.com/rltoken/7lj-zoZQ7xFTkj4MTyos_g)
* [TCP and UDP](https://intranet.alxswe.com/rltoken/uJbs8E9-FyATfsELpmtTIg)
* [TCP/UDP ports List](https://intranet.alxswe.com/rltoken/4PYkqDfOvIZZb9aUPGOOzQ)
* [What is ping /ICMP](https://intranet.alxswe.com/rltoken/3zBgO6r2M1Q8lUVt9g8aJw)
* [Positional parameters](https://intranet.alxswe.com/rltoken/-8dL4Vqc0Wbt7f1iAwks6w)

## Learning Objectives

### General

* What it is
* How many layers it has
* How it is organized

## Tasks

| Task | File |
| ---- | ---- |
| 0. OSI model | [0-OSI_model](./0-OSI_model) |
| 1. Types of network | [1-types_of_network](./1-types_of_network) |
| 2. MAC and IP address | [2-MAC_and_IP_address](./2-MAC_and_IP_address) |
| 3. UDP and TCP | [3-UDP_and_TCP](./3-UDP_and_TCP) |
| 4. TCP and UDP ports | [4-TCP_and_UDP_ports](./4-TCP_and_UDP_ports) |
| 5. Is the host on the network | [5-is_the_host_on_the_network](./5-is_the_host_on_the_network) |

## Task 0: OSI Model

### Objective
Understand the OSI (Open Systems Interconnection) model, its purpose, and how it is organized.

### Questions and Answers
1. **What is the OSI model?**
   - **Answer**: The OSI model is a conceptual model that characterizes the communication functions of a telecommunication system without regard to their underlying internal structure and technology.

2. **How is the OSI model organized?**
   - **Answer**: From the lowest to the highest level.
### File
- [0-OSI_model](./0-OSI_model)

## Task 1: Types of Network

### Objective
Understand the different types of networks (LAN, WAN, Internet) and their applications.

### Questions and Answers
1. **What type of network is a computer in local connected to?**
   - **Answer**: LAN

2. **What type of network could connect an office in one building to another office in a building a few streets away?**
   - **Answer**: WAN

3. **What network do you use when you browse www.google.com from your smartphone (not connected to the WiFi)?**
   - **Answer**: Internet
### File
- [1-types_of_network](./1-types_of_network)

## Task 2: MAC and IP Address

### Objective
Understand the concepts of MAC addresses and IP addresses, including their roles in networking.

### Questions and Answers
1. **What is a MAC address?**
   - **Answer**: The unique identifier of a network interface

2. **What is an IP address?**
   - **Answer**:Is to devices connected to a network what postal address is to houses
### File
- [2-MAC_and_IP_address](./2-MAC_and_IP_address)


## Task 3: UDP and TCP

### Objective
Understand the differences between TCP and UDP protocols and their characteristics in data transmission.

### Questions and Answers
1. **Which statement is correct for the TCP box?**
   - **Answer**: It is a protocol that is transferring data in a slow way but surely

2. **Which statement is correct for the UDP box?**
   - **Answer**: It is a protocol that is transferring data in a fast way and might lose data along in the process

3. **Which statement is correct for the TCP worker?**
   - **Answer**: Have you received boxes x, y, z?

### File
- [3-UDP_and_TCP](./3-UDP_and_TCP)

## Task 4: TCP and UDP Ports

### Objective
Write a Bash script that displays listening ports, showing only listening sockets and the PID and name of the program to which each socket belongs.

### Script Description
The task requires a Bash script that lists all active listening ports on the system, specifically focusing on TCP and UDP sockets in the "LISTEN" state. Additionally, the script must display the Process ID (PID) and the name of the program associated with each socket.

### file
- [4-TCP_and_UDP_ports](./4-TCP_and_UDP_ports)


## Task 5: Is the Host on the Network

### Objective
Write a Bash script that pings an IP address passed as an argument to check if a network device is available.

### Script Description
The task requires a Bash script that uses the `ping` command, which leverages the Internet Control Message Protocol (ICMP) to check the availability of a network device. The script must:
- Accept a string as an argument (the IP address to ping).
- Display `Usage: 5-is_the_host_on_the_network {IP_ADDRESS}` if no argument is provided.
- Ping the specified IP address 5 times.

### File
- [5-is_the_host_on_the_network](./5-is_the_host_on_the_network)
