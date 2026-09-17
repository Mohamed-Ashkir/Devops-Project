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
