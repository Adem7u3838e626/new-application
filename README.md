# 🛰 Remote IP Logger & Reverse Shell Server

This project allows a client machine to send its local and public IP to a server, which logs it. After receiving the IP info, the server automatically launches a remote shell interface to interact with the client.

---

## ⚙️ Requirements

- Python 3.9 or later  
- OS: Windows or Linux  
- Internet connection (for public IP detection)

---

## 🚀 How to Run

### 1. Install Python

If Python is not already installed on your machine, download it from the official website:  
👉 https://www.python.org/downloads/

Make sure to check ✅ "Add Python to PATH" during installation on Windows.

---

### 2. Download the Project

You can clone the repository using Git:

```bash
git clone https://github.com/Adem7u3838e626/new-application.git
cd your-repo-name

Or download it as a ZIP and extract it:
https://github.com/Adem7u3838e626/new-application/archive/refs/heads/main.zip

3. Run the Program

On Windows, double-click start.py or run it using PowerShell or Command Prompt:

setup_and_run.ps1

On Linux, you can run:

bash start.sh

This will:

    Start the IP receiver server.

    Wait for the client to send its IP info.

    Log the IPs into ip_log.txt.

    Automatically launch the command-and-control server.

🗃 Project Structure

📁 project-root/
├── client.py           # Sends local/public IP to server
├── ip_server.py        # Receives IP info and logs it
├── server.py           # Reverse shell server
├── start.py            # Entry point: runs ip_server, then server
├── ip_log.txt          # Stores the latest received IPs
├── requirements.txt    # Python dependencies (empty or basic)
├── setup.sh            # Bash script for Linux setup (optional)
├── setup_win.bat       # Batch script for Windows setup (optional)
└── README.md           # This file
