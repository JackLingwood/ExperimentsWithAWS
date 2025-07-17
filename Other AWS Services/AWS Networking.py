# VPC (Virtual Private Cloud)
# Amazon VPC (Virtual Private Cloud) is a service that allows you to create a logically isolated network within the AWS cloud.
# You can define your own IP address range, create subnets, and configure route tables and network gateways.
# VPC enables you to launch AWS resources, such as Amazon EC2 instances, within your own virtual network.
# It provides control over network configuration, security, and connectivity to other AWS services and the internet.
# VPC is essential for building secure and scalable applications in the cloud, allowing you to customize your network architecture
# to meet specific requirements.
# AWS VPC is a service that allows you to create a logically isolated network within the AWS cloud. You can define your own IP address
# range, create subnets, and configure route tables and network gateways. VPC enables you to launch AWS resources, such as Amazon EC2
# instances, within your own virtual network. It provides control over network configuration, security, and connectivity to other AWS
# services and the internet. VPC is essential for building secure and scalable applications in the cloud, allowing you to customize
# your network architecture to meet specific requirements.

# AWS VPC (Virtual Private Cloud) is a service that allows you to create a logically isolated network within the AWS cloud.
# You can define your own IP address range, create subnets, and configure route tables and network gateways.
# VPC enables you to launch AWS resources, such as Amazon EC2 instances, within your own virtual network.
# It provides control over network configuration, security, and connectivity to other AWS services and the internet.
# VPC is essential for building secure and scalable applications in the cloud, allowing you to customize
# your network architecture to meet specific requirements.

# AWS VPC (Virtual Private Cloud) is a service that allows you to create a logically isolated network within the AWS cloud.
# An Amazon VPC lets you provision a logically isolated section of the AWS Cloud where you can launch AWS resources in a virtual network
# that you define.

# Subnets
# Subnets are segments of a VPC's IP address range where you can place groups of isolated resources.
# Each subnet must reside entirely within one Availability Zone and cannot span zones.
# Subnets allow you to organize resources based on security and operational needs.
# Subnets are used to organize your resources and can be made publicly or privately accessible. A private subnet is commonly used to contain
# resources like a database storing customer or transactional information. A public subnet is commonly used for resources like a customer-facing
# website.
# Subnets are used to organize resources, share resources publicly, or isolate resources to keep them private.

# AWS Cloud >> AWS Region >> AWS Availability Zone >> AWS VPC >> Subnet

# You can place EC2 instances in a subnet, and you can also place other resources like RDS databases or Lambda functions.
# Subnets can be public or private, depending on whether they have a route to the internet

# Subnets are chunks of ip address space that you can use to organize your resources.
# Subnets are used to organize resources, share resources publicly, or isolate resources to keep them private.


# An internet gateway is a horizontally scaled, redundant, and highly available VPC component that allows communication between instances in your VPC and the internet.
# It serves two purposes: to provide a target in your VPC route tables for internet-routbound traffic, and to perform network address translation (NAT) for instances
# that have been assigned public IPv4 addresses.

# A virtual private gateway is the VPN concentrator on the Amazon side of the VPN connection between your VPC and your data center.
# It is the AWS side of a VPN connection. A virtual private gateway is a logical, fully redundant distributed edge routing function that sits at the edge of your VPC.
# It allows you to connect your VPC to your on-premises network using a VPN connection.

# A NAT gateway is a managed NAT service that provides outbound internet access to instances in a private subnet.
# It allows instances in a private subnet to initiate outbound traffic to the internet while preventing unsolicited inbound traffic from the internet.
# A NAT gateway is a managed NAT service that provides outbound internet access to instances in a private subnet.

# AWS Direct Connect is a cloud service solution that makes it easy to establish a dedicated network connection from your premises to AWS.
# Using AWS Direct Connect, you can connect your internal network to an AWS Direct Connect location over a standard Ethernet fiber-optic cable.
# AWS Direct Connect links your internal network to an AWS Direct Connect location over a standard Ethernet fiber-optic cable.

# Amazon Virtual Private Cloud
# Amazon VPC is used to establish boundaries around your AWS resources.

# Virtual private gateway
# A virtual private gateway allows protected internet traffic to enter into the VPC.

# Virtual private network
# A VPN encrypts your internet traffic, helping protect it from anyone who might try to intercept or monitor it.

# AWS Client VPN
# AWS Client VPN is a managed client-based VPN service that enables you to securely access AWS resources from any location.
# It allows you to connect your devices to AWS resources over an encrypted VPN connection, providing secure access to your VPC and on-premises networks.
# AWS Client VPN is a networking service you can use to connect your remote workers and on-premises networks to the cloud. It is a fully managed, elastic
# VPN service that automatically scales up or down based on user demand. Because it is a cloud VPN solution, you don’t need to install and manage hardware
# or try to estimate how many remote users to support at one time.
# Benefits: AWS Client VPN provides advanced authentication, remote access. It is elastic and fully managed.
# Use case: It can be used to quickly scale remote-worker access.


# AWS Site to Site VPN
# AWS Site-to-Site VPN is a managed service that allows you to securely connect your on-premises network or branch office to your Amazon VPC.`
# It establishes a secure and encrypted connection over the internet, enabling you to extend your data center or office network to the AWS cloud.
# AWS Site-to-Site VPN is a managed service that allows you to securely connect your on-premises network or branch office to your Amazon VPC.
# Site-to-Site VPN creates a secure connection between your data center or branch offices and your AWS Cloud resources.
# Benefits: Site-to-Site VPN provides high availability, secure and private sessions, and accelerates applications.
# Use cases: It can be used for application migration and secure communication between remote locations.




# AWS PrivateLink
# AWS PrivateLink is a service that enables you to privately connect your VPC to supported AWS services and VPC endpoint services powered by PrivateLink.
# It provides private connectivity between VPCs, AWS services, and on-premises applications without exposing your traffic to the public internet.

# AWS Direct Connect
# AWS Direct Connect is a cloud service solution that makes it easy to establish a dedicated network connection from your premises to AWS.
# Using AWS Direct Connect, you can connect your internal network to an AWS Direct Connect location over a standard Ethernet fiber-optic cable.
# Direct Connect is a service that makes it possible for you to establish a dedicated private connection between your network and VPC in the AWS Cloud.
# Benefits: AWS Direct Connect reduces network costs and increases amount of bandwidth.
# Direct Connect bypasses the internet and provides a consistent, low-latency network experience.
# This makes it ideal for applications like video streaming and other real-time applications that require high performance. 
# Direct Connect helps ensure smooth and reliable data transfers at massive scale for real-time analysis, rapid data backup, or broadcast media processing.


# AWS PrivateLink is a highly available, scalable technology that you can use to privately connect your VPC to services and resources as if they
# were in your VPC. You do not need to use an internet gateway, NAT device, public IP address, Direct Connect connection, or AWS Site-to-Site VPN
# connection to allow communication with AWS services or resources from your private subnets. Instead, you control the specific API endpoints,
# sites, services, and resources that are reachable from your VPC.
# Benefits: AWS PrivateLink helps you secure your traffic and connect with simplified management rules.
# Use case: It is used for connecting your clients in your VPC to resources, other VPCs, and endpoints.

# AWS Transit Gateway
# AWS Transit Gateway is a service that enables you to connect multiple VPCs and on-premises networks through a single gateway.
# It simplifies network management by allowing you to create a hub-and-spoke model for connecting VPCs, VPNs, and Direct Connect gateways.

# Network Address Translation (NAT) Gateway
# A NAT gateway is a managed NAT service that provides outbound internet access to instances in a private subnet.
# It allows instances in a private subnet to initiate outbound traffic to the internet while preventing unsolicited inbound traffic from the internet.

# Amazon API Gateway
# Amazon API Gateway is a fully managed service that makes it easy for developers to create, publish, maintain, monitor, and secure APIs at any scale.
# It provides a simple way to create RESTful APIs and WebSocket APIs that enable real-time two-way communication between clients and servers.
# API Gateway handles all the tasks involved in accepting and processing up to hundreds of thousands of concurrent API calls, including traffic management,
# authorization and access control, monitoring, and API version management.

# AWS Direct Connect
# AWS Direct Connect is a private, dedicated AWS connection to your data center or office.

# Access control in a VPC is done using security groups and network access control lists (ACLs).
# Security groups act as virtual firewalls for your instances to control inbound and outbound traffic.
# Network ACLs provide an additional layer of security by allowing you to control traffic at the subnet level.
# Security groups are stateful, meaning that if you allow an incoming request, the response is automatically allowed.
# Network ACLs are stateless, meaning that you must explicitly allow both inbound and outbound traffic.
# Security groups are used to control inbound and outbound traffic at the instance level, while network ACLs are used 
# to control traffic at the subnet level.


# All EC2 instances disallow all inbound traffic by default.
# You can allow inbound traffic by adding rules to the security group associated with the instance.
# Security groups are stateful, meaning that if you allow an incoming request, the response is automatically allowed.
# Network ACLs are stateless, meaning that you must explicitly allow both inbound and outbound traffic.

# For custom network ACLs, all inbound and outbound traffic is denied until you add rules to specify which traffic to allow.
# Additionally, all network ACLs have an explicit deny rule. This rule makes sure that if a packet doesn’t match any of the
# other rules on the list, the packet is denied.

# Security groups operate at instance level, while network ACLs operate at subnet level.
# Security groups are stateful, meaning that if you allow an incoming request, the response is automatically allowed.
# Network ACLs are stateless, meaning that you must explicitly allow both inbound and outbound traffic
# Security groups only allow type rules, while network ACLs allow both type and port rules.
# Type rules are used to allow or deny traffic based on the protocol and port number, while port rules are used to allow or deny traffic based on the port number only.
# With security groups return traffic is automatically allowed, while with network ACLs return traffic must be explicitly allowed.
# Security groups are useful for fine-grained control over instance-level traffic, while network ACLs are useful for broader control over subnet-level traffic.

