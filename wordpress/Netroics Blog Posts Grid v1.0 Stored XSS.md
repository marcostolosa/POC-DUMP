```
# Exploit Title: Stored XSS in post_title parameter in WordPress Plugin "Netroics Blog Posts Grid" v1.0
# Date: 08/08/2022
# Exploit Author: saitamang
# Vendor Homepage: wordpress.org
# Software Link: https://downloads.wordpress.org/plugin/netroics-blog-posts-grid.zip
# Version: 1.0
# Tested on: Centos 7 apache2 + MySQL

WordPress Plugin "Netroics Blog Posts Grid" is prone to a stored cross-site scripting (XSS) vulnerability because it fails to properly sanitize user-supplied input. An attacker may leverage this issue to execute arbitrary script code in the browser of an unsuspecting user in the context of the affected site. This can allow the attacker to steal cookie-based authentication credentials and launch other attacks. WordPress Plugin "Netroics Blog Posts Grid" version 1.0 is vulnerable; prior versions may also be affected.

Login as Editor > Add testimonial > Under Title inject payload below ; parameter (post_title parameter) > Save Draft > Preview the post


payload --> user s1"><img src=x onerror=alert(document.cookie)>.gif


The draft post can be viewed using other Editor or Admin account and Stored XSS will be triggered.

Further information can be preview from github below:
https://github.com/saitamang/POC-DUMP/blob/main/wordpress/Netroics%20Blog%20Posts%20Grid%20v1.0%20Stored%20XSS.md

```