#!/usr/bin/python36


import os
import subprocess
import cgi
import cgitb
cgitb.enable()


print("content-type: text/html")
print("\n")


os.system("tput  setaf   4")
print("<marque>------------------------WELCOME TO MY MENU------------------------</marque>")
print("<br>")
print("<br>")

form = cgi.FieldStorage()
mysystem = form.getvalue("l")

if mysystem == "remote":	
	form = cgi.FieldStorage()	
	rip = form.getvalue('i')
	form = cgi.FieldStorage()	
	ch = form.getvalue('v')
	form =cgi.FieldStorage()
	password = form.getvalue('p')

	if int(ch) == 1:
		x = subprocess.getoutput("""sudo sshpass -p {} ssh  -o StictHostKeyChecking=no -l  root {}
		date""".format(password,rip))
		print(x)

	elif int(ch) == 2:
		x = subprocess.getoutput("""sudo sshpass -p  {} ssh -o StrictHostKeyChecking=no -l  root {}
		 cal""".format(password,rip))
		print("<pre>")		
		print(x)
		print("< pre />")

	elif int(ch) == 3:
		form = cgi.FieldStorage()	
		u = form.getvalue('u')

		subprocess.getoutput("""sudo sshpass -p {} ssh -o StrictHostKeyChecking=no -l root {} useradd  {} """.format(password,rip,u))
		print ("<br>")
		print("new user ", u ,"created ")

	elif int(ch) == 4:
		print(subprocess.getoutput("sudo sshpass -p  {} ssh -o StrictHostKeyChecking=no -l root {} yum install httpd -y ".format(password,rip)))		
		print(subprocess.getoutput("sudo sshpass -p  {} ssh -o StrictHostKeyChecking=no -l root {} iptables -F".format(password,rip)))
		print(subprocess.getoutput("sudo sshpass -p  {} ssh  -o  StrictHostKeyChecking=no -l root {} systemctl start httpd".format(password,rip)))
		
		print("server configured")
	
	elif int(ch) == 5 :	
		subprocess.getoutput("sudo sshpass -p {} ssh -o StrictHostKeyChecking=no -l root {} systemctl  status httpd".format(password,rip))
            		
	elif int(ch) == 6:
		subprocess.getoutput("sudo sshpass -p {} ssh -o StrictHostKeyChecking=no -l root {} systemctl stop httpd".format(password,rip))

	elif int(ch) == 7:
		print(subprocess.getoutput("sudo sshpass -p {} ssh -o StrictHostKeyChecking=no -l root {}iptables -F".format(password,rip))) 
		print(subprocess.getoutput("sudo sshpass -p {} ssh -o StrictHostKeyChecking=no -l root {} hadoop-daemon.sh start namenode".format(password,rip)))
		print("Hadoop Master Cluster Started :")
		print("</br>")
		print("<a href = 'http://192.168.43.46:50070' > OPEN CLUSTER DETAILS FROM HERE </a>")
	
	elif int(ch) == 8: 
		subprocess.getoutput("sudo sshpass -p {} ssh -o StrictHostKeyChecking=no -l root {} hadoop-daemon.sh stop namenode".format(password,rip))
		print("hadoop master cluster stoped")

	elif int(ch) == 9:
		subprocess.getoutput("sudo sshpass -p {} ssh -o StrictHostKeyChecking=no -l root {} iptables -F".format(password,rip)) 
		subprocess.getoutput("sudo sshpass -p {} ssh -o StrictHostKeyChecking=no -l root {} hadoop-daemon.sh start datanode".format(password,rip))
		print("Hadoop Slave Cluster Started : ")
		print("</br>")
		print("<a href = 'http://192.168.43.46:50070' > OPEN CLUSTER DETAILS FROM HERE </a>")
		print("</br> </br>")
		#<!-- b = subprocess.getoutput("sudo hadoop dfadmin -report") -->

	elif int(ch) == 10:
		subprocess.getoutput("sudo sshpass -p {} ssh -o StrictHostKeyChecking=no -l root {} hadoop-daemon.sh start datanode".format(password,rip))
		print("hadoop slave cluster stoped")
		
	elif int(ch) == 11:
    		print("<a href = 'http://192.168.43.46:50070' > OPEN CLUSTER DETAILS FROM HERE </a>")

	elif int(ch) == 12:
		form = cgi.FieldStorage()	
		h = form.getvalue('f')
		form = cgi.FieldStorage()	
		d = form.getvalue('d')
		subprocess.getoutput("cd {}".format(d))
		print(subprocess.getoutput("pwd"))
		subprocess.getoutput("sudo sshpass -p {} ssh -o StrictHostKeyChecking=no -l root {} hadoop fs -put {}/{} / ".format(password,rip,d,h))		
  		
	elif int(ch) == 13:
		form = cgi.FieldStorage()	
		h = form.getvalue('f1')
		
		subprocess.getoutput("cd /root/Desktop ")
		x = subprocess.getoutput("sudo sshpass -p {} ssh -o StrictHostKeyChecking=no -l root {} hadoop fs -cat /{} ".format(password,rip,h))
		print(x)



if mysystem == "local":
	form = cgi.FieldStorage()	
	ch = form.getvalue('v')
	subprocess.getoutput("setenforce 0")

	if int(ch) == 1:
		x = subprocess.getoutput("date")
		print(x)


	elif int(ch) == 2:
		x = subprocess.getoutput("sudo cal")
		print("<pre>")		
		print(x)
		print("</pre>")

	elif int(ch) == 3:
		form = cgi.FieldStorage()	
		u = form.getvalue('u')
		subprocess.getoutput("sudo useradd {}".format(u))
		print ("<br>")
		print("new user ", u ,"created ")

	elif int(ch) == 4:
		subprocess.getoutput("sudo yum install httpd")
		subprocess.getoutput("sudo iptables -F")
		subprocess.getoutput("sudo systemctl restart httpd")
		print("server configured")

	elif int(ch) == 5 :
		print("<pre>")	
		x = subprocess.getoutput("sudo systemctl status httpd ")
		print(x)
		print("<pre />")	


	elif int(ch) == 6:
		subprocess.getoutput("sudo systemctl stop httpd")

	elif int(ch) == 7:
		print(subprocess.getoutput("sudo iptables -F")) 
		print(subprocess.getoutput("sudo hadoop-daemon.sh start namenode"))
		print("Hadoop Master Cluster Started :")
		print("</br>")
		print("<a href = 'http://192.168.43.46:50070' > OPEN CLUSTER DETAILS FROM HERE </a>")
	
	elif int(ch) == 8: 
		subprocess.getoutput("sudo hadoop-daemon.sh stop namenode")
		print("hadoop master cluster stoped")

	elif int(ch) == 9:
		subprocess.getoutput("sudo iptables -F") 
		subprocess.getoutput("sudo hadoop-daemon.sh start datanode")
		print("Hadoop Slave Cluster Started : ")
		print("</br>")
		print("<a href = 'http://192.168.43.46:50070' > OPEN CLUSTER DETAILS FROM HERE </a>")
		print("</br> </br>")
		#<!-- b = subprocess.getoutput("sudo hadoop dfadmin -report") -->

	elif int(ch) == 10:
		subprocess.getoutput("sudo hadoop-daemon.sh start datanode")
		print("hadoop slave cluster stoped")
		
	elif int(ch) == 11:
    		print("<a href = 'http://192.168.43.46:50070' > OPEN CLUSTER DETAILS FROM HERE </a>")

	elif int(ch) == 12:
		form = cgi.FieldStorage()	
		h = form.getvalue('f')
		form = cgi.FieldStorage()	
		d = form.getvalue('d')
		subprocess.getoutput("cd {}".format(d))
		print(subprocess.getoutput("pwd"))
		subprocess.getoutput("sudo hadoop fs -put {}/{} / ".format(d,h))		
  		
	elif int(ch) == 13:
		form = cgi.FieldStorage()	
		h = form.getvalue('f1')
		
		subprocess.getoutput("cd /root/Desktop ")
		x = subprocess.getoutput("sudo hadoop fs -cat /{} ".format(h))
		print(x)


print("""<br> <br>If You Want To Do Something Else : <a href = 'http://192.168.43.46/menu.html' > click here <a />""")

print("<br>To Exit : <a href = 'https://www.google.com' > CLICK </a>")


