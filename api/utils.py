import logging
import uuid

from app_service.models import Link

logger = logging.getLogger(__name__)


def create_link(link, return_data=True):
    link_code = uuid.uuid4()
    protocol = link.split(":")[0]
    domain = (
        link.split("//")[1].split(".")[0]
        if "www" not in link.split("//")[1].split(".")
        else link.split("//")[1].split(".")[1]
    )
    domain_zone = (
        link.split("//")[1].split(".")[1].split("/")[0]
        if "www" not in link.split("//")[1].split(".")
        else link.split("//")[1].split(".")[-1].split("/")[0]
    )
    path = (
        "".join(link.split(domain_zone)[1].split("?")[0])
        if "?" in link
        else "".join(link.split(domain_zone)[1])
    )

    get_parameters = link.split("?")[1] if "?" in link else ""
    parameters = {}
    if get_parameters:
        if "&" in get_parameters:
            param_pairs = get_parameters.split("&")
            for pair in param_pairs:
                key_value = pair.split("=")
                key, value = key_value
                parameters[key] = value
        else:
            key_value = get_parameters.split("=")
            key, value = key_value
            parameters[key] = value

    try:
        link_obj = Link.objects.create(
            link_code=uuid.uuid4(),
            protocol=protocol,
            domain=domain,
            domain_zone=domain_zone,
            path=path,
            parameters=parameters,
        )
        logger.info(f"Object of Link has been created | ID - {link_obj.id}")
    except Exception as error:
        print(f"[ERROR]: {error}")

    if return_data:
        link_data = {
            "code": link_code,
            "protocol": protocol,
            "domain": domain,
            "domain_zone": domain_zone,
            "path": path,
            "parameters": parameters,
        }
        return link_data
