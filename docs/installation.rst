============
Installation
============

#. Install the latest version::

    pip install django-propaganda

#. Add ``propaganda`` to your ``INSTALLED_APPS`` setting. One possible method::

    INSTALLED_APPS = INSTALLED_APPS + ('propaganda',)

#. If you use South for migration management (you should!) just run the
   migrations::

    python manage.py migrate propaganda

#. Otherwise, update your database the Django standard way (the good old
   ``syncdb``)::

    python manage.py syncdb

