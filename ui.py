import utils
from db import cur
from utils import ResponseData, BadRequest, session
import service
from typing import Union

from colorama import Fore

from dto import UserRegisterDTO


def print_response(response: Union[ResponseData, BadRequest]):
    color = Fore.GREEN if response.status_code == 200 else Fore.RED
    print(color + response.data + Fore.RESET)


def login():
    username = input('Enter your username: ')
    password = input('Enter your password: ')
    response = service.login(username, password)
    print_response(response)


def register():
    username = input('Enter your username: ')
    password = input('Enter your password: ')
    dto: UserRegisterDTO = UserRegisterDTO(username, password)
    response = service.register(dto)
    print_response(response)


def logout():
    response = service.logout()
    print_response(response)


def todo_add():
    title = input('Enter title : ')
    response = service.todo_add(title)
    print_response(response)


def todo_get_all():
    get_all_query = """select * from todos where user_id = %s"""
    cur.execute(get_all_query, (session.session.id,))
    all_items = cur.fetchall()
    for i in all_items:
        print(i)
    return all_items


def todo_get_all_titles():
    get_all_query = """select * from todos where user_id = %s"""
    cur.execute(get_all_query, (session.session.id,))
    all_items = cur.fetchall()
    for i in all_items:
        print(i[1])


def todo_update():
    print("List of todos: ")
    todo_get_all_titles()
    new_title = input("Enter new title: ")
    old_title = input("Which todo needs to change: ")
    all_data = todo_get_all()
    for i in all_data:
        if old_title in i[1]:
            response = service.todo_update(new_title, old_title)
            print_response(response)
        else:
            print_response(utils.BadRequest("Nothing to update"))


def todo_delete():
    print("List of todos: ")
    todo_get_all_titles()
    title = input("Enter title: ")
    all_data = todo_get_all()
    for i in all_data:
        if title in i[1]:
            response = service.todo_delete(title)
            print_response(response)
        else:
            print_response(utils.BadRequest("Nothing to delete"))


def menu():
    print('1. Login')
    print('2. Register')
    print('3. Logout')
    print('4. Todo Add')
    print("5. Get all todos")
    print("6. Todo Update")
    print("7. Todo Delete")
    print('q.  Exit ')
    return input('Enter your choice ?: ')


if __name__ == '__main__':
    while True:
        choice = menu()
        if choice == '1':
            login()
        elif choice == '2':
            register()
        elif choice == '3':
            logout()
        elif choice == '4':
            todo_add()
        elif choice == "5":
            todo_get_all()
        elif choice == "6":
            todo_update()
        elif choice == "7":
            todo_delete()
        elif choice == 'q':
            break
