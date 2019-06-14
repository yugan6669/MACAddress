Fetching Company  Name and details  through hitting  API

CASE 1
=====================
Step1: 
First generate your API key through Macaddress site https://macaddress.io

Step2:
Implemented Program using Python language
Executed the program using command
$python3 macadrress.py <API_Key> <MAC_Address>


CASE2
======================
Step3:
Write the Docker file to build image 
Build the image using Dockerfile
$docker image build -t mac_image .
Run the container and pass API_Key and MAC Adress
$docker container run <Image-Id>/<Tag_name> <API-key> <Mac-Address>
Ex:
   $docker container run <Image-Id> at_Jkpyix2qvXMRA29casQxJ1nqioU8b 44:38:39:ff:ef:57
   $docker container run mac_image at_Jkpyix2qvXMRA29casQxJ1nqioU8b 44:38:39:ff:ef:57
Step4:
   Implemented Bash scrpt to containerized application
   $sudo bash macaddress.sh at_Jkpyix2qvXMRA29casQxJ1nqioU8b 44:38:39:ff:ef:57
   

CASE3
================================
Step5:
Create Custome Amazon machine Image 
$./packer build  -var-file=variables.json -var 'key=value' -var 'key=value' template.json
Ex:
$./packer build  -var-file=variables.json -var 'aws_access_key=AKIASRY7UBHWKEYP7WA5' -var 'aws_secret_key=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' template.json
Step6:
Launch EC2 Instance Ubuntu 16.04 with the above custom AMI
$cd /home/ubuntu/MACAddress
Step7:
$sudo bash macaddress.sh at_Jkpyix2qvXMRA29casQxJ1nqioU8b 44:38:39:ff:ef:57


In all the above 3 Cases  the output looks like :
company Name  for MAC Address: 44:38:39:ff:ef:57 is  Cumulus Networks, Inc
Company Address is 650 Castro Street, suite 120-245 Mountain View  CA  94041 US
countryCode is: US
