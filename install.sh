apt update
apt install python3 python3-pip -y
apt install apt-transport-https ca-certificates curl software-properties-common -y
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"
apt update
apt install docker-ce -y
pip3 install gitpython pygithub docker
pip3 install mysql-connector-python
apt install uvicorn -y
apt install mysql-server -y
apt-get install libmysqlclient-dev -y