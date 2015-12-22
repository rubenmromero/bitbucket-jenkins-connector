# Bitbucket-Jenkins-Connector

Web service to integrate Bitbucket webhooks with Jenkins multi-branch projects.

Execute a Jenkins branch task based on the pushed branch from Bitbucket.

## Configuration

* Enable Apache cgi module:

        # From Debian OS family
        $ sudo a2enmod cgi
        
        # From Red Hat OS family
        $ ...

* For Debian OS family, enable the hooks VHost:

        $ sudo a2ensite hooks.conf
