from fabric.contrib.files import append, exists, sed
from fabric.api import env, local, run
import random

REPO_URL = "https://github.com/Yetocome/AcaPush.git"
env.hosts=['ubuntu@123.206.196.67',]
env.key_filename = "~/.ssh/qcloud_key"

def _create_directory_structure_if_necessary(site_folder):
    for subfolder in ('database', 'static', 'virtualenv', 'source'):
        run('mkdir -p %s/%s' % (site_folder, subfolder))

def _get_latest_source(source_folder):
    if exists(source_folder + '/.git'):
        run('cd %s && git fetch' % (source_folder,))
    else:
        run('git clone %s %s' % (REPO_URL, source_folder))
    current_commit = local("git log -n 1 --format=%H", capture=True)
    run('cd %s && git reset --hard %s' % (source_folder, current_commit))

def _update_settings(source_folder, site_name):
    settings_path = source_folder + '/AcaPush/settings.py'
    sed(settings_path, "DEBUG = True", "DEBUG = False")
    sed(settings_path,
        'ALLOWED_HOSTS =.+$',
        'ALLOWED_HOSTS = ["%s"]' % (site_name,)
    )
    secret_key_file = source_folder + '/AcaPush/secret_key.py'
    if not exists(secret_key_file):
        chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
        key = ''.join(random.SystemRandom().choice(chars) for _ in range(50))
        append(secret_key_file, "SECRET_KEY = '%s'" % (key,))
    append(settings_path, '\nfrom .secret_key import SECRET_KEY')

def _update_virtualenv(source_folder):
    virtualenv_folder = source_folder + '/../virtualenv'
    if not exists(virtualenv_folder + '/bin/pip'):
        run('virtualenv --python=python3 %s' % (virtualenv_folder,))
    run('%s/bin/pip install -r %s/requirements.txt' % (
        virtualenv_folder, source_folder
    ))

def _update_static_files(source_folder):
    run('cd %s && ../virtualenv/bin/python3 manage.py collectstatic --noinput' % (
        source_folder
    ))

def _update_database(source_folder):
    run('cd %s && ../virtualenv/bin/python3 manage.py migrate --noinput' % (
        source_folder
    ))

def _init_database(source_folder):
    run('cd %s && ../virtualenv/bin/python3 dataUpdate.py init' % (
        source_folder
    ))

def _wash_database(source_folder):
    run('cd %s && rm db.sqlite3' % (
        source_folder
    ))

def _crawl_data(source_folder, size):
    run('cd %s && ../virtualenv/bin/python3 dataUpdate.py %s' % (
        source_folder, size
    ))

# usage: `fab deploy:xmhtest.cn`
def deploy(domain_name):
    site_folder = '/home/%s/sites/%s' % (env.user, domain_name)

    source_folder = site_folder + '/source'
    _create_directory_structure_if_necessary(site_folder)
    _get_latest_source(source_folder)
    _update_settings(source_folder, domain_name)
    _update_virtualenv(source_folder)
    _update_static_files(source_folder)
    _update_database(source_folder)

def wash(domain_name):
    site_folder = '/home/%s/sites/%s' % (env.user, domain_name)

    source_folder = site_folder + '/source'
    _wash_database(source_folder)
    _update_database(source_folder)
    _init_database(source_folder)

def crawl(domain_name, size):
    site_folder = '/home/%s/sites/%s' % (env.user, domain_name)

    source_folder = site_folder + '/source'
    _crawl_data(source_folder, size)

## Before deploy
# Replace REPO_URL
# Replace settings_path
# Replace gunicorn-upstart unix

## After first deploy - live
# cd /sites/xmhtest.cn/source
# sed "s/SITENAME/xmhtest.cn/g" deploy_tools/nginx.template.conf | sudo tee /etc/nginx/sites-available/xmhtest.cn
# sudo ln -s ../sites-available/xmhtest.cn /etc/nginx/sites-enabled/xmhtest.cn
# sed "s/SITENAME/xmhtest.cn/g" deploy_tools/gunicorn-upstart.template.conf | sudo tee /etc/init/gunicorn-xmhtest.cn.conf
# sudo service nginx reload
# sudo start gunicorn-xmhtest.cn

# ../virtualenv/bin/python3 manage.py createsuperuser

## After first deploy - staging
# cd /sites/api-staging.xmhtest.cn/source
# sed "s/SITENAME/api-staging.xmhtest.cn/g" deploy_tools/nginx.template.conf | sudo tee /etc/nginx/sites-available/api-staging.xmhtest.cn
# sudo ln -s ../sites-available/api-staging.xmhtest.cn /etc/nginx/sites-enabled/api-staging.xmhtest.cn
# sed "s/SITENAME/api-staging.xmhtest.cn/g" deploy_tools/gunicorn-upstart.template.conf | sudo tee /etc/init/gunicorn-api-staging.xmhtest.cn.conf
# sudo service nginx reload
# sudo start gunicorn-api-staging.xmhtest.cn

## After first deploy - both
# fab wash:api-staging.xmhtest.cn
# fab crawl:api-staging.xmhtest.cn, 1000

## After future deploy
# sudo service nginx reload
# sudo restart gunicorn-xmhtest.cn

# sudo restart gunicorn-api-staging.xmhtest.cn
