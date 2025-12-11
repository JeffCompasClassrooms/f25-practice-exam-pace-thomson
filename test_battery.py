import pytest
from battery import Battery
from unittest.mock import Mock

@pytest.fixture
def charged_battery():
    return Battery(100)

@pytest.fixture
def partially_charged_battery():
    b = Battery(100)
    b.mCharge = 70
    return b

def describe_battery():

    def init_creates_battery(partially_charged_battery):
        assert isinstance(partially_charged_battery, Battery)

    def getCapacity_returns_the_capacity(partially_charged_battery):
        assert partially_charged_battery.getCapacity() is 100

    def getCharge_returns_the_Charge(partially_charged_battery):
        assert partially_charged_battery.getCharge() is 70

    def recharge_changes_charge(partially_charged_battery):
        partially_charged_battery.recharge(20)
        assert partially_charged_battery.mCharge is 90

    def recharge_doesnt_exceed_100(partially_charged_battery):
        partially_charged_battery.recharge(40)
        assert partially_charged_battery.mCharge is 100

    def it_calls_monitor_on_recharge(partially_charged_battery):
        # setup
        mock_monitor = Mock()
        battery = partially_charged_battery # use the fixture
        battery.external_monitor = mock_monitor

        # execute
        battery.recharge(20)   # battery starts at 70, add 20

        # validate
        mock_monitor.notify_recharge.assert_called_once_with(90)

    #put more test cases here.
