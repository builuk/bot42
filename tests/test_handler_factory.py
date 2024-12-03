import pytest
from factory.handler_factory import CommandHandlerFactory
from handlers.admin_handler import AdminHandler
from handlers.seller_handler import SellerHandler
from handlers.buyer_handler import BuyerHandler
from handlers.guest_handler import GuestHandler


def test_handler_factory_creation_admin():
    factory = CommandHandlerFactory()
    admin_handler = factory.get_handler("admin")
    assert isinstance(admin_handler, AdminHandler)


def test_handler_factory_creation_seller():
    factory = CommandHandlerFactory()
    seller_handler = factory.get_handler("seller")
    assert isinstance(seller_handler, SellerHandler)


def test_handler_factory_creation_buyer():
    factory = CommandHandlerFactory()
    buyer_handler = factory.get_handler("buyer")
    assert isinstance(buyer_handler, BuyerHandler)


def test_handler_factory_invalid_type():
    factory = CommandHandlerFactory()
    guest_handler = factory.get_handler("invalid_type")
    assert isinstance(guest_handler, GuestHandler)
