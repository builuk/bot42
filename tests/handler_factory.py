import pytest
from factory.handler_factory import HandlerFactory
from handlers.base_handler import BaseHandler
from handlers.admin_handler import AdminHandler
from handlers.seller_handler import SellerHandler

def test_handler_factory_creation_admin():
    factory = HandlerFactory()
    admin_handler = factory.create_handler("admin")
    assert isinstance(admin_handler, AdminHandler)

def test_handler_factory_creation_seller():
    factory = HandlerFactory()
    seller_handler = factory.create_handler("seller")
    assert isinstance(seller_handler, SellerHandler)

def test_handler_factory_invalid_type():
    factory = HandlerFactory()
    with pytest.raises(ValueError):
        factory.create_handler("invalid_type")
