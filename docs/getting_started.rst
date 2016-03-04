.. _getting_started:


***************
Getting started
***************

Introduction
============

This is the place for people that are new to anapioficeandfire. This tutorial will help you to get started with anapioficeandfire. Note that we won't go too much
into detail, just the most important basic functionality.

Installation
============

At the command line::

    $ pip install anapioficeandfire

First example
============

.. code-block :: python

   import anapioficeandfire

   api = anapioficeandfire.API()

   jon_snow = api.get_character(id=583)
   for title in jon_snow.aliases:
       print(title)

This example will download all data about the character Jon Snow and print each one of his aliases to the console.

API
============
The API class provides access to the entire An API of Ice And Fire in a clean and "pythonic" way. Each method accepts various parameters and return responses. Fore detailed information about the methods, please refer to :ref:`API Reference <api_reference>`.

Models
============
