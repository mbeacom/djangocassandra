.. _quickstart:

Getting Started
===============

This page will help you get up and running quickly with a basic environment.  If you haven't installed Apache Cassandra yet follow the instructions here: :ref:`installcassandra`

.. _quickinstallation:

Installation
------------

    | ``pip install djangocassandra``
    | ``pip install git+https://github.com/kavdev/djangotoolbox.git@patch-1``

.. _quickconfiguration:
  
Configuration (settings.py)
---------------------------
    
Set database backend to djangocassandra.db.backends.cassandra.
