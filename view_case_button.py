import pygame
import openpyxl

workbook = openpyxl.Workbook()
# Select the default sheet (usually named 'Sheet')
sheet = workbook.active

class ViewCaseButton:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load('View Case Database Button (1).png')
        self.case_spreadsheet = openpyxl.Workbook()
        self.sheet = self.case_spreadsheet.active
        self.mouse_pos = pygame.mouse.get_pos()
        self.view_case_database_button_clicked = False
        # self.data = data
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def collide_point(self, x, y, mouse_pos, view_case_database_button_clicked):
        if self.mouse_pos == (self.x, self.y):
            self.view_case_database_button_clicked = True

    def case_spreadsheet(self, case_spreadsheet, data):
        # Fix these errors
        for row in data:
            sheet.append(row)
        case_spreadsheet.save(sheet.xlsx)
