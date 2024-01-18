from Windows.common_tk_classes import *

class WindowShow(Window):
    def __init__(self, title, desc, table) -> None:
        Window.__init__(self, title)
        self.table = table
        self.desc = desc

    def vis(self):
        # tree
        create_treeview(self.window, self.desc,  get_select(f"SELECT * FROM {self.table};" ), 
        get_select(
            f"""
            SELECT COLUMN_NAME
            FROM INFORMATION_SCHEMA.COLUMNS
            WHERE TABLE_NAME = '{self.table}';"""), 10)
        # 