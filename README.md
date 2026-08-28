# 🛡️ Network Sniffer

A simple **Python-based network packet sniffer** built for cybersecurity learning and authorized network analysis. The project captures and analyzes network packets using Python and Scapy, displaying useful information such as source and destination IP addresses, protocols, ports, and packet details.

> ⚠️ **Educational & Ethical Use Only:** This tool should only be used on networks and devices that you own or have explicit permission to monitor. Unauthorized packet interception may be illegal.

---

## 📌 Features

* 🔍 Capture live network packets
* 🌐 Display source and destination IP addresses
* 📡 Identify common network protocols
* 🔢 Display source and destination ports
* 📦 Inspect packet information
* 🐍 Built with Python and Scapy
* 🎓 Designed for cybersecurity education and authorized testing

---

## 🛠️ Technologies Used

* **Python 3**
* **Scapy**
* **VS Code** (recommended)

---


---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/Network-Sniffer.git
```

Move into the project directory:

```bash
cd Network-Sniffer
```

### 2. Install Dependencies

Install Scapy using:

```bash
pip install scapy
```

Or, if you have a `requirements.txt` file:

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run

Run the Python script:

```bash
python network_sniffer.py
```

On some systems, administrator/root privileges may be required for packet capture.

### Windows

Open **Command Prompt or PowerShell as Administrator** and run:

```bash
python network_sniffer.py
```

---

## 🔎 Example Output

```text
[+] Network Sniffer Started...

Source IP      : 192.168.1.10
Destination IP : 8.8.8.8
Protocol       : UDP
Source Port    : 52341
Destination Port: 53

-----------------------------------

Source IP      : 192.168.1.10
Destination IP : 142.250.x.x
Protocol       : TCP
Source Port    : 52432
Destination Port: 443
```

The exact output depends on the packets observed on the authorized network interface.

---

## 🧠 How It Works

The program uses **Scapy** to capture packets from a network interface.

The basic process is:

```text
Network Interface
       ↓
Packet Capture
       ↓
Packet Analysis
       ↓
Extract Information
       ↓
Display Packet Details
```

The sniffer can inspect packet layers such as:

* Ethernet
* IP
* TCP
* UDP
* ICMP

---

## 🎯 Learning Objectives

This project was created to understand:

* Network packet structure
* IP addressing
* TCP and UDP protocols
* Network interfaces
* Packet capturing
* Basic network monitoring
* Python cybersecurity programming
* Scapy packet manipulation and analysis

---


## 🚀 Future Improvements

Possible improvements include:

* [ ] Add packet filtering
* [ ] Add protocol statistics
* [ ] Add packet count
* [ ] Save captured packets to `.pcap`
* [ ] Add a graphical user interface
* [ ] Add real-time traffic statistics
* [ ] Add logging functionality
* [ ] Improve packet analysis
* [ ] Add customizable network-interface selection

---

## 👨‍💻 Author

**Rehmat Ullah**

Cybersecurity & Python Enthusiast

---

## ⭐ Support

If you found this project useful for learning cybersecurity, consider giving the repository a ⭐ on GitHub.
