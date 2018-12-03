import unittest

from tests import CreateAdminEvent
from tests import CreateDeleteCalendar
from tests import LoginLogout
from tests import LoginTeamCalendar
from tests import PageValidation
from tests import AdminPassword
from tests import AdminAddUser
from tests import InstructorPriveleges
from tests import UserPrivileges


def suite():
    loader = unittest.TestLoader()
    tests = unittest.TestSuite()
    tests.addTests(loader.loadTestsFromModule(CreateAdminEvent))
    #tests.addTests(loader.loadTestsFromModule(CreateDeleteCalendar))
    tests.addTest(loader.loadTestsFromModule(LoginLogout))
    tests.addTest(loader.loadTestsFromModule(LoginTeamCalendar))
    tests.addTest(loader.loadTestsFromModule(PageValidation))
    tests.addTest(loader.loadTestsFromModule(AdminPassword))
    tests.addTest(loader.loadTestsFromModule(AdminAddUser))
    tests.addTest(loader.loadTestsFromModule(InstructorPriveleges))
    tests.addTest(loader.loadTestsFromModule(UserPrivileges))
    return tests


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())


