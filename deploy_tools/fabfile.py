from fabric.contrib.files import append, exists, sed
from fabric.api import env, local, run
import random

REPO_URL = "https://github.com/Yetocome/Django_test.git"
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
    settings_path = source_folder + '/superlists/settings.py'
    sed(settings_path, "DEBUG = Ture", "DEBUG = False")
    sed(settings_path,
        'ALLOWED_HOSTS =.+$',
        'ALLOWED_HOSTS = ["%s"]' % (site_name,)
    )
    secret_key_file = source_folder + '/superlists/secret_key.py'
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


# sed "s/SITENAME/xmhtest.cn/g" deploy_tools/nginx.template.conf | sudo tee /etc/nginx/sites-available/xmhtest.cn
# sudo ln -s ../sites-available/xmhtest.cn /etc/nginx/sites-enabled/xmhtest.cn
# sed "s/SITENAME/xmhtest.cn/g" deploy_tools/gunicorn-upstart.template.conf | sudo tee /etc/init/gunicorn-xmhtest.cn.conf
# sudo service nginx reload
# sudo start gunicorn-xmhtest.cn
