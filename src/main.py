from src.repository.ManufacturerRepository import ManufacturerRepository
from src.repository.MarketplaceRepository import MarketplaceRepository
from src.repository.ProductRepository import ProductRepository

if __name__ == "__main__":
    init_manufacturer = ManufacturerRepository()
    init_marketplace = MarketplaceRepository()
    init_product = ProductRepository()