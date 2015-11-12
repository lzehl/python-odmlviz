Introduction
============
odML is a metadata framework which was first introduced by `Grewe et al. 2011 
<http://journal.frontiersin.org/article/10.3389/fninf.2011.00016/abstract>`_ 
:sub:`1`_ as a `G-Node project <http://www.g-node.org/projects/odml>`_ and is also 
openly available on `GitHub <https://github.com/G-Node/python-odml>`_.
odML was developed to hierarchically organize and save metadata into a human 
and machine readable format. Although the hierarchical structure of an odML 
file optimizes the organization of metadata, it aggravates to keep an overview 
of the content and to manually edit the file.
As a solution we provide here an add-on module called odmlviz which gives you 
the possibility to transform hierarchically organized metadata from an odML 
file into a flat table format (csv or xls). The table representation of the 
odML file can easily be edited and afterwards turned back to an odML-file. 
Additionally, we provide the possibility to extract repeating structures of the
odML file (e.g. the sections for each electrode of an multielectrode array) and
display the corresponding metadata in an easy readable overview table.
In this documentation you will find a summary of the available functions and a 
tutorial which explains you how to use the odmlviz module.

.. _:sub:`1` Grewe J, Wachtler T and Benda J (2011) A bottom-up approach to data 
   annotation in neurophysiology. Front. Neuroinform. 5:16
