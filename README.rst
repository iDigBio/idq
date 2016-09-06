Integrated Data Quality (IDQ)

===

IDQ is a software package for building data quality processes to maximize their ability to integrate into diverse workflows. The ultimate goal of the project is to provide a robust set of pre-packaged test, assertion and correction tools that can be utilized by users of all skill levels across a wide variety of biodiversity data.  It grew out of work done on data quality at the iDigBio project and is being spun out of the main code base in order to open up the tools and methods used to a broader community of users. The base library provides tools and interfaces for easily constructing efficient data quality workflows, and separate modules build upon the core to provide the actual library of tests and assertions. It is intended to be usable at all scales, from working on individual records to aggregator sized data processing pipelines and all the steps in between.


Production Setup
================

.. code-block::
    
    pip install idq

Development Setup
=================

.. code-block::

    git clone https://github.com/iDigBio/idq.git
    cd idq
    pip install -r requirements.txt
    python -m idq.example
