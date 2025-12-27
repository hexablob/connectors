"""Entry point for isMalicious OpenCTI connector."""

from pycti import OpenCTIConnectorHelper

from .connector import IsMaliciousConnector
from .connector.models import ConfigLoader


def main():
    """Initialize and run the connector."""
    # Load configuration
    config = ConfigLoader.from_env()

    # Initialize OpenCTI helper
    helper = OpenCTIConnectorHelper(
        {
            "id": config.connector.id,
            "type": config.connector.type,
            "name": config.connector.name,
            "scope": config.connector.scope,
            "log_level": config.connector.log_level,
            "auto": config.connector.auto,
        }
    )

    # Create and run connector
    connector = IsMaliciousConnector(config, helper)
    connector.run()


if __name__ == "__main__":
    main()
