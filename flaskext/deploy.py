from fabric.api import run, require, env, local, put
from fabric.contrib.files import exists
from fabric.context_managers import cd
import time


env.branch = 'master'
env.app_name = app.name

env.staging_hosts = []
env.live_hosts = []
env.user = env.app_name
env.app_dir = '/opt/%s' % (env.app_name)
env.timestamp = time.strftime('%Y%m%d%H%M%S')
    
def setup():
    """Set up the initial structure on the remote hosts."""
    require('hosts')
    require('app_dir')
    
    with cd(env.app_dir):
        run("mkdir versions")
        run("mkdir archives")

def switch_to(version):
    """Switch the current (ie live) version"""
    require('hosts')
    require('app_dir')
    with cd(env.app_dir):
        if exists('versions/previous'):
            run('rm versions/previous')
    
        if exists('versions/current'):
            run('mv versions/current versions/previous')
        
        run('ln -s %s versions/current' % version)

def switch_to_version(version):
    switch_to(version)
    # restart nginx/apache

def make_tar():
    require('version')
    local('tar -cf - %s | gzip -c > %s.tar.gz' % (env.version, env.version))
    local('rm -fr %s' % env.version)

def upload_tar():
    require('version', provided_by=[deploy])

    put('%s.tar.gz' % env.version, '%s/archives/' % env.app_path)
    with cd(env.app_dir):
        with cd('versions'):
            run('gzip -dc ../archives/%s.tar.gz | tar xf -' % (env.version))
            
    local('rm %s.tar.gz' % env.version)

def increment_version():
    # ++ version number
    # make git tags
    # generate changelog
    env.version = 1
    

def deploy():
    
    setup()
    increment_version()
    make_tar()
    upload_tar()
