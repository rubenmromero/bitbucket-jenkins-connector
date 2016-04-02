# Bitbucket-Jenkins-Connector

Web service to integrate Bitbucket webhooks with Jenkins multi-branch projects.

Execute a Jenkins branch task based on the pushed branch from Bitbucket.

## Configuration

1. Download the project code in your favourite path:

        $ git clone https://github.com/rubenmromero/bitbucket-jenkins-connector.git

2. Create a copy of [jenkins.yaml.dist](conf/jenkins.yaml.dist) template to `conf/jenkins.yaml`, edit the new file and set the Jenkins global parameters replacing the existing `<tags>` with the appropiate values:

        # From the project root folder
        $ cp -p conf/jenkins.yaml.dist conf/jenkins.yaml
        $ vi conf/jenkins.yaml

3. For each new project to deploy through Jenkins, create a copy of [project.yaml.dist](conf/project.yaml.dist) template to `conf/<project>.yaml`, edit the new file and set the Jenkins project parameters replacing the existing `<tags>` with the appropiate values:

        # From the project root folder
        $ cp -p conf/project.yaml.dist conf/<project>.yaml
        $ vi conf/<project>.yaml

4. For Debian OS family, enable Apache cgi module (in Red Hat OS family this module is loaded by default):

        $ sudo a2enmod cgi

5. Enable `bjconnector` VHost:

    * For Debian OS family:

            # From the project root folder
            $ sudo cp vhost/debian/bjconnector.conf /etc/apache2/sites-available/
            $ sudo a2ensite bjconnector.conf
            $ /etc/init.d/apache2 restart

    * For Red Hat OS family:

            # From the project root folder
            $ sudo cp vhost/redhat/bjconnector.conf /etc/httpd/conf.d
            $ /etc/init.d/httpd restart

