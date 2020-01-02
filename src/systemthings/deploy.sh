cp hazmanot.service /etc/systemd/system/hazmanot.service
sudo systemctl start $PROJECT
sudo systemctl enable $PROJECT
sudo systemctl status $PROJECT