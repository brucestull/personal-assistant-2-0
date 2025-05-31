

```bash
flynntknapp@DELL-DESK:~$ python manage.py makemigrations
Traceback (most recent call last):
  File "/home/flynntknapp/Programming/personal-assistant-2-0/manage.py", line 26, in <module>
    main()
  File "/home/flynntknapp/Programming/personal-assistant-2-0/manage.py", line 22, in main
    execute_from_command_line(sys.argv)
  File "/home/flynntknapp/.local/share/virtualenvs/personal-assistant-2-0-Z4bZKilw/lib/python3.11/site-packages/django/core/management/__init__.py", line 446, in execute_from_command_line
    utility.execute()
  File "/home/flynntknapp/.local/share/virtualenvs/personal-assistant-2-0-Z4bZKilw/lib/python3.11/site-packages/django/core/management/__init__.py", line 420, in execute
    django.setup()
  File "/home/flynntknapp/.local/share/virtualenvs/personal-assistant-2-0-Z4bZKilw/lib/python3.11/site-packages/django/__init__.py", line 24, in setup
    apps.populate(settings.INSTALLED_APPS)
  File "/home/flynntknapp/.local/share/virtualenvs/personal-assistant-2-0-Z4bZKilw/lib/python3.11/site-packages/django/apps/registry.py", line 116, in populate
    app_config.import_models()
  File "/home/flynntknapp/.local/share/virtualenvs/personal-assistant-2-0-Z4bZKilw/lib/python3.11/site-packages/django/apps/config.py", line 269, in import_models
    self.models_module = import_module(models_module_name)
                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1204, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1176, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1147, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 690, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 940, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/home/flynntknapp/Programming/personal-assistant-2-0/accounts/models.py", line 8, in <module>
    from vitals.models import BloodPressure
  File "/home/flynntknapp/Programming/personal-assistant-2-0/vitals/models.py", line 3, in <module>
    from base.models import CreatedUpdatedBase
  File "/home/flynntknapp/Programming/personal-assistant-2-0/base/models.py", line 3, in <module>
    from config.settings import AUTH_USER_MODEL
ImportError: cannot import name 'AUTH_USER_MODEL' from 'config.settings' (/home/flynntknapp/Programming/personal-assistant-2-0/config/settings/__init__.py)
flynntknapp@DELL-DESK:~$
```

```bash
flynntknapp@DELL-DESK:~$ python manage.py makemigrations
Traceback (most recent call last):
  File "/home/flynntknapp/.local/share/virtualenvs/personal-assistant-2-0-Z4bZKilw/lib/python3.11/site-packages/django/apps/config.py", line 235, in get_model
    return self.models[model_name.lower()]
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^
KeyError: 'customuser'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/flynntknapp/.local/share/virtualenvs/personal-assistant-2-0-Z4bZKilw/lib/python3.11/site-packages/django/contrib/auth/__init__.py", line 170, in get_user_model
    return django_apps.get_model(settings.AUTH_USER_MODEL, require_ready=False)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/flynntknapp/.local/share/virtualenvs/personal-assistant-2-0-Z4bZKilw/lib/python3.11/site-packages/django/apps/registry.py", line 213, in get_model
    return app_config.get_model(model_name, require_ready=require_ready)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/flynntknapp/.local/share/virtualenvs/personal-assistant-2-0-Z4bZKilw/lib/python3.11/site-packages/django/apps/config.py", line 237, in get_model
    raise LookupError(
LookupError: App 'accounts' doesn't have a 'CustomUser' model.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/flynntknapp/Programming/personal-assistant-2-0/manage.py", line 26, in <module>
    main()
  File "/home/flynntknapp/Programming/personal-assistant-2-0/manage.py", line 22, in main
    execute_from_command_line(sys.argv)
  File "/home/flynntknapp/.local/share/virtualenvs/personal-assistant-2-0-Z4bZKilw/lib/python3.11/site-packages/django/core/management/__init__.py", line 446, in execute_from_command_line
    utility.execute()
  File "/home/flynntknapp/.local/share/virtualenvs/personal-assistant-2-0-Z4bZKilw/lib/python3.11/site-packages/django/core/management/__init__.py", line 420, in execute
    django.setup()
  File "/home/flynntknapp/.local/share/virtualenvs/personal-assistant-2-0-Z4bZKilw/lib/python3.11/site-packages/django/__init__.py", line 24, in setup
    apps.populate(settings.INSTALLED_APPS)
  File "/home/flynntknapp/.local/share/virtualenvs/personal-assistant-2-0-Z4bZKilw/lib/python3.11/site-packages/django/apps/registry.py", line 116, in populate
    app_config.import_models()
  File "/home/flynntknapp/.local/share/virtualenvs/personal-assistant-2-0-Z4bZKilw/lib/python3.11/site-packages/django/apps/config.py", line 269, in import_models
    self.models_module = import_module(models_module_name)
                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1204, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1176, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1147, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 690, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 940, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/home/flynntknapp/Programming/personal-assistant-2-0/accounts/models.py", line 8, in <module>
    from vitals.models import BloodPressure
  File "/home/flynntknapp/Programming/personal-assistant-2-0/vitals/models.py", line 4, in <module>
    from base.models import CreatedUpdatedBase
  File "/home/flynntknapp/Programming/personal-assistant-2-0/base/models.py", line 28, in <module>
    class Note(CreatedUpdatedBase):
  File "/home/flynntknapp/Programming/personal-assistant-2-0/base/models.py", line 39, in Note
    get_user_model(),
    ^^^^^^^^^^^^^^^^
  File "/home/flynntknapp/.local/share/virtualenvs/personal-assistant-2-0-Z4bZKilw/lib/python3.11/site-packages/django/contrib/auth/__init__.py", line 176, in get_user_model
    raise ImproperlyConfigured(
django.core.exceptions.ImproperlyConfigured: AUTH_USER_MODEL refers to model 'accounts.CustomUser' that has not been installed
flynntknapp@DELL-DESK:~$
```

```bash
(personal-assistant-2-0) flynntknapp@DELL-DESK:~/Programming/personal-assistant-2-0$ python manage.py makemigrations accounts
Traceback (most recent call last):
  File "/home/flynntknapp/.local/share/virtualenvs/personal-assistant-2-0-Z4bZKilw/lib/python3.11/site-packages/django/apps/config.py", line 235, in get_model
    return self.models[model_name.lower()]
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^
KeyError: 'customuser'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/flynntknapp/.local/share/virtualenvs/personal-assistant-2-0-Z4bZKilw/lib/python3.11/site-packages/django/contrib/auth/__init__.py", line 170, in get_user_model
    return django_apps.get_model(settings.AUTH_USER_MODEL, require_ready=False)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/flynntknapp/.local/share/virtualenvs/personal-assistant-2-0-Z4bZKilw/lib/python3.11/site-packages/django/apps/registry.py", line 213, in get_model
    return app_config.get_model(model_name, require_ready=require_ready)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/flynntknapp/.local/share/virtualenvs/personal-assistant-2-0-Z4bZKilw/lib/python3.11/site-packages/django/apps/config.py", line 237, in get_model
    raise LookupError(
LookupError: App 'accounts' doesn't have a 'CustomUser' model.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/flynntknapp/Programming/personal-assistant-2-0/manage.py", line 26, in <module>
    main()
  File "/home/flynntknapp/Programming/personal-assistant-2-0/manage.py", line 22, in main
    execute_from_command_line(sys.argv)
  File "/home/flynntknapp/.local/share/virtualenvs/personal-assistant-2-0-Z4bZKilw/lib/python3.11/site-packages/django/core/management/__init__.py", line 446, in execute_from_command_line
    utility.execute()
  File "/home/flynntknapp/.local/share/virtualenvs/personal-assistant-2-0-Z4bZKilw/lib/python3.11/site-packages/django/core/management/__init__.py", line 420, in execute
    django.setup()
  File "/home/flynntknapp/.local/share/virtualenvs/personal-assistant-2-0-Z4bZKilw/lib/python3.11/site-packages/django/__init__.py", line 24, in setup
    apps.populate(settings.INSTALLED_APPS)
  File "/home/flynntknapp/.local/share/virtualenvs/personal-assistant-2-0-Z4bZKilw/lib/python3.11/site-packages/django/apps/registry.py", line 116, in populate
    app_config.import_models()
  File "/home/flynntknapp/.local/share/virtualenvs/personal-assistant-2-0-Z4bZKilw/lib/python3.11/site-packages/django/apps/config.py", line 269, in import_models
    self.models_module = import_module(models_module_name)
                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1204, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1176, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1147, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 690, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 940, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/home/flynntknapp/Programming/personal-assistant-2-0/accounts/models.py", line 8, in <module>
    from vitals.models import BloodPressure
  File "/home/flynntknapp/Programming/personal-assistant-2-0/vitals/models.py", line 4, in <module>
    from base.models import CreatedUpdatedBase
  File "/home/flynntknapp/Programming/personal-assistant-2-0/base/models.py", line 28, in <module>
    class Note(CreatedUpdatedBase):
  File "/home/flynntknapp/Programming/personal-assistant-2-0/base/models.py", line 39, in Note
    get_user_model(),
    ^^^^^^^^^^^^^^^^
  File "/home/flynntknapp/.local/share/virtualenvs/personal-assistant-2-0-Z4bZKilw/lib/python3.11/site-packages/django/contrib/auth/__init__.py", line 176, in get_user_model
    raise ImproperlyConfigured(
django.core.exceptions.ImproperlyConfigured: AUTH_USER_MODEL refers to model 'accounts.CustomUser' that has not been installed
(personal-assistant-2-0) flynntknapp@DELL-DESK:~/Programming/personal-assistant-2-0$
```

