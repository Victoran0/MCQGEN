# MCQ Generator

### End to end Generative AI project using Langchain and OpenAI

#### AWS Deployment

1. first login to the AWS: https://aws.amazon.com/console/
2. search about the EC2
3. you need to config the UBUNTU Machine
4. launch the instance
5. update the machine:  
   `sudo apt update`  
   `sudo apt-get update`  
   `sudo apt upgrade -y`  
   `sudo apt install git curl unzip tar make sudo vim wget -y`  
   `git clone "this-repository"`  
   `sudo apt install python3-pip`  
   `pip3 install -r requirements .txt`  
   `python3 -m streamlit run StreamlitAPP.py`

##### if you want to add openai api key

create . env file in your server  
`touch .env`  
`vi .env`  
press insert  
copy your api key and paste it there  
press escape then :wq and hit enter  
Go to the security section of instance after clicking its id, add the inbound rule  
Add the port 8501
