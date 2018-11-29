import pytest
from pytest_factoryboy import register

from home import factories

register(factories.HomePageFactory)
register(factories.ContactPageFactory)
register(factories.ProjectPageFactory)
register(factories.PortfolioPageFactory)
register(factories.TagFactory)
register(factories.TechnologyInfoFactory)
register(factories.TechnologiesPageFactory)
register(factories.SiteFactory)


@pytest.fixture(autouse=True)
def default_site(site_factory):
    return site_factory.create(is_default_site=True)
