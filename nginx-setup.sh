#!/bin/bash
amazon-linux-extras enable nginx1
yum clean metadata
yum install -y nginx
systemctl start nginx
systemctl enable nginx