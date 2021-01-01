=====================
google-search-scraper
=====================


.. image:: https://img.shields.io/pypi/v/google-search-scraper.svg
        :target: https://pypi.python.org/pypi/google-search-scraper

.. image:: https://img.shields.io/travis/nidhaloff/google-search-scraper.svg
        :target: https://travis-ci.com/nidhaloff/google-search-scraper

.. image:: https://readthedocs.org/projects/google-search-scraper/badge/?version=latest
        :target: https://google-search-scraper.readthedocs.io/en/main
        :alt: Documentation Status



a python package to scrape google search results


* Free software: Apache Software License 2.0
* Documentation: https://google-search-scraper.readthedocs.io.


Usage
------

.. code-block:: python

    from google_search_scraper import GoogleScraper

    your_text = 'something interesting'
    results = GoogleScraper().search(your_text)


