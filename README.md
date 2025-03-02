# GCP VM Auto-Scaling and Security

## Project Overview
This project demonstrates how to set up a **Virtual Machine (VM) on Google Cloud Platform (GCP)**, configure **auto-scaling policies based on workload**, and implement **security measures like IAM roles and firewall rules**. Additionally, a **CPU Load Testing Application** is included to simulate high CPU usage and test the auto-scaling feature.

## Features
- **VM Instance Deployment**: Creating and configuring a VM instance on GCP.
- **Auto-Scaling Configuration**: Automatically increasing or decreasing VM instances based on CPU utilization.
- **Security Implementation**: IAM role-based access control and firewall rules to manage network security.
- **CPU Load Testing Script**: Python application to simulate high CPU usage for auto-scaling validation.

---

## Prerequisites

Before proceeding, ensure you have the following:

- A **Google Cloud Platform (GCP) account** with billing enabled.
- **Google Cloud SDK (gcloud CLI)** installed on your local machine.
- **Basic knowledge of GCP services** like Compute Engine and IAM.
- **Python 3.x** installed.

---

## Setup Instructions

### 1. Clone the Repository

Run the following command to download the project files:

```bash
git clone <your-github-repo-url>
cd GCP_VM_AutoScaling_Project
```

### 2. Create a Virtual Machine on GCP

1. **Log in to Google Cloud Console**: [GCP Console](https://console.cloud.google.com/)
2. Navigate to **Compute Engine → VM Instances**.
3. Click **Create Instance** and configure:
   - **Machine Type**: `e2-standard-2` (2 vCPUs, 8GB RAM)
   - **Boot Disk**: Ubuntu 22.04 LTS
   - **Firewall**: Allow HTTP and HTTPS traffic.
4. Click **Create**.

### 3. Connect to the VM

Use SSH to connect to your VM:

```bash
gcloud compute ssh auto-scaling-vm --zone=<your-zone>
```

Alternatively, use the **SSH button** in the GCP Console.

---

## Installing Dependencies on VM

Run the following commands inside your VM to set up Python and required dependencies:

```bash
sudo apt update
sudo apt install -y python3 python3-pip
pip install psutil
```

---

## Running the CPU Load Testing Application

Navigate to the project directory and execute the script:

```bash
python3 cpu_load_test.py
```

The script will prompt you to enter:
```
Enter number of CPU cores to use (default: 2): 4
Enter duration in seconds (default: 30): 60
```

### Monitoring CPU Usage

To monitor CPU usage while the script runs, open another SSH session and run:

```bash
top
```

Or use:

```bash
htop
```

### Stopping the Test

To stop the script manually, press `CTRL + C`.

---

## Auto-Scaling Configuration

1. Go to **Compute Engine → Instance Groups**.
2. Click **Create Instance Group**.
3. Choose **Managed Instance Group** and select your VM template.
4. Configure auto-scaling:
   - **Enable Autoscaling**.
   - **Target CPU Utilization**: 50%.
   - **Min Instances**: 1, **Max Instances**: 10.
   - **Cooldown Period**: 60 seconds.
5. Click **Create**.

Once CPU load increases, new instances will be created automatically.

---

## Security Measures

### **Setting Up IAM Roles for Restricted Access**

1. Go to **IAM & Admin → IAM** in the Google Cloud Console.
2. Click **Add User** and enter the email address.
3. Assign restricted roles:
   - **Compute Viewer**: View VM details without modifications.
   - **Monitoring Viewer**: View logs without admin access.
4. Click **Save**.

### **Configuring Firewall Rules**

1. Navigate to **VPC Network → Firewall**.
2. Click **Create Firewall Rule**.
3. Set the following values:
   - **Name**: `allow-ssh-http`
   - **Direction**: Ingress
   - **Target**: All instances
   - **Source IP**: `0.0.0.0/0` (or restrict as needed)
   - **Allowed Protocols**: `tcp:22,80,443`
4. Click **Create**.

---

## Author
Ramaraju Venkata Veereswara Lohit (M23AID065)
