# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

import sqlite3



class FirstprojectscrapyPipeline:
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect("mydatabase.db")
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS demo_tb""")
        self.curr.execute(""" create table  demo_tb(
  
   h3 text
) """ )


    def process_item(self, item, spider):
        self.store_db(item)
        print("Pipeline :" + item['h3'][0])
        return item

    def store_db(self, item):
        self.curr.execute(""" insert into demo_tb  values(?)""",(
        item['h3'][0],
    
        ))

        self.conn.commit()
    
