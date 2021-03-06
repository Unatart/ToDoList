from tests.unit_test_signup import SignUpTests
from tests.unit_test_login import LoginTests
from tests.system_test_signup import sysSignUpTest
from tests.system_test_login import sysLoginTest
from tests.integration_tests import DBmanager_test
from tests.system_test_admin import sysAdminTest
from tests.system_test_todo import sysTodoTest

import unittest
import filecmp


if __name__ == "__main__":
    runner = unittest.TextTestRunner()

    all = True

    routes_bool = filecmp.cmp('/home/unatart/TodoList/routes/routes.py',
                              '/home/unatart/git/ToDoList/routes/routes.py')
    db_bool = filecmp.cmp('/home/unatart/TodoList/DBmanager/DBmanager.py',
                          '/home/unatart/git/ToDoList/DBmanager/DBmanager.py')
    int_bool = filecmp.cmp('/home/unatart/TodoList/tests/integration_tests.py',
                           '/home/unatart/git/ToDoList/tests/integration_tests.py')
    sys_login = filecmp.cmp('/home/unatart/TodoList/tests/system_test_login.py',
                            '/home/unatart/git/ToDoList/tests/system_test_login.py')
    sys_signup = filecmp.cmp('/home/unatart/TodoList/tests/system_test_signup.py',
                            '/home/unatart/git/ToDoList/tests/system_test_signup.py')
    unit_login = filecmp.cmp('/home/unatart/TodoList/tests/unit_test_login.py',
                            '/home/unatart/git/ToDoList/tests/unit_test_login.py')
    unit_signup = filecmp.cmp('/home/unatart/TodoList/tests/unit_test_signup.py',
                            '/home/unatart/git/ToDoList/tests/unit_test_signup.py')
    admin = filecmp.cmp('/home/unatart/TodoList/tests/system_test_admin.py',
                        '/home/unatart/git/ToDoList/tests/system_test_admin.py')
    todo = filecmp.cmp('/home/unatart/TodoList/tests/system_test_todo.py',
                        '/home/unatart/git/ToDoList/tests/system_test_todo.py')

    if all == True:
        print('Run all tests: \n')
        runner.run(unittest.TestSuite((
            unittest.makeSuite(SignUpTests),
            unittest.makeSuite(LoginTests),
            unittest.makeSuite(sysSignUpTest),
            unittest.makeSuite(sysLoginTest),
            unittest.makeSuite(sysAdminTest),
            unittest.makeSuite(sysTodoTest),
            unittest.makeSuite(DBmanager_test)
        )))

    if routes_bool == False:
        print('Run tests for routes.py: \n')
        runner.run(unittest.TestSuite((
            unittest.makeSuite(SignUpTests),
            unittest.makeSuite(LoginTests),
            unittest.makeSuite(sysSignUpTest),
            unittest.makeSuite(sysLoginTest),
            unittest.makeSuite(sysAdminTest),
            unittest.makeSuite(sysTodoTest)
        )))

    if db_bool == False:
        print('Run tests for DBmanager.py: \n')
        runner.run(unittest.TestSuite((
            unittest.makeSuite(sysSignUpTest),
            unittest.makeSuite(sysLoginTest),
            unittest.makeSuite(sysAdminTest),
            unittest.makeSuite(sysTodoTest),
            unittest.makeSuite(DBmanager_test),
        )))

    if int_bool == False:
        print('Run integration tests: \n')
        runner.run(unittest.TestSuite((
           unittest.makeSuite(DBmanager_test)
        )))

    if sys_login == False:
        print('Run system tests for login: \n')
        runner.run(unittest.TestSuite((
            unittest.makeSuite(sysLoginTest)
        )))

    if sys_signup == False:
        print('Run system tests for signup: \n')
        runner.run(unittest.TestSuite((
            unittest.makeSuite(sysSignUpTest)
        )))

    if unit_login == False:
        print('Run unit tests for login: \n')
        runner.run(unittest.TestSuite((
            unittest.makeSuite(LoginTests)
        )))

    if unit_signup == False:
        print('Run unit tests for signup: \n')
        runner.run(unittest.TestSuite((
            unittest.makeSuite(SignUpTests)
        )))

    if admin == False:
        print('Run system tests for admin: \n')
        runner.run(unittest.TestSuite((
            unittest.makeSuite(sysAdminTest)
        )))

    if todo == False:
        print('Run system tests for todo: \n')
        runner.run(unittest.TestSuite((
           unittest.makeSuite(sysTodoTest)
        )))




