echo "-------------------------------"
echo "|   Installing dependencies   |"
echo "-------------------------------"
echo ""
echo "* Updating package list        "
apt-get update
echo "* Installing nginx, python & pip      "

apt-get -q -y install virtualenv dnsutils nginx python python-dev python-pip

if [ $(arch) != arm* ]; then
    echo "This is not arm machine, install qemu-user-static and binfmt-support for image chroot"
    apt-get -q -y install qemu qemu-user-static binfmt-support

if [[ "$OSTYPE" == "linux-gnu" ]]; then
    apt-get -q -y install build-essential libffi-dev libssl-dev
fi
if [ ! -f /etc/init.d/mysql* ]; then
    echo "* Installing MySQL (root password will be empty!)"
    DEBIAN_FRONTEND=noninteractive apt-get install -y mysql-server
fi
echo "* Update setuptools            "
pip install --upgrade setuptools
echo "* Installing pip dependencies"
pip install nose mock ipaddress enum34 cryptography idna sqlalchemy twisted pyopenssl flask-sqlalchemy flask passlib pymysql service_identity pycrypto flask-wtf netifaces gunicorn >> "$install_log" 2>&1