# Project - EC2, NGINX & DNS

For this project, I set up a web server using an AWS EC2 instance and NGINX.

I also configured a custom domain using Cloudflare DNS and created an A record pointing my domain/subdomain to the public IPv4 address of my EC2 instance.

The purpose of this project was to understand how DNS, IP addresses, ports, security groups, EC2 and web servers work together

# Launch an EC2 instance 
What it is? - Brand-new virtual server in the AWS cloud 
Usage- run software applications and process data in the cloud without buying physical hardware
Steps:
- Search EC2 on the search bar, then you should see lunch instance option below 
- click on it and give it name. I chose ubuntu, then for the application i chose ubuntu 
- Create new key pair, WHY? two parts: private key (you keep it, never share) + public key (on the server). When you SSH, you prove you have the private key without sending a password over the network. More secure than passwords.  
- Network settings - Click Enable on the Auto-assign public ip .Why? You need a public IP so the outside world can reach your server.
- Firewall(security group) - Click Allow SSH traffic. We need this to log in. Click Allow HTTP traffic from the internet. Why? You need this. People access your site via http://ashkir.co.uk on port 80. HTTP is fast and simple and HTTPS requires SSL certificate 
-Launch instance and save it 
- Click connect and get the SSH key 

![description of what this shows](Screenshot%202026-09-17%20at%2016.12.13.png)

# NGINX
Nginx is  software used to host websites, manage web traffic, and speed up applications

Steps:
- Chmod 400 Ubuntu.pem this means the owner can read the file
- SSH connection- we are connecting securely to a remote Linux virtual server hosted on Amazon Web Services (AWS).
- Sudo apt install -y nginx - downloads and install nginx -y flag auto confirms it 
- sudo systemctl start nginx- it tells the linux system to turn nginx web server in the background
- Sudo systemctl enable nginx- make nginx turn itself on automatically every time the server reboots
- To check if nginx is working we type curl http://localhost see below for the output

![description of what this shows](Screenshot%202026-09-17%20at%2016.17.33.png)

# Configure DNS

Create an A record in Cloudflare
- Click on add record, type the domain name you bought ashkir.co.uk
- In content put the public ipv4 address you can find this in EC2 instance
- Proxy turned off as we want traffic to go straight to my EC2 Ip, no middleman (cloudflare)
- A-Record - type of DNS record that maps a domain name to it physical ipv4 address

![description of what this shows](Screenshot%202026-09-17%20at%2016.17.46.png)

![description of what this shows](Screenshot%202026-09-17%20at%2016.18.02.png)


''' Browser
   |
   v
nginx.ashkir.co.uk
   |
   v
Cloudflare DNS
   |
   v
EC2 Public IP
   |
   v
AWS Security Group
   |
   | Port 80
   v
NGINX
   |
   v
NGINX Welcome Page'''
