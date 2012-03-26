=================
django-propaganda
=================

Hey you, political leader, founder of a new religion or spiritual guru! With
this application, your acolytes will receive the official organizational
propaganda pamphlets right into their inboxes. Keep them updated with the Truth!

This simple Django application is made to be used for trivial newsletter
(**pamphlets**) deliveries with your information (**propaganda**), where you
supply the raw content (both plain text and HTML versions). Subscribers
(**subscribers**) will receive the emails.

Installation
============

#. Install the latest version::

   pìp install -e git+git://github.com/nabucosound/django-propaganda#egg=django-propaganda

#. Add ``propaganda`` to your ``INSTALLED_APPS`` setting.

#. If you use South for migration management (you should!) just run the
   migrations::

        python manage.py migrate propaganda

   Otherwise, update your database the Django standard way::

        python manage.py syncdb

