import unittest

from tests import CreateAdminEvent
from tests import LoginLogout
from tests import LoginTeamCalendar
from tests import PageValidation
from tests import AdminPassword
from tests import AdminAddUser
from tests import InstructorPriveleges
from tests import UserPrivileges
from tests import ContactNavBar
from tests import ValidateUserButtons
from tests import ValidateUserAccess
from tests import AdminAddGroup

def suite():
    loader = unittest.TestLoader()
    tests = unittest.TestSuite()
    tests.addTests(loader.loadTestsFromModule(CreateAdminEvent))
    tests.addTest(loader.loadTestsFromModule(LoginLogout))
    tests.addTest(loader.loadTestsFromModule(LoginTeamCalendar))
    tests.addTest(loader.loadTestsFromModule(PageValidation))
    tests.addTest(loader.loadTestsFromModule(AdminPassword))
    tests.addTest(loader.loadTestsFromModule(AdminAddUser))
    tests.addTest(loader.loadTestsFromModule(InstructorPriveleges))
    tests.addTest(loader.loadTestsFromModule(UserPrivileges))
    tests.addTest(loader.loadTestsFromModule(ContactNavBar))
    tests.addTest(loader.loadTestsFromModule(ValidateUserButtons))
    tests.addTest(loader.loadTestsFromModule(ValidateUserAccess))
    tests.addTest(loader.loadTestsFromModule(AdminAddGroup))
    return tests


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())


