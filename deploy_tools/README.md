If it is a newserver:

You should install git python3(with pip and virtualenv) and nginx by:
	
	apt-get install git python3 nginx python-pip python-virtualenv

Before running your websites, you should do these things by steps.

1. Go to the source folder.
2. Replace the name in module and place it appropriately.

	    servername@server_ip:$ sed "s/SITENAME/[your_domain]/g" \
	                           deploy_tools/nginx.template.conf | sudo tee \
	                           /etc/nginx/sites-available/[your_domain]

3. active the virtual server of this configureation.

		 servername@server_ip:$ sudo ln -s ../sites-available/[your_domain] \
		 						/etc/nginx/sites-enabled/[your_domain]


4. Edit your Upstart script.

		servername@server_ip:$ sed "s/SITENAME/[your_domain]/g" \
		 						deploy_tools/gunicorn-upstart.template.conf | sudo tee \
		 						/etc/init/gunicorn-[your_domain].conf

5. Launch these two services.

		servername@server_ip:$ sudo service nginx reload
		servername@server_ip:$ sudo start gunicorn-[your_domain]
