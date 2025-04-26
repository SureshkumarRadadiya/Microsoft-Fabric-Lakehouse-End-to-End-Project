# Welcome to your new notebook
# Type here in the cell editor to add code!
from notebookutils import mssparkutils

mssparkutils.fs.mount("abfss://1df115cc-23f0-4d1d-9a90-aad986d02161@onelake.dfs.fabric.microsoft.com/f79a512c-ee42-4057-bc18-ce8433d05b40/Files","/Files")

mssparkutils.fs.getMountPath("/Files")

check_files=mssparkutils.fs.ls(f"file://{mssparkutils.fs.getMountPath('/Files')}/Current/")

check_files

if check_files:
    mssparkutils.notebook.run('bronze_sales')
    mssparkutils.notebook.run('gold_customer')
    mssparkutils.notebook.run('gold_date')
    mssparkutils.notebook.run('gold_fact_sale')
    mssparkutils.notebook.run('gold_orderpriority')
    mssparkutils.notebook.run('gold_orderreturn')
    mssparkutils.notebook.run('gold_product')
    mssparkutils.notebook.run('gold_shipmode')