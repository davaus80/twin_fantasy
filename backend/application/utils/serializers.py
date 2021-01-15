import json

def serialize_one(result):
    return json.dumps(result.to_dict())

def serialize_many(results):
    data = [res.to_dict() for res in results]
    result_dict = {"results": data}
    return result_dict