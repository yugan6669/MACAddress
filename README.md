Fetching Company  Data through hitting  API
First generate your API key through Macaddress site https://macaddress.io
Implemented Program using Python language
Executed the program using command
$python3 macadrress.py <API_Key> <MAC_Address>

Write the Docker file to build image 
Build the image using Dockerfile
$docker image build -t mac_image .
Run the container and pass API_Key and MAC Adress
$docker container run <Image-Id>/<Tag_name> <API-key> <Mac-Address>
Ex:$docker container run <Image-Id> at_Jkpyix2qvXMRA29casQxJ1nqioU8b 44:38:39:ff:ef:57
   $docker container run mac_image at_Jkpyix2qvXMRA29casQxJ1nqioU8b 44:38:39:ff:ef:57
Then we will get output like :
Company Name is: Cumulus Networks, Inc
Compnay Address is: 650 Castro Street, suite 120-245 Mountain View CA 94041 US
