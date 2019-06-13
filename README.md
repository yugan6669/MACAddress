Fetching Company  Name and details  through hitting  API

Step1: 
First generate your API key through Macaddress site https://macaddress.io

Step2:
Implemented Program using Python language
Executed the program using command
$python3 macadrress.py <API_Key> <MAC_Address>

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
   $bash macaddress.sh at_Jkpyix2qvXMRA29casQxJ1nqioU8b 44:38:39:ff:ef:57

Then the output looks like :
Company Name for MAC Address :44:38:39:ff:ef:57 is  Cumulus Networks, Inc
Compnay Address is: 650 Castro Street, suite 120-245 Mountain View CA 94041 US
