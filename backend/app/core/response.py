from typing import Any


def success_response(data: Any = None, message: str = "Success", code: int = 200) -> dict:
    return {"code": code, "success": True, "message": message, "data": data}


def error_response(message: str, code: int = 400, detail: Any = None) -> dict:
    return {"code": code, "success": False, "message": message, "data": detail}


def paginated_response(items: list, total: int, page: int, page_size: int) -> dict:
    return success_response(
        data={"items": items, "total": total, "page": page, "page_size": page_size}
    )
