# напиши здесь код основного приложения и первого экранаfrom PyQt5.QtCore import Qt
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QLineEdit, QHBoxLayout, QListWidget, QTextEdit, QVBoxLayout
import json
from random import *

app = QApplication([])
window = QWidget()

list_countries = QListWidget()
text_countries = QTextEdit()
name_countries = QLineEdit()
name_countries.setPlaceholderText('Введите название приложения')
button_add = QPushButton('Добавьте приложение')
button_del = QPushButton('Удалить приложение')
button_edit = QPushButton('Изменить описание приложения')
button_d = QPushButton('Сгенерировать случайное приложение')

main_layout = QHBoxLayout()
second_layout = QVBoxLayout()
buttons_layout = QHBoxLayout()

buttons_layout.addWidget(button_add)
buttons_layout.addWidget(button_edit)
buttons_layout.addWidget(button_del)
buttons_layout.addWidget(button_d)

second_layout.addWidget(text_countries)
second_layout.addWidget(name_countries)
second_layout.addLayout(buttons_layout)

main_layout.addWidget(list_countries)
main_layout.addLayout(second_layout)

window.setLayout(main_layout)

with open('countries.json', 'r', encoding='utf-8') as file:
    countries = json.load(file)
    for country in countries:
        list_countries.addItem(country)

def show_winner():
    countries = {}
    with open('countries.json', 'r', encoding='utf-8') as file:
        countries = json.load(file)
    random_country_num = randint(1, 100)
    if random_country_num <= 25:
        random_country = 'Google go'
    if random_country_num > 25 and random_country_num <= 50:
        random_country = 'eGov mobile'
    if random_country_num > 50 and random_country_num <= 75:
        random_country = 'Быстрые настройки'
    if random_country_num > 75:
        random_country = 'YouTube'
    countries[random_country] = ''
    list_countries.addItem(random_country)
    with open('countries.json', 'w', encoding='utf-8') as file:
        json.dump(countries, file)

def add_country():
    countries = {}
    with open('countries.json', 'r', encoding='utf-8') as file:
        countries = json.load(file)
    country = name_countries.text()
    countries[country] = ''
    list_countries.addItem(country)
    with open('countries.json', 'w', encoding='utf-8') as file:
        json.dump(countries, file)

def info_country():
    country = list_countries.selectedItems()[0].text()
    with open('countries.json', 'r', encoding='utf-8') as file:
        countries = json.load(file)
    text_countries.setText(countries[country])

def edit_country():
    if list_countries.selectedItems():
        country = list_countries.selectedItems()[0].text()
        text = text_countries.toPlainText()
        with open('countries.json', 'r', encoding='utf-8') as file:
            countries = json.load(file)
        countries[country] = text
        with open('countries.json', 'w', encoding='utf-8') as file:
            json.dump(countries, file)
        text_countries.clear()
    else:
        pass

def del_country():
    if list_countries.selectedItems():
        country = list_countries.selectedItems()[0].text()
        with open('countries.json', 'r', encoding='utf-8') as file:
            countries = json.load(file)
        del countries[country]
        text_countries.clear()
        list_countries.clear()
        for country in countries:
            list_countries.addItem(country)
        with open('countries.json', 'w', encoding='utf-8') as file:
            json.dump(countries, file)
    else:
        pass

button_add.clicked.connect(add_country)
button_edit.clicked.connect(edit_country)
button_del.clicked.connect(del_country)
button_d.clicked.connect(show_winner)
list_countries.itemClicked.connect(info_country)

window.show()
app.exec()
