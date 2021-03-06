# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 08:32:23 2015

@author: pick
"""

import datetime
import odml
from compare_section_table import CompareSectionTable
import xlwt
from xls_style import XlsStyle


class CompareSectionXlsTable(CompareSectionTable):
    """
    class to write a CompareSectionTable to a xls-file


    :param sheet_name: name of the excel-sheet, default is 'sheet1'
    :type sheet_name: string
    :param header_style: style used for the header
    :param first_style: style used for the values inside the table
    :param second_style: second style used for the values inside the table
    :param missing_value_style: if include_all is True, this style will be used
        if a property doesnt exist in the section, so they distinguish from
        properties with empty values
    :type header_style: XlsStyle
    :type first_style: XlsStyle
    :type second_style: XlsStyle
    :type missing_value_style: XlsStyle

    """

    def __init__(self):

        CompareSectionTable.__init__(self)

        self.sheet_name = "sheet1"
        self.header_style = XlsStyle(backcolor='gray80', fontcolor='white',
                                     fontstyle='bold 1')
        self.first_style = XlsStyle(backcolor='dark_blue', fontcolor='white',
                                    fontstyle='')
        self.second_style = XlsStyle(backcolor='green', fontcolor='white',
                                     fontstyle='')
        self.missing_value_style = XlsStyle(backcolor='red',
                                            fontcolor='black', fontstyle='',)

    def write2file(self, save_to):
        """
        writes the table to an xls-file
        """
        headerstyle = xlwt.easyxf(self.header_style.get_style_string())
        missing_val_style = xlwt.easyxf(
            self.missing_value_style.get_style_string())
        row_styles = [xlwt.easyxf(self.first_style.get_style_string()),
                      xlwt.easyxf(self.second_style.get_style_string())]


        properties, sections, table = self._build_table()

        workbook = xlwt.Workbook()
        sheet = workbook.add_sheet(self.sheet_name)

        max_col_len = []

        if(self.switch):

            for i, prop in enumerate([''] + properties):
                sheet.write(0, i, prop, headerstyle)
                max_col_len.append(len(str(prop)))

            for row_num, sec in enumerate(sections):
                sheet.write(row_num + 1, 0, sec, headerstyle)

            for row_num, row in enumerate(table):
                for col_num, elem in enumerate(row):

                    if elem is None:
                        style = missing_val_style
                        cell_content = ""
                    else:
                        style = row_styles[row_num % 2]
                        cell_content = elem

                        if isinstance(cell_content, datetime.datetime):
                            style.num_format_str = "DD-MM-YYYY HH:MM:SS"
                        elif isinstance(cell_content, datetime.date):
                            style.num_format_str = "DD-MM-YYYY"
                        elif isinstance(cell_content, datetime.time):
                            style.num_format_str = "HH:MM:SS"
                        else:
                            style.num_format_str = ""

                    sheet.write(row_num + 1, col_num + 1, cell_content, style)
                    if len(str(cell_content)) > max_col_len[col_num]:
                        max_col_len[col_num] = len(str(cell_content))

        else:

            for i, sec in enumerate([''] + sections):
                sheet.write(0, i, sec, headerstyle)
                max_col_len.append(len(str(sec)))

            for row_num, prop in enumerate(properties):
                sheet.write(row_num + 1, 0, prop, headerstyle)

            for col_num, col in enumerate(table):
                for row_num, elem in enumerate(col):

                    if elem is None:
                        style = missing_val_style
                        cell_content = ""
                    else:
                        style = row_styles[row_num % 2]
                        cell_content = elem

                        if isinstance(cell_content, datetime.datetime):
                            style.num_format_str = "DD-MM-YYYY HH:MM:SS"
                        elif isinstance(cell_content, datetime.date):
                            style.num_format_str = "DD-MM-YYYY"
                        elif isinstance(cell_content, datetime.time):
                            style.num_format_str = "HH:MM:SS"
                        else:
                            style.num_format_str = ""

                    sheet.write(row_num + 1, col_num + 1, cell_content, style)
                    if len(str(cell_content)) > max_col_len[col_num]:
                        max_col_len[col_num] = len(str(cell_content))


#        if self.switch:
#                csvwriter.writerow([''] + properties)
#
#                for i, line in enumerate(table):
#                    csvwriter.writerow([sections[i]] + line)
#
#            else:
#                csvwriter.writerow([''] + sections)
#
#                for i in range(len(table[0])):
#                    csvwriter.writerow([properties[i]] + [table[j][i]
#                                       for j in range(len(table))])
#
#        for col, h in enumerate(header):
#            sheet.write(0, col, h, headerstyle)
#            max_col_len.append(len(h))
#
#        for row, dic in enumerate(table):
#            for col, h in enumerate(header):
#                if h in table[dic]:
#                    cell_content = table[dic][h]
#                    style = row_styles[row % 2] if col > 0 else headerstyle
#                    if isinstance(cell_content, datetime.datetime):
#                        style.num_format_str = "DD-MM-YYYY HH:MM:SS"
#                    elif isinstance(cell_content, datetime.date):
#                        style.num_format_str = "DD-MM-YYYY"
#                    elif isinstance(cell_content, datetime.time):
#                        style.num_format_str = "HH:MM:SS"
#                    else:
#                        style.num_format_str = ""
#                else:
#                    cell_content = ""
#                    style = missing_val_style
#
#                sheet.write(row+1, col, cell_content, style)
#                if len(str(cell_content)) > max_col_len[col]:
#                    max_col_len[col] = len(str(cell_content))
#
#        # adjust width of he columns
#        for col in range(len(header)):
#            sheet.col(col).width = (256 * (max_col_len[col]+1))
        workbook.save(save_to)
